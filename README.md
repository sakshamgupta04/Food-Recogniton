# Food Recognition & Recipe Finder 🍲

An intelligent AI-powered food recognition and recipe discovery application. The system accurately classifies food items from uploaded images using deep vision models, displaying the dish name, classification confidence, culinary origin, key ingredients, and preparation recipes.

---

## 🌟 Features

- **Accurate Food Classification**: Utilizes a deep vision model fine-tuned on the Food-101 benchmark dataset (101 food categories).
- **Culinary Insights & Recipes**: Displays dish origin, typical ingredients, and cooking instructions.
- **Modern Responsive Web Interface**: Clean, accessible drag-and-drop web UI built with Flask.
- **YOLOv8 Support**: Includes scripts for object detection and training custom YOLOv8 classification models.
- **Local / Offline Capable**: Automatically loads cached weights if available locally, with fallback to Hugging Face Hub.

---

## 📂 Project Structure

```text
Food_Recognition/
│
├── app/
│   ├── Static/             # Static web assets & upload cache
│   ├── Templates/
│   │   ├── index.html      # Image upload interface
│   │   └── result.html     # Detection result & recipe view
│   ├── food_classifier.py  # Image classification pipeline
│   ├── food_info.py        # Culinary knowledgebase (origin, ingredients, recipes)
│   ├── main.py             # Flask web application entrypoint
│   └── test.py             # YOLOv8 object detection test script
│
├── prepare_food101.py      # Dataset split preparation script
├── train_food101.py        # YOLOv8 training script
├── train_food101_gpu.py    # GPU-accelerated YOLOv8 training script
├── start.py                # Quick verification script
├── requirements.txt        # Python package dependencies
└── README.md
```

---

## 🚀 Quickstart

### 1. Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/sakshamgupta04/Food-Recogniton.git
cd Food-Recogniton
pip install -r requirements.txt
```

### 2. Run the Web Application

Start the Flask server:

```bash
python app/main.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:5000
```

Upload or drag and drop any food image to identify the dish and view its recipe!

### 3. Run Object Detection Test (YOLOv8)

```bash
python app/test.py
```

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Deep Learning**: PyTorch, Hugging Face Transformers, Torchvision, Ultralytics YOLOv8
- **Computer Vision**: OpenCV, Pillow
- **Frontend**: HTML5, Modern CSS

