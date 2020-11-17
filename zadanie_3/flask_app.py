from typing import Callable, Dict
from flask import Flask, abort


class Calendar:
    CALENDAR_URL: str = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?%s&lang=1"

    def get_calendar(self, year: str, month: str):
        return self.CALENDAR_URL % f"rok={year}&miesiac={month}"


INFO_MESSAGE: str = "Info: zadanie_3"
flask_app = Flask(__name__)
calendar = Calendar()


@flask_app.route('/')
def main():
    return INFO_MESSAGE


@flask_app.route('/health')
def health():
    return ""


@flask_app.route('/calendar/<year>/<month>')
def get_calendar(year: str, month: str):
    return calendar.get_calendar(year, month)


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
