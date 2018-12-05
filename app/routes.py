import sys
for p in sys.path:
    print(p)

from app import app
from app.user import User
from flask import request, url_for, render_template, session, redirect, flash
from app.forms import SubmitMessageForm, LoginForm
from app.helpers import parse_login_error


@app.route('/', methods=['GET'])
@app.route('/message', methods=['GET'])
def send_message():
    if False:  # if not valid cookie
        # reroute to login endpoint
        return
    else:
        # print(app.load_user(1))
        form = SubmitMessageForm()
        return render_template('send-message.html', form=form)


@app.route('/message', methods=['POST'])
def message_post():
    form = SubmitMessageForm()
    if form.validate_on_submit():
        message_to_print = form.message.data
        print(f"form: {message_to_print}")
        return render_template("message-sent.html")
    else:
        return "We had an issue!"

@app.route('/login', methods=['GET'])
def login_get():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/login', methods=['POST'])
def login_post():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Login POST - username: {form.username.data}")
        print(f"Login POST - password: {form.password.data}")
        return redirect(url_for('login_get'))
    else:
        flash(parse_login_error(form.errors))
        return redirect(url_for('login_get'))

