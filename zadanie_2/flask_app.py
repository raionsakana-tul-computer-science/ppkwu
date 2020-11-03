from flask import Flask, abort
from json import dumps

INFO_MESSAGE: str = "Info: To get stats of message, use /*endpoint name*/*your message*"
flask_app = Flask(__name__)


def count_big_letters(text: str):
    return sum(1 for c in text if c.isupper())


def count_small_letters(text: str):
    return sum(1 for c in text if c.islower())


def count_numbers(text: str):
    return sum(1 for c in text if c.isnumeric())


def count_special_characters(text: str):
    number_of_letters = sum((count_big_letters(text), count_small_letters(text)))
    return len(text) - number_of_letters - count_numbers(text)


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


@flask_app.route('/numbers/<text>')
def numbers(text: str):
    if text is None:
        abort(415)

    return dumps({
        "numbers": count_numbers(text)
    })


@flask_app.route('/special-characters/<text>')
def special_characters(text: str):
    if text is None:
        abort(415)

    return dumps({
        "special-characters": count_special_characters(text)
    })


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
