from flask import Flask, abort
from json import dumps

INFO_MESSAGE: str = "Info: To get stats of message, use /*endpoint name*/*your message*"
flask_app = Flask(__name__)


def count_big_letters(text: str):
    return sum(1 for c in text if c.isupper())


def count_small_letters(text: str):
    return sum(1 for c in text if c.islower())


@flask_app.route('/')
def main():
    return INFO_MESSAGE


@flask_app.route('/health')
def health():
    return ""


@flask_app.route('/big-letters/<text>')
def big_letters(text: str):
    if text is None:
        abort(415)

    return dumps({
        "big-letters": count_big_letters(text)
    })


@flask_app.route('/small-letters/<text>')
def small_letters(text: str):
    if text is None:
        abort(415)

    return dumps({
        "small-letters": count_small_letters(text)
    })


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
