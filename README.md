# 👕 AI Fashion Image Classifier

An end-to-end AI web application that classifies clothing items using a deep learning model. Users can upload an image, and the system predicts the clothing category in real time.



## 🚀 Features

* Upload image and get prediction instantly
* Image preprocessing (grayscale, resize, normalization)
* Deep Learning model (CNN) for classification
* Simple and clean web interface
* Flask-based backend integration



## 🧠 How It Works

1. User uploads an image through the browser
2. The image is sent to the Flask server
3. Image is preprocessed:

   * Resized to 28x28
   * Converted to grayscale
   * Normalized
4. Processed image is passed to the trained CNN model
5. Model predicts probabilities for each class
6. Final prediction is sent back and displayed



## 🏗️ System Architecture

![Architecture Diagram](./assets/architecture.png)



## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **Machine Learning:** TensorFlow / Keras
* **Libraries:** NumPy, Pillow



## 📁 Project Structure


Fashion_MNIST/
│
├── app.py
├── fashion_model.h5
├── requirements.txt
├── templates/
│   └── index.html
└── assets/
    └── architecture.png




## ⚙️ Installation & Setup

### 1. Clone the repository


git clone https://github.com/vedddev/Fashion_MNIST.git
cd Fashion_MNIST


### 2. Install dependencies


pip install -r requirements.txt


### 3. Run the application


python app.py


### 4. Open in browser


http://127.0.0.1:5000




## 📊 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Dataset: Fashion MNIST
* Input Shape: (28, 28, 1)
* Output: 10 clothing categories



## ⚠️ Limitations

* Model trained on grayscale dataset (28x28)
* Real-world images may reduce accuracy
* Works best with simple clothing images



## 🔮 Future Improvements

* Improve accuracy with larger datasets
* Add confidence scores
* Enhance UI/UX
* Deploy online (cloud hosting)
* Add drag-and-drop upload



## 🙌 Acknowledgements

* TensorFlow / Keras
* Fashion MNIST dataset



## 📬 Contact

Feel free to connect if you want to collaborate or discuss ideas!


