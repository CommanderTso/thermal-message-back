from flask import Flask, request, render_template
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message_post():
    message_to_print = request.form['user_message']
    print(f"form: {message_to_print}")
    return "POST /message success"
