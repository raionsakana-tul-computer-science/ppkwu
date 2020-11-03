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
    return sum(letters), len(letters), letters


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
    return sum(letters), len(letters), letters


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
    return sum(letters), len(letters), letters


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
    return sum(letters), len(letters), letters


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

    count, strings, number_of_characters_in_strings = count_big_letters(text)

    return dumps({
        "big-letters": count,
        "number-of-strings": strings,
        "number-of-characters-in-string": number_of_characters_in_strings
    })


@flask_app.route('/small-letters/<text>')
def small_letters(text: str):
    if text is None:
        abort(415)

    count, strings, number_of_characters_in_strings = count_small_letters(text)

    return dumps({
        "small-letters": count,
        "number-of-strings": strings,
        "number-of-characters-in-string": number_of_characters_in_strings
    })


@flask_app.route('/numbers/<text>')
def numbers(text: str):
    if text is None:
        abort(415)

    count, strings, number_of_characters_in_strings = count_numbers(text)

    return dumps({
        "numbers":  count,
        "number-of-strings": strings,
        "number-of-characters-in-string": number_of_characters_in_strings
    })


@flask_app.route('/special-characters/<text>')
def special_characters(text: str):
    if text is None:
        abort(415)

    count, strings, number_of_characters_in_strings = count_special_characters(text)

    return dumps({
        "special-characters": count,
        "number-of-strings": strings,
        "number-of-characters-in-string": number_of_characters_in_strings
    })


@flask_app.route('/all-characters/<text>')
def all_characters(text: str):
    if text is None:
        abort(415)

    return dumps({
        "big-letters": count_big_letters(text),
        "small-letters": count_small_letters(text),
        "numbers": count_numbers(text),
        "special-characters": count_special_characters(text)
    })


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
