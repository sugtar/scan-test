from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    user = request.args.get('user')
    return 'Hello, World!' + user
