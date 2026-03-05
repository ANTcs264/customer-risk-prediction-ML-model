from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = np.array([
        float(data["age"]),
        float(data["income"]),
        float(data["children"]),
        float(data["spend"])
    ]).reshape(1,-1)

    features = scaler.transform(features)

    prediction = model.predict(features)

    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)