import os
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification

# Suppress verbose log warnings
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_MODEL_DIR = os.path.join(BASE_DIR, "models", "food_classifier")
MODEL_ID = "nateraw/food"

print("Loading Food Classifier model...")
if os.path.isdir(LOCAL_MODEL_DIR) and os.path.exists(os.path.join(LOCAL_MODEL_DIR, "config.json")):
    print(f"Loading from local weights: {LOCAL_MODEL_DIR}")
    processor = AutoImageProcessor.from_pretrained(LOCAL_MODEL_DIR, local_files_only=True)
    model = AutoModelForImageClassification.from_pretrained(LOCAL_MODEL_DIR, local_files_only=True)
else:
    print(f"Loading from Hugging Face hub: {MODEL_ID}")
    processor = AutoImageProcessor.from_pretrained(MODEL_ID)
    model = AutoModelForImageClassification.from_pretrained(MODEL_ID)

model.eval()
print("Food Classifier loaded successfully!")

def predict_food(image_path):
    """
    Predicts the food category from an image file.
    Returns: (food_name, confidence_percent)
    """
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=-1)
        top_prob, top_idx = torch.topk(probs, 1)

    predicted_label = model.config.id2label[top_idx.item()]
    confidence = top_prob.item() * 100.0

    # Format label e.g., 'spaghetti_bolognese' -> 'Spaghetti Bolognese'
    formatted_label = predicted_label.replace("_", " ").title()
    return formatted_label, round(confidence, 1)
