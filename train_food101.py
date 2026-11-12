"""
=============================================================================
Food Recognition & Recipe Finder - YOLOv8 Classification Training Pipeline
Author: Saksham Gupta
GitHub: https://github.com/sakshamgupta04
Repository: https://github.com/sakshamgupta04/Food-Recogniton
Copyright (c) 2026 Saksham Gupta. All rights reserved.
=============================================================================
"""

import os
from ultralytics import YOLO

# Paths & Hyperparameters
DATASET_PATH = "dataset/food101"
MODEL_NAME = "yolov8n-cls.pt"   # Lightweight model
EPOCHS = 30                     # Number of training epochs
IMAGE_SIZE = 224                # Image resolution

def train_model():
    print("=" * 60)
    print("Starting YOLOv8 Food Classification Training (Saksham Gupta)...")
    print("=" * 60)
    model = YOLO(MODEL_NAME)
    
    # Train the model
    model.train(
        data=DATASET_PATH,
        epochs=EPOCHS,
        imgsz=IMAGE_SIZE
    )
    print("Training completed!")

    # Return path to best weights
    weights_path = "runs/classify/train/weights/best.pt"
    if os.path.exists(weights_path):
        print(f"Best model saved at: {weights_path}")
    else:
        print("Could not find best.pt. Please check training logs.")
    return weights_path

def test_model(weights_path, test_image):
    print(f"Testing model on: {test_image}")
    model = YOLO(weights_path)
    results = model.predict(test_image)
    print("Prediction Results:")
    print(results[0].probs)   # Shows top predictions

    top_class = results[0].names[results[0].probs.top1]
    print(f"Predicted Food: {top_class}")
    return top_class

if __name__ == "__main__":
    best_weights = train_model()

    # Test with a sample image
    test_image = "test_food.jpg"
    if os.path.exists(test_image):
        test_model(best_weights, test_image)
    else:
        print("Please place a test image named 'test_food.jpg' in this directory to test the model.")
