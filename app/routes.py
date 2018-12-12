from app import app
from app.user import User
from flask import request, url_for, render_template, session, redirect, flash
from app.forms import SubmitMessageForm, LoginForm
from app.helpers import parse_login_error
from flask_login import LoginManager, login_required, login_user, logout_user

login_manager = LoginManager()

@app.route('/', methods=['GET'])
@app.route('/message', methods=['GET'])
@login_required
def message_get():
    if False:  # if not valid cookie
        # reroute to login endpoint
        return url_for(login_get)
    else:
        form = SubmitMessageForm()
        return render_template('send-message.html', form=form)


@app.route('/message', methods=['POST'])
@login_required
def message_post():
    form = SubmitMessageForm()
    if form.validate_on_submit():
        message_to_print = form.message.data
        print(f"Message to print from form: {message_to_print}")
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
        user = User(form.username.data)
        username = form.username.data
        password = form.password.data

        if user is None or user.check_password(password) == False:
            flash('Invalid username or password')
            return redirect(url_for('login_get'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('message_get')
        return redirect(next_page)
    else:
        flash(parse_login_error(form.errors))
        return redirect(url_for('login_get'))

@app.route("/logout")
@login_required
def logout_get():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login_get'))
