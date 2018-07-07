from flask import Flask
app = Flask(__name__)

@app.route('/message', methods=['GET'])
def message_get():
    return 'message -> get\n'

@app.route('/message', methods=['POST'])
def message_post():
    return 'message -> post\n'