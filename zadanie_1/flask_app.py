from flask import Flask

ERROR_MESSAGE: str = "Error: message not found"

flask_app = Flask(__name__)


@flask_app.route('/rev/<text>')
def rev(text: str):
    if text is not None:
        return text[::-1]

    return ERROR_MESSAGE


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
