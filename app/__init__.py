import flask_login
import os
from flask import Flask


app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET']

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

from app import routes
