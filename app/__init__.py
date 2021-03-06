import os
# from dotenv import load_dotenv, dotenv_values
import flask_login
from flask import Flask
from app.user import User
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

print(f'APP.CONFIG:  {app.config}')

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_get"
login_manager.login_message = "Please log in to access this page."

@login_manager.user_loader
def load_user(user_id):
    return User(None, user_id)

from app import routes

@app.context_processor
def inject_environment():
    return dict(app_environment=app.config['ENV'])
