from database.db import initialize_dbs
from flask import Flask
from flask_restful import Api
from secrets import FLASK_APP_SECRET_KEY
from utils.JsonEncoder import MongoEngineJsonEncoder
from resources.ChatCards import ChatCards
from resources.TutorialCards import TutorialCards
from resources.InformationCards import InformationCards

app = Flask(__name__)
app.secret_key = FLASK_APP_SECRET_KEY

initialize_dbs()
app.json_encoder = MongoEngineJsonEncoder
api = Api(app)

# Resources for testing purposes
api.add_resource(ChatCards, '/chat-cards', '/chat-cards/<string:card_id>')
api.add_resource(
    TutorialCards, '/tutorial-cards', '/tutorial-cards/<string:card_id>')
api.add_resource(
    InformationCards,
    '/information-cards',
    '/information-cards/<string:card_id>'
)

if __name__ == '__main__':
    app.run()
