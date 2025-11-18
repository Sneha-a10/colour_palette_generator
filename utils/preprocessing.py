from PIL import Image


def load_image_as_pil(path):
    return Image.open(path).convert("RGB")
