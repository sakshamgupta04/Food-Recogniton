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

def predict_food(image_path, top_k=5):
    """
    Predicts the food category from an image file.
    Returns:
        top_name (str): The top predicted food dish.
        top_confidence (float): Confidence percentage of the top dish.
        top_predictions (list): List of dicts with name & confidence for top K predictions.
    """
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=-1)
        top_probs, top_indices = torch.topk(probs, min(top_k, probs.shape[-1]))

    top_predictions = []
    for prob, idx in zip(top_probs[0], top_indices[0]):
        raw_label = model.config.id2label[idx.item()]
        conf = round(prob.item() * 100.0, 1)
        formatted_name = raw_label.replace("_", " ").title()
        top_predictions.append({
            "name": formatted_name,
            "confidence": conf
        })

    top_name = top_predictions[0]["name"]
    top_confidence = top_predictions[0]["confidence"]

    return top_name, top_confidence, top_predictions
