from flask import Flask, request, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def index():
    if False: # if not valid cookie
        # reroute to login endpoint
        return
    else:
        return redirect(url_for('message_post'))

@app.route('/message-post', methods=['POST', 'GET'])
def message_post():
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        return "success"
    elif request.method == 'GET':
        return "message posting page!"
    else:
        abort(405)  # Method Not Allowed
