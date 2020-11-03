from flask import Flask
from json import dumps

INFO_MESSAGE: str = "Info: To get stats of message, use /*endpoint name*/*your message*"
flask_app = Flask(__name__)


@flask_app.route('/')
def main():
    return INFO_MESSAGE


@flask_app.route('/health')
def health():
    return ""


@flask_app.route('/big-letters/<text>')
def big_letters(text: str):
    return dumps({
        "big-letters": sum(1 for c in text if c.isupper())
    })


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
