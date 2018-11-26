import sys

for p in sys.path:
    print(p)
    
from app import app
from app.user import User
from flask import request, url_for, render_template, session
from app.forms import SubmitMessageForm


@app.route('/', methods=['GET'])
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
