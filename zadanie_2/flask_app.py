from flask import Flask, abort
from json import dumps

INFO_MESSAGE: str = "Info: To get stats of message, use /*endpoint name*/*your message*"
flask_app = Flask(__name__)


def count_big_letters(text: str):
    index, mark = 0, False
    temp_letters = [0]

    for c in text:
        if c.isupper():
            temp_letters[index] = temp_letters[index] + 1
            mark = True
        else:
            mark = False

        if not mark:
            index += 1
            temp_letters.append(0)

    letters = [c for c in temp_letters if c != 0]

    return {
        "count": sum(letters),
        "number-of-strings": len(letters),
        "number-of-characters-in-string": letters
    }


def count_small_letters(text: str):
    index, mark = 0, False
    temp_letters = [0]

    for c in text:
        if c.islower():
            temp_letters[index] = temp_letters[index] + 1
            mark = True
        else:
            mark = False

        if not mark:
            index += 1
            temp_letters.append(0)

    letters = [c for c in temp_letters if c != 0]

    return {
        "count": sum(letters),
        "number-of-strings": len(letters),
        "number-of-characters-in-string": letters
    }


def count_numbers(text: str):
    index, mark = 0, False
    temp_letters = [0]

    for c in text:
        if c.isnumeric():
            temp_letters[index] = temp_letters[index] + 1
            mark = True
        else:
            mark = False

        if not mark:
            index += 1
            temp_letters.append(0)

    letters = [c for c in temp_letters if c != 0]

    return {
        "count": sum(letters),
        "number-of-strings": len(letters),
        "number-of-characters-in-string": letters
    }


def count_special_characters(text: str):
    index, mark = 0, False
    temp_letters = [0]

    for c in text:
        if not c.isnumeric() and not c.isupper() and not c.islower():
            temp_letters[index] = temp_letters[index] + 1
            mark = True
        else:
            mark = False

        if not mark:
            index += 1
            temp_letters.append(0)

    letters = [c for c in temp_letters if c != 0]

    return {
        "count": sum(letters),
        "number-of-strings": len(letters),
        "number-of-characters-in-string": letters
    }


@flask_app.route('/')
def main():
    return INFO_MESSAGE


@flask_app.route('/<name>')
@flask_app.route('/<name>/')
def error(name: str):
    abort(415)


@flask_app.route('/health')
def health():
    return ""


@flask_app.route('/big-letters/<text>')
def big_letters(text: str):
    if text is None:
        abort(415)

    return dumps(count_big_letters(text))


@flask_app.route('/small-letters/<text>')
def small_letters(text: str):
    if text is None:
        abort(415)

    return dumps(count_small_letters(text))


@flask_app.route('/numbers/<text>')
def numbers(text: str):
    if text is None:
        abort(415)

    return dumps(count_numbers(text))


@flask_app.route('/special-characters/<text>')
def special_characters(text: str):
    if text is None:
        abort(415)

    return dumps(count_special_characters(text))


@flask_app.route('/all-characters/<text>')
def all_characters(text: str):
    if text is None:
        abort(415)

    return dumps({
      "big-letters": {
        "count": 0,
        "number-of-strings": 0,
        "number-of-characters-in-string": [0]
      },
      "small-letters": {
        "count": 0,
        "number-of-strings": 0,
        "number-of-characters-in-string": [0]
      },
      "numbers": {
        "count": 0,
        "number-of-strings": 0,
        "number-of-characters-in-string": [0]
      },
      "special-characters": {
        "count": 0,
        "number-of-strings": 0,
        "number-of-characters-in-string": [0]
      }
    })


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
