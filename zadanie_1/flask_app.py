from flask import Flask

flask_app = Flask(__name__)


@flask_app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
