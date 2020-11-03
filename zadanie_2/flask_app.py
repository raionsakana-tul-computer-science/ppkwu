from flask import Flask

INFO_MESSAGE: str = "Info: To get stats of message, use /*endpoint name*/*your message*"
flask_app = Flask(__name__)


@flask_app.route('/')
def main():
    return INFO_MESSAGE


@flask_app.route('/health')
def health():
    return ""


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
