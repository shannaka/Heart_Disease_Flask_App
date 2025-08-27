from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json

# Load your trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

# Load the expected column names from training
with open('model_columns.json', 'r') as f:
    expected_cols = json.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

        # Convert incoming data to DataFrame
        input_df = pd.DataFrame([data])

        # One-hot encode the input
        input_encoded = pd.get_dummies(input_df)

        # Add missing columns
        for col in expected_cols:
            if col not in input_encoded:
                input_encoded[col] = 0

        # Reorder columns to match training
        input_encoded = input_encoded[expected_cols]

        # Make prediction
        prediction = model.predict(input_encoded)[0]
        return jsonify({'HeartDiseasePrediction': int(prediction)})

    except Exception as e:
        print("Error during prediction:", e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
