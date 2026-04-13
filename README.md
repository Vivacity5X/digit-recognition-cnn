# 🧠 Handwritten Digit Recognition using CNN

## 📌 Overview

This project implements a **Convolutional Neural Network (CNN)** to recognize handwritten digits (0–9) from images.
The model is trained on the **MNIST** dataset and deployed using a **Flask web application** for real-time predictions.

---

## 🎯 Features

* 📷 Upload handwritten digit image
* 🧠 CNN-based digit classification
* ⚡ Real-time prediction using Flask
* 🔄 Image preprocessing (resize, normalize, invert, threshold)
* 🎨 Simple and clean UI

---

## 🏗️ Tech Stack

* Python 🐍
* TensorFlow / Keras
* OpenCV
* Flask
* HTML & CSS

---

## 🧠 Model Architecture

The CNN model consists of:

* Convolution Layers (feature extraction)
* ReLU Activation (non-linearity)
* MaxPooling Layers (downsampling)
* Flatten Layer
* Dense Layers (classification)
* Dropout (prevent overfitting)
* Softmax Output (10 classes: digits 0–9)

---

## 📂 Project Structure

```
digit-recognition-cnn/
│
├── models/
│   └── cnn_model.h5
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── train.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/digit-recognition-cnn.git
cd digit-recognition-cnn
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Train the Model

```bash
python train.py
```

This will:

* Load MNIST dataset
* Train CNN model
* Save model in `models/cnn_model.h5`

---

## ▶️ Run the Web App

```bash
cd app
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🔄 Image Preprocessing

To match MNIST format, we apply:

* Resizing to 28×28
* Grayscale conversion
* Color inversion (black → white)
* Thresholding (noise removal)
* Normalization (0–1 scaling)

---

## 📊 Results

* Achieved high accuracy on MNIST dataset
* Correct predictions for most handwritten inputs after preprocessing

---


---

## 🚀 Future Improvements

* ✏️ Draw-on-screen digit input (canvas)
* 📊 Confidence score visualization
* 🌐 Deploy on cloud (Render / AWS)
* 📱 Mobile-friendly UI

---

## 👨‍💻 Team Contribution

* Model Development
* Data Preprocessing
* Backend (Flask API)
* Frontend & UI

---

## ⭐ Acknowledgements

* MNIST Dataset
* TensorFlow & Keras

---

## 📌 License

This project is for educational and hackathon purposes.
