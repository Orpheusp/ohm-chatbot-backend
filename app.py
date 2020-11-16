from database.db import initialize_db, initialize_sessions
from flask import Flask, session
from flask_restful import Api
from utils.JsonEncoder import MongoEngineJsonEncoder
from resources.ChatCards import ChatCards
from resources.TutorialCards import TutorialCards
from resources.InformationCards import InformationCards
from resources.Chats import Chats
from flask_cors import CORS
from datetime import timedelta


app = Flask(__name__)

initialize_db(app)
initialize_sessions(app)
app.config.update(
    PERMANENT_SESSION_LIFETIME=timedelta(hours=1),
)
app.json_encoder = MongoEngineJsonEncoder

cors_resources_config = {
    r'/chats/*': {
        'origins': 'http://localhost:8010',
        'methods': ['GET', 'POST'],
        'supports_credentials': True
    }
}
CORS(app, resources=cors_resources_config, supports_credentials=True)
api = Api(app)

api.add_resource(Chats, '/chats')

# Resources for testing purposes
api.add_resource(ChatCards, '/chat-cards', '/chat-cards/<string:card_id>')
api.add_resource(
    TutorialCards, '/tutorial-cards', '/tutorial-cards/<string:card_id>')
api.add_resource(
    InformationCards,
    '/information-cards',
    '/information-cards/<string:card_id>'
)

@app.before_request
def make_session_permanent():
    session.modified = True
    session.permanent = True

if __name__ == '__main__':
    app.run()
