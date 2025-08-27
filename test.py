import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'Age': 52,
    'Sex': 1,
    'ChestPainType': 2,
    'RestingBP': 130,
    'Cholesterol': 250,
    'FastingBS': 0,
    'RestingECG': 1,
    'MaxHR': 150,
    'ExerciseAngina': 0,
    'Oldpeak': 1.2,
    'ST_Slope': 2
}

response = requests.post(url, json=data)
print("Raw response:", response.text)