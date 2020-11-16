from mongoengine import connect
from pymongo import MongoClient
from typing import Optional
from secrets import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOSTNAME
from flask_session import Session
from secrets import FLASK_APP_SECRET_KEY

_cards_db: Optional[MongoClient] = None
_sessions_db: Optional[MongoClient] = None
_sessions: Optional[Session] = None


def initialize_db():
    global _cards_db

    _cards_db = connect(
        db='Cards',
        alias='cards',
        username=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOSTNAME
    )


def initialize_sessions(app):
    global _sessions_db

    _sessions_db = connect(
        db='Sessions',
        alias='sessions',
        username=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOSTNAME
    )

    app.config['SECRET_KEY'] = FLASK_APP_SECRET_KEY
    app.config['SESSION_TYPE'] = 'mongodb'
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_MONGODB'] = _sessions_db
    app.config['SESSION_MONGODB_DB'] = 'Sessions'
    app.config['SESSION_MONGODB_COLLECT'] = 'sessions'
    _sessions = Session(app)


def fetch_cards_db():
    global _cards_db
    return _cards_db


def fetch_sessions_db():
    global _sessions_db
    return _sessions_db
