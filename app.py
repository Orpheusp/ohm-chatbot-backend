from database.db import initialize_db
from flask import Flask
from flask_restful import Api
from secrets import FLASK_APP_SECRET_KEY
from utils.JsonEncoder import MongoEngineJsonEncoder

app = Flask(__name__)
app.secret_key = FLASK_APP_SECRET_KEY

initialize_db(app)
app.json_encoder = MongoEngineJsonEncoder
api = Api(app)

if __name__ == '__main__':
    app.run()
