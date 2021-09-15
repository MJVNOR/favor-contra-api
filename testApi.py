import requests
import sys

tweet = " ".join(sys.argv[1:])
print(tweet)
review = {"texto": tweet}
resp = requests.post(
    "https://favor-contra-api.herokuapp.com/clasification", json=review
)

print(resp.content)
