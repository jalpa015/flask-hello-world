from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name
