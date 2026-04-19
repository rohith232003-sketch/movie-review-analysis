import joblib
import numpy as np
from preprocess import preprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

model = joblib.load('model.joblib')
vectorizer = joblib.load('tf_idf.joblib')

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Sentiment Analysis API is running!',
        'endpoint': {
            'health' : 'GET health',
            'predict' : 'POST /predict'
        }
    })
    
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        if not data or 'reviews' not in data:
            return jsonify({"error": "Invalid input"}), 400

        reviews = data['reviews']

        process_review = preprocess(reviews)
        process_review = vectorizer.transform([process_review])

        prediction = model.predict(process_review)

        return jsonify({"prediction": str(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)