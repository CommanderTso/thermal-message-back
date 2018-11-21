from flask import Flask, request, redirect, url_for, render_template, session
import flask_login
import os
from user import User

app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET']
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@app.route('/', methods=['GET'])
def index():
    if False: # if not valid cookie
        # reroute to login endpoint
        return
    else:
        print(load_user(1))
        return render_template('index.html')

@app.route('/message', methods=['POST'])
def message_post():
    message_to_print = request.form['user_message']
    print(f"form: {message_to_print}")
    return "Your message has been posted!"


# -----------------

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)