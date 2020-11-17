from typing import Callable, Dict
from flask import Flask, abort


class Calendar:
    _VALIDATION_ERROR: str = "ERROR, given year or month is not correct data, please, check out and try again."
    _CALENDAR_URL: str = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?%s&lang=1"

    _JANUARY: int = 1
    _DECEMBER: int = 12

    def get_calendar(self, year: str, month: str):
        if self._validate(year, month):
            return self._get_calendar_url(year, month)

        return self._VALIDATION_ERROR

    def _get_calendar_url(self, year: str, month: str) -> str:
        return self._CALENDAR_URL % f"rok={year}&miesiac={month}"

    def _validate(self, year: str, month: str) -> bool:
        try:
            int(year)
            month = int(month)
            return self._JANUARY <= month <= self._DECEMBER
        except ValueError:
            pass

        return False


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
