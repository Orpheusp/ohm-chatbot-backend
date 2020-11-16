from flask_mongoengine import MongoEngine
from pymongo import MongoClient
from secrets import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_CARDS_HOSTNAME, DATABASE_SESSIONS_HOSTNAME
from flask_session import Session
from secrets import FLASK_APP_SECRET_KEY

_db = MongoEngine()
_sessions = Session()


def initialize_db(app):
    global _db

    app.config['MONGODB_SETTINGS'] = {
        'db': 'Cards',
        'username': DATABASE_USERNAME,
        'password': DATABASE_PASSWORD,
        'host': DATABASE_CARDS_HOSTNAME
    }

    _db.init_app(app)


def initialize_sessions(app):
    _sessions_db = MongoClient(
        DATABASE_SESSIONS_HOSTNAME,
        username=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        authSource='admin',
        authMechanism='SCRAM-SHA-1'
    )

    app.secret_key = FLASK_APP_SECRET_KEY
    app.config['SECRET_KEY'] = FLASK_APP_SECRET_KEY
    app.config['SESSION_TYPE'] = 'mongodb'
    app.config['SESSION_MONGODB'] = _sessions_db
    app.config['SESSION_MONGODB_DB'] = 'Sessions'
    app.config['SESSION_MONGODB_COLLECT'] = 'sessions'
    _sessions.init_app(app)


def fetch_db():
    global _db
    return _db
