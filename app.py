import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

print("Loading model artifacts...")
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
print("Model artifacts loaded successfully.")

@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives a JSON payload with a 'text' key,
    and returns a sentiment prediction.
    """
    data = request.get_json()

    if 'text' not in data:
        return jsonify({'error': 'Missing "text" key in request body'}), 400

    review_text = data['text']

    text_vec = vectorizer.transform([review_text])

    prediction = model.predict(text_vec)

    return jsonify({'sentiment': prediction[0]})


if __name__ == '__main__':
    # The host='0.0.0.0' makes the app accessible from your network

    app.run(host='0.0.0.0', port=5000, debug=True)
