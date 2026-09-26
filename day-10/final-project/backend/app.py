from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained model and scaler
model = joblib.load('hygiene_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    # Returning HTML with explicit black text and white background
    return '''
        <body style="background-color: white; color: black; font-family: sans-serif; padding: 2rem;">
            <h1>Smart Hygiene API is running!</h1>
            <p><strong>Status:</strong> Active</p>
            <p>To use the model, send a POST request to <code>/api/predict</code></p>
        </body>
    '''

@app.route('/api/predict', methods=['POST'])
def predict_risk():
    try:
        data = request.json
        # Extract features in the exact order the model expects
        features = np.array([[
            data['cleanliness_score'],
            data['odor_score'],
            data['waste_level'],
            data['complaints'],
            data['footfall'],
            data['hours_since_cleaning']
        ]])
        
        # Scale and predict
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]
        
        return jsonify({
            'success': True,
            'prediction': prediction,
            'input_data': data
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    print("Starting Smart Hygiene Prediction API on port 5000...")
    app.run(debug=True, port=5000)