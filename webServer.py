from flask import Flask, request
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/send-message', methods=['GET'])
def message_get():
    return 'message -> get\n'

@app.route('/message', methods=['POST'])
def message_post():
    post_data = request.get_json()
    print(post_data)
    return "success"