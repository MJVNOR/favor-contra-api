import requests

review = {"texto": "Viva amlo"}
resp = requests.post(
    "https://favor-contra-api.herokuapp.com/clasification", json=review
)

print(resp.content)
