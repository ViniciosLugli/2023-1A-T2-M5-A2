import requests

url = "http://localhost:5000/game"
method = "GET"

games = requests.request(method, url).json()

for game in games:
    print(games)
