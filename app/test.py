"""
=============================================================================
Food Recognition & Recipe Finder - Object Detection & Inference Test
Author: Saksham Gupta
GitHub: https://github.com/sakshamgupta04
Repository: https://github.com/sakshamgupta04/Food-Recogniton
Copyright (c) 2026 Saksham Gupta. All rights reserved.
=============================================================================
"""

from ultralytics import YOLO
from pathlib import Path
import cv2

print("Running YOLOv8 Food/Object Detection (Saksham Gupta)...")

# Load model (COCO classes, general objects)
model = YOLO("yolov8n.pt")

# Use a safe path
image_path = Path("app") / "Spicy-Penne-Pasta_-done.png"

# Run inference (set save=True to auto-save annotated image)
results = model(str(image_path))

res = results[0]            # first image result

# List detections
print("\nDetections:")
for box in res.boxes:
    cls_id = int(box.cls[0])
    name = res.names[cls_id]
    conf = float(box.conf[0])
    print(f" - {name}: {conf:.2f}")

# Save annotated image manually
annotated = res.plot()      # BGR image
cv2.imwrite("annotated.png", annotated)
print("\nAnnotated image saved to annotated.png")
