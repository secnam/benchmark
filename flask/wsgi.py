from flask import Flask
application = Flask(__name__)

@application.route('/hello')
def hello_world():
    return 'Hello, World!'
