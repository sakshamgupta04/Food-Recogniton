<div align="center">

# 🍲 Food Recognition & Recipe Finder

**An intelligent end-to-end Computer Vision & Deep Learning web platform for automated food recognition, nutritional analysis, and recipe discovery.**

[![Author](https://img.shields.io/badge/Author-Saksham%20Gupta-orange.svg?style=for-the-badge&logo=github)](https://github.com/sakshamgupta04)
[![Repository](https://img.shields.io/badge/GitHub-Food--Recognition-blue.svg?style=for-the-badge&logo=github)](https://github.com/sakshamgupta04/Food-Recogniton)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch)](https://pytorch.org/)
[![YOLOv8](https://img.shields.io/badge/Ultralytics-YOLOv8-00FFFF?style=for-the-badge&logo=yolo)](https://ultralytics.com/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)

---

Developed and maintained with ❤️ by **[Saksham Gupta](https://github.com/sakshamgupta04)**

</div>

## 📌 Overview

**Food Recognition & Recipe Finder** is an AI-powered culinary intelligence platform developed by **Saksham Gupta**. By leveraging state-of-the-art Computer Vision architectures (fine-tuned Vision Transformers and Ultralytics YOLOv8), the system accurately classifies food items from uploaded photographs and instantly pairs them with:
- **Culinary Origin & Heritage**
- **Detailed Nutritional Breakdown** (Calories, Protein, Carbohydrates, Fat)
- **Ranked Top-5 Confidence Predictions** with dynamic probability distributions
- **Complete Ingredients & Step-by-Step Cooking Recipes**

Whether you are identifying a foreign delicacy, tracking macro-nutrients, or looking for recipe inspiration from a photo, this project delivers real-time, high-accuracy inference through a sleek, responsive interface.

---

## ✨ Key Features

- **🧠 Deep Vision Architecture**: Powered by deep neural networks trained on the Food-101 benchmark dataset (101 food categories, 101,000 images).
- **📊 Top-K Probabilities**: Interactive visual distribution bars illustrating model confidence across the top-5 candidate food classes.
- **🥗 Nutrition & Macro Estimates**: Provides per-serving calorie count, protein, carbohydrates, and fats.
- **🍳 Culinary Knowledge Base**: Built-in culinary database detailing ingredients, preparation recipes, and cultural origins.
- **🎨 Modern Drag & Drop UI**: Intuitive, responsive web interface built with Flask and modern CSS design system.
- **⚡ YOLOv8 Model Training Pipeline**: Dedicated scripts for both CPU and GPU-accelerated training (`train_food101.py`, `train_food101_gpu.py`).
- **🛡️ Robust Error Handling**: Clean validation for file extensions (JPG, PNG, WEBP), file size caps, and error messaging.

---

## 📂 Repository Structure

```text
Food_Recognition/
│
├── app/
│   ├── Static/                 # Web assets & cached uploads
│   │   └── uploads/            # Temporary image cache
│   ├── Templates/
│   │   ├── index.html          # Drag-and-drop image upload portal
│   │   └── result.html         # Rich analysis, nutrition & recipe interface
│   ├── models/
│   │   └── food_classifier/    # Local model weights & tokenizer configurations
│   ├── food_classifier.py      # Core image classification inference engine
│   ├── food_info.py            # Culinary knowledge base & nutritional mapping
│   ├── main.py                 # Flask web server application
│   └── test.py                 # YOLOv8 object detection test script
│
├── dataset/                    # Dataset directory for Food-101 splits (optional)
├── prepare_food101.py          # Train/val split generator for Food-101
├── train_food101.py            # Standard YOLOv8 training routine
├── train_food101_gpu.py        # High-performance GPU-aware YOLOv8 trainer
├── start.py                    # Environment & dependency check
├── requirements.txt            # Project dependencies
├── LICENSE                     # MIT License
└── README.md                   # Project documentation
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository

```bash
git clone https://github.com/sakshamgupta04/Food-Recogniton.git
cd Food-Recogniton
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Web Application

```bash
python app/main.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

Upload any image of a dish (e.g., Pizza, Sushi, Pasta, Curry, Burger) to see real-time classification, nutrition metrics, and recipes!

---

## 🎯 Model Training & Testing

### Test YOLOv8 Inference

Run the standalone detection script on sample images:

```bash
python app/test.py
```

### Prepare Food-101 Dataset

If fine-tuning on the full Food-101 benchmark:

```bash
python prepare_food101.py
```

### Train Classification Model (GPU-Accelerated)

```bash
python train_food101_gpu.py --data dataset/food101 --device 0 --epochs 30 --batch 32
```

---

## 🛠️ Tech Stack & Libraries

| Domain | Technologies Used |
|---|---|
| **Deep Learning & CV** | PyTorch, Hugging Face Transformers, Torchvision, Ultralytics YOLOv8, OpenCV |
| **Backend & Web API** | Python 3, Flask, Werkzeug |
| **Data Processing** | Pillow (PIL), NumPy |
| **Frontend** | HTML5, CSS3, Plus Jakarta Sans typography |
| **Version Control** | Git, GitHub |

---

## 👤 Author

**Saksham Gupta**
- **GitHub**: [@sakshamgupta04](https://github.com/sakshamgupta04)
- **Repository**: [https://github.com/sakshamgupta04/Food-Recogniton](https://github.com/sakshamgupta04/Food-Recogniton)
- **Email**: sakshamsgupta04@gmail.com

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

Copyright © 2026 **Saksham Gupta**. All rights reserved.
