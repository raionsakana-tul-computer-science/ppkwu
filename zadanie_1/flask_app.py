from flask import Flask

flask_app = Flask(__name__)


@flask_app.route('/rev/<text>')
def hello(text: str):
    return text


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
