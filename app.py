from flask import Flask, request, render_template
import numpy as np
import cv2
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model('../models/cnn_model.h5')

def preprocess(img):
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        file = request.files['file']
        img = cv2.imdecode(
            np.frombuffer(file.read(), np.uint8),
            cv2.IMREAD_GRAYSCALE
        )

        img = preprocess(img)
        pred = model.predict(img)
        prediction = np.argmax(pred)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)