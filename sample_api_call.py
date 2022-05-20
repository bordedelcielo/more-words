import requests
import json

# free dictionary api
# https://dictionaryapi.dev/
# https://github.com/meetDeveloper/freeDictionaryAPI

word = "love"
# word = "panettone"
response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

print(response.json())
# print(response.json()[0]["meanings"][0]["definitions"][0]["definition"])

# for index, item in enumerate(response.json()):
#     print(f'index: {index}. item: {item}.')

# Lingua Robot api