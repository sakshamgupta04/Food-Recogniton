"""
=============================================================================
Food Recognition & Recipe Finder - Web Application
Author: Saksham Gupta
GitHub: https://github.com/sakshamgupta04
Repository: https://github.com/sakshamgupta04/Food-Recogniton
Copyright (c) 2026 Saksham Gupta. All rights reserved.
=============================================================================
"""

import os
from flask import Flask, render_template, request, url_for, redirect
from food_info import get_food_info
from food_classifier import predict_food

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'Templates')
STATIC_DIR = os.path.join(BASE_DIR, 'Static')
UPLOAD_FOLDER = os.path.join(STATIC_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR,
    static_url_path='/static'
)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16MB

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file and file.filename != '':
            safe_filename = os.path.basename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
            file.save(filepath)

            try:
                # Predict food using the classifier
                food_name, confidence, top_predictions = predict_food(filepath, top_k=5)
                info = get_food_info(food_name)

                # Web image URL
                image_url = url_for('static', filename=f'uploads/{safe_filename}')

                return render_template(
                    'result.html',
                    food=food_name,
                    confidence=confidence,
                    predictions=top_predictions,
                    info=info,
                    image=image_url
                )
            except Exception as e:
                return render_template(
                    'index.html',
                    error=f"Could not read the uploaded image ({str(e)}). Please upload a standard JPG, PNG, or WEBP image."
                )

    return render_template('index.html')

if __name__ == "__main__":
    print("=" * 60)
    print("Food Recognition Web App by Saksham Gupta")
    print("GitHub: https://github.com/sakshamgupta04")
    print("Starting server on http://127.0.0.1:5000 ...")
    print("=" * 60)
    app.run(host='127.0.0.1', port=5000, debug=False)
