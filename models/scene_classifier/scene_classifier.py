import torch
import clip
from PIL import Image
from .prompts import SCENE_LABELS

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load CLIP model once
model, preprocess = clip.load("ViT-B/32", device=device)


def classify_scene(image: Image.Image):
    """
    Returns scene classification:
    {
        'indoor_outdoor': 'indoor scene',
        'nature_urban': 'urban city environment',
        'portrait_landscape': 'portrait of a person'
    }
    """

    image_input = preprocess(image).unsqueeze(0).to(device)
    results = {}

    with torch.no_grad():
        image_features = model.encode_image(image_input)

    for category, texts in SCENE_LABELS.items():
        text_tokens = clip.tokenize(texts).to(device)

        with torch.no_grad():
            text_features = model.encode_text(text_tokens)

            # similarity
            logits = (image_features @ text_features.T).softmax(dim=-1)
            best = logits.argmax().item()

        results[category] = texts[best]

    return results
