from flask import Flask, render_template, request, jsonify
from PIL import Image
import os
import numpy as np

# Scene classifier
from models.scene_classifier.scene_classifier import classify_scene

# Utils
from utils.video_processing import get_representative_frames
from utils.preprocessing import load_image_as_pil
from utils.clustering import extract_palette_smart

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4', 'mov', 'avi', 'mkv'}
NUM_DOMINANT_COLORS = 5

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # -----------------------------
        # VIDEO PROCESSING
        # -----------------------------
        if filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
            # Use intelligent frame selection
            frames = get_representative_frames(filename, max_frames=7)

            if len(frames) == 0:
                return jsonify({'error': 'Could not extract frames'}), 500

            # Take the middle selected frame for scene classification
            mid_frame = Image.fromarray(frames[len(frames) // 2])

            # Scene detection
            scene = classify_scene(mid_frame)

            # Smart palette extraction (LAB + rules + KMeans)
            palette = extract_palette_smart(frames, scene)

        # -----------------------------
        # IMAGE PROCESSING
        # -----------------------------
        else:
            image = load_image_as_pil(filename)

            # Scene detection
            scene = classify_scene(image)

            # Smart palette extraction
            palette = extract_palette_smart(image, scene)

        # Clean up uploaded file
        os.remove(filename)

        return jsonify({
            'colors': palette,
            'scene': scene
        }), 200

    return jsonify({'error': 'Invalid file type'}), 400


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
