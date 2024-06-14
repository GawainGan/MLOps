import requests

ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

url = 'http://localhost:9696/predict'  # Corrected URL
response = requests.post(url, json=ride)

try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("Response content is not valid JSON")