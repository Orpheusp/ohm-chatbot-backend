from flask import Flask
from database.db import initialize_db
from secrets import FLASK_APP_SECRET_KEY

app = Flask(__name__)
app.secret_key = FLASK_APP_SECRET_KEY

initialize_db(app)

if __name__ == '__main__':
    app.run()
