from flask import Flask, abort
from json import dumps

INFO_MESSAGE: str = "Info: To get stats of message, use /*endpoint name*/*your message*"
flask_app = Flask(__name__)


def count_characters(text, condition):
    index, mark = 0, False
    temp_letters = [0]

    for c in text:
        if condition(c):
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


def check_if_big_letter(c: str):
    return c.isupper()


def check_if_small_letter(c: str):
    return c.islower()


def check_if_number(c: str):
    return c.isnumeric()


def check_if_special_character(c: str):
    return not c.isnumeric() and not c.isupper() and not c.islower()


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

    return dumps(count_characters(text, check_if_big_letter))


@flask_app.route('/small-letters/<text>')
def small_letters(text: str):
    if text is None:
        abort(415)

    return dumps(count_characters(text, check_if_small_letter))


@flask_app.route('/numbers/<text>')
def numbers(text: str):
    if text is None:
        abort(415)

    return dumps(count_characters(text, check_if_number))


@flask_app.route('/special-characters/<text>')
def special_characters(text: str):
    if text is None:
        abort(415)

    return dumps(count_characters(text, check_if_special_character))


@flask_app.route('/all-characters/<text>')
def all_characters(text: str):
    if text is None:
        abort(415)

    return dumps({
      "big-letters": count_characters(text, check_if_big_letter),
      "small-letters": count_characters(text, check_if_small_letter),
      "numbers": count_characters(text, check_if_number),
      "special-characters": count_characters(text, check_if_special_character)
    })


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
