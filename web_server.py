from flask import Flask, request, redirect, url_for, render_template
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def index():
    if False: # if not valid cookie
        # reroute to login endpoint
        return
    else:
        return render_template('index.html')

@app.route('/message', methods=['POST'])
def message_post():
    message_to_print = request.form['user_message']
    print(f"form: {message_to_print}")
    return "POST /message success"