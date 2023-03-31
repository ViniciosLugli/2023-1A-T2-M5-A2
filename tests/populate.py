import requests

url = "http://localhost:5000/game/create"
method = "POST"

mapping = [
    {
        "name": "DEAD SPACE REMAKE",
        "platform": "PS5",
        "price": 350.00,
        "amount": 10
    },
    {
        "name": "FORSPOKEN",
        "platform": "PC",
        "price": 299.00,
        "amount": 8
    },
    {
        "name": "DEAD ISLAND 2",
        "platform": "PS5",
        "price": 350.00,
        "amount": 10
    },
    {
        "name": "HOGWARTS LEGACY",
        "platform": "PC",
        "price": 219.00,
        "amount": 7
    }
]

for game in mapping:
    response = requests.request(method, url, json=game)
    print(f'Game {game["name"]} created in api')
