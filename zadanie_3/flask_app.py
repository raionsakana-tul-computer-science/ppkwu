from typing import Callable, Dict
from flask import Flask, abort

INFO_MESSAGE: str = "Info: zadanie_3"
flask_app = Flask(__name__)


@flask_app.route('/')
def main():
    return INFO_MESSAGE


@flask_app.route('/health')
def health():
    return ""


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
