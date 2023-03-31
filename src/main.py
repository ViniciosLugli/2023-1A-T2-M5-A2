from routes import game
from flask import Flask

app = Flask(__name__)

game.init_routes(app)
