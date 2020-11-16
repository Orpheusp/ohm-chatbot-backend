from mongoengine import connect
from pymongo import MongoClient
from typing import Optional
from secrets import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_CARDS_HOSTNAME, DATABASE_SESSIONS_HOSTNAME

_cards_db: Optional[MongoClient] = None
_sessions_db: Optional[MongoClient] = None


def initialize_dbs():
    global _cards_db
    global _sessions_db

    _cards_db = connect(
        db='Cards',
        alias='cards',
        username=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_CARDS_HOSTNAME
    )
    _sessions_db = connect(
        db='Sessions',
        alias='sessions',
        username=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_SESSIONS_HOSTNAME
    )


def fetch_cards_db():
    global _cards_db
    return _cards_db


def fetch_sessions_db():
    global _sessions_db
    return _sessions_db
