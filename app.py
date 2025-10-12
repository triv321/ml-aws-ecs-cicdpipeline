import joblib
from flask import Flask, request, jsonify

# Create the Flask app
app = Flask(__name__)

# --- Load the Model Artifacts ---
# Load the trained model and the vectorizer from disk
# These are loaded only once when the app starts, for efficiency
print("Loading model artifacts...")
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
print("Model artifacts loaded successfully.")

# --- Define the Prediction Endpoint ---
@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives a JSON payload with a 'text' key,
    and returns a sentiment prediction.
    """
    # Get the JSON data from the request
    data = request.get_json()

    # Check if the 'text' key exists
    if 'text' not in data:
        return jsonify({'error': 'Missing "text" key in request body'}), 400

    review_text = data['text']

    # Vectorize the input text using the loaded vectorizer
    text_vec = vectorizer.transform([review_text])

    # Make a prediction using the loaded model
    prediction = model.predict(text_vec)

    # Return the prediction as a JSON response
    # The [0] is to get the single prediction from the numpy array
    return jsonify({'sentiment': prediction[0]})

# --- Run the App ---
if __name__ == '__main__':
    # The host='0.0.0.0' makes the app accessible from your network
    app.run(host='0.0.0.0', port=5000, debug=True)