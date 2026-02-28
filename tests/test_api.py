import requests

response = requests.get("http://localhost:8000/pose/latest")

print("API Response:", response.json())