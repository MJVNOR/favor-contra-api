import requests

review = {"texto": "Viva amlo"}
resp = requests.post("http://localhost:8000/clasification", json=review)

print(resp.content)
