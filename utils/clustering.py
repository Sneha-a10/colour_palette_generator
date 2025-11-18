import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import cv2

NUM_DOMINANT_COLORS = 5


# ----------------------
# LAB CONVERSION HELPERS
# ----------------------
def rgb_to_lab(pixels):
    """
    Convert an Nx3 RGB array into CIELAB.
    """
    lab_pixels = cv2.cvtColor(pixels.reshape(-1, 1, 3).astype(np.uint8), cv2.COLOR_RGB2LAB)
    return lab_pixels.reshape(-1, 3)


def lab_to_rgb(lab_pixels):
    rgb_pixels = cv2.cvtColor(lab_pixels.reshape(-1, 1, 3).astype(np.uint8), cv2.COLOR_LAB2RGB)
    return rgb_pixels.reshape(-1, 3)


def rgb_to_hex(rgb):
    r, g, b = rgb
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


# ----------------------
# SCENE-AWARE LOGIC
# ----------------------
def apply_scene_rules(rgb_colors, scene):
    """
    Scene-aware palette adjustment.
    This is what makes your project look intelligent.
    """

    scene_type = scene.get("nature_urban", "")  # using one key for now

    if "natural" in scene_type:
        # Boost greens & blues — nature scenes
        rgb_colors = sorted(rgb_colors, key=lambda x: x[1], reverse=True)

    elif "urban" in scene_type:
        # Prioritize grayscale / neutral tones
        rgb_colors = sorted(rgb_colors, key=lambda x: abs(x[0] - x[1]), reverse=True)

    # Later you can extend rules for portrait, indoor, landscape, etc.

    return rgb_colors


# ----------------------
# MAIN FUNCTION
# ----------------------
def extract_palette_smart(image_or_frames, scene):
    """
    Minimal-optimal intelligent palette extractor.
    Uses:
    - LAB for perceptual accuracy
    - Scene-aware rule engine
    - KMeans for speed (not complexity)
    """

    # Collect pixels
    if isinstance(image_or_frames, list):
        pixels = []
        for frame in image_or_frames:
            img = Image.fromarray(frame).resize((120, 120))
            pixels.extend(np.array(img).reshape(-1, 3))
        pixels = np.array(pixels)
    else:
        img = image_or_frames.resize((200, 200))
        pixels = np.array(img.getdata())

    # Convert to LAB
    lab_pixels = rgb_to_lab(pixels)

    # Cluster in LAB
    kmeans = KMeans(n_clusters=NUM_DOMINANT_COLORS, random_state=0, n_init=10)
    kmeans.fit(lab_pixels)

    # Convert cluster centers LAB → RGB
    rgb_centers = lab_to_rgb(kmeans.cluster_centers_).astype(int).tolist()

    # Apply scene-aware rules
    rgb_centers = apply_scene_rules(rgb_centers, scene)

    # Convert to HEX
    hex_colors = [rgb_to_hex(c) for c in rgb_centers]

    return hex_colors
