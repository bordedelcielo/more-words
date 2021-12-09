import requests
import json

word = "panettone"
response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

# print(response.text)
# print(response.json()[0])
# print(response.json()[0]["word"])
# print(response.json()[0]["origin"])
# print(response.json()[0])
print(response.json()[0]["meanings"][0]["definitions"][0]["definition"])