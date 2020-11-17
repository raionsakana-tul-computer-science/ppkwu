from typing import Callable, Dict
from flask import Flask, abort

INFO_MESSAGE: str = "Info: zadanie_3"
flask_app = Flask(__name__)


class Calendar:
    CALENDAR_URL: str = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php"

    @staticmethod
    def get_calendar(year: str, month: str):
        pass


@flask_app.route('/')
def main():
    return INFO_MESSAGE


@flask_app.route('/health')
def health():
    return ""


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
