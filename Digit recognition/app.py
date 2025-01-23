from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import pickle
import base64
from PIL import Image
import io

app = Flask(__name__)
with open('digit_recognition_cnn.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')
@app.route('/predict', methods=['POST'])
def predict():
    image_data = request.json['image']
    image_data = image_data.split(',')[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))

    image_array = np.array(image.convert('L'))
    image_array = image_array / 255.0
    image_array = image_array.reshape(1, 28, 28, 1)

    prediction = model.predict(image_array)[0]
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)