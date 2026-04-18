from flask import Flask, render_template, request
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model("fashion_model.h5")

labels = [
    "T-shirt", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        file = request.files['image']

        if file:
            img = Image.open(file)

            # Preprocess
            img = img.convert('L')              # grayscale
            img = img.resize((28, 28))          # resize
            img = np.array(img) / 255.0         # normalize
            img = img.reshape(1, 28, 28, 1)     # reshape

            pred = model.predict(img)
            prediction = labels[np.argmax(pred)]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)