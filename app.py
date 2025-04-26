from flask import Flask, render_template, request, jsonify
from PIL import Image
import os
from collections import Counter
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
NUM_DOMINANT_COLORS = 5  

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_dominant_colors(image_path, num_colors=NUM_DOMINANT_COLORS):
    try:
        image = Image.open(image_path).convert('RGB')
        image = image.resize((200, 200))  
        pixels = np.array(image.getdata())
        
        kmeans = KMeans(n_clusters=num_colors, random_state=0, n_init=10)
        kmeans.fit(pixels)
        
        dominant_colors = kmeans.cluster_centers_.astype(int).tolist()
        
        hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in dominant_colors]
        return hex_colors
    except Exception as e:
        print(f"Error processing image: {e}")
        return []

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
        dominant_colors = get_dominant_colors(filename)
        os.remove(filename)  
        return jsonify({'colors': dominant_colors}), 200
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)