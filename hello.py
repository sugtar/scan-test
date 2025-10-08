from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    user = request.args.get('user')
    return 'Hello, World!' + user

@app.route('/foo')
def foo():
    return 'foo'

@app.route('/bar')
def bar():
    return 'bar'
