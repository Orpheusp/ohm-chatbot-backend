from flask_mongoengine import MongoEngine
from secrets import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOSTNAME

db = MongoEngine()


def initialize_db(app):
    app.config['MONGODB_SETTINGS'] = {
        'db': 'Cards',
        'host': DATABASE_HOSTNAME,
        'username': DATABASE_USERNAME,
        'password': DATABASE_PASSWORD,
    }
    db.init_app(app)

def fetch_engine():
    return db