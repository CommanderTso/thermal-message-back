from app import app
from user import User
from flask import request, url_for, render_template, session


@app.route('/', methods=['GET'])
def index():
    if False:  # if not valid cookie
        # reroute to login endpoint
        return
    else:
        # print(app.load_user(1))
        return render_template('index.html')


@app.route('/message', methods=['POST'])
def message_post():
    message_to_print = request.form['user_message']
    print(f"form: {message_to_print}")
    return "Your message has been posted!"
