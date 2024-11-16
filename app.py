from flask import Flask, request, jsonify
import cv2
import numpy as np
import tensorflow as tf  # Assuming TensorFlow is used for your model

# Load the pre-trained model
model = tf.keras.models.load_model("klasifikasi_sampah.h5")

def preprocess_image(image):
    # Convert to RGB and resize
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (150, 150))
    # Remove normalization here, since it will be done in the model
    # Expand dimensions for model input
    image = np.expand_dims(image, axis=0)
    return image


def predict(image):
  # Preprocess the image
  preprocessed_image = preprocess_image(image)
  # Get prediction probability
  prediction = model.predict(preprocessed_image)[0][0]
  # Classify based on threshold
  if prediction > 0.5:
    classification = "anorganik"
  else:
    classification = "organik"
  return classification

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def upload_and_predict():
  # Get the uploaded image file
  image_file = request.files.get("image")
  if image_file is None:
    return jsonify({"error": "No image uploaded"}), 400

  # Read the image from the file
  image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

  # Make prediction
  classification = predict(image)

  # Return JSON response
  return jsonify({"classification": classification})

if __name__ == "__main__":
  app.run(debug=True)