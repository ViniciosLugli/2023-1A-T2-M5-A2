from models.game import Game
from database.connection import session
import flask


def init_routes(app):
    @app.route('/game', methods=['GET'])
    def get_games():
        # Get the first game object from the database
        games = session.query(Game).all()

        # Return the game object as a JSON in a list
        return [game.to_json() for game in games]

    @app.route('/game/create', methods=['POST'])
    def create_game():
        # Get the JSON data from the request
        content = flask.request.json

        # Create a new game object
        game = Game(content['name'], content['platform'], content['price'], content['amount'])

        # Add the game object to the database
        session.add(game)
        session.commit()

        # Return the created game object as a JSON
        return game.to_json()

    @app.route('/game/delete/<id>', methods=['DELETE'])
    def delete_game(id):
        # Get the game object
        game = session.query(Game).filter(Game.id == id).first()

        # Delete the game object
        session.delete(game)
        session.commit()

        # Return the deleted game object as a JSON
        return game.to_json()
