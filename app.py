from database.db import initialize_db
from flask import Flask
from secrets import FLASK_APP_SECRET_KEY
from utils.JsonEncoder import MongoEngineJsonEncoder

app = Flask(__name__)
app.secret_key = FLASK_APP_SECRET_KEY
app.json_encode = MongoEngineJsonEncoder

initialize_db(app)

if __name__ == '__main__':
    app.run()
