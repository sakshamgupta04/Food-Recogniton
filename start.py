"""
=============================================================================
Food Recognition & Recipe Finder - Quick Verification Script
Author: Saksham Gupta
GitHub: https://github.com/sakshamgupta04
Repository: https://github.com/sakshamgupta04/Food-Recogniton
Copyright (c) 2026 Saksham Gupta. All rights reserved.
=============================================================================
"""

from ultralytics import YOLO

print("=" * 60)
print("Food Recognition Environment Check - Saksham Gupta")
print("=" * 60)

model = YOLO('yolov8n.pt')
print("YOLOv8 initialized and loaded successfully!")
