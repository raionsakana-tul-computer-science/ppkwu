from typing import Dict

from requests import get
from bs4 import BeautifulSoup
from flask import Flask


class CalendarHandler:
    _VALIDATION_ERROR: str = "ERROR, given year or month is not correct data, please, check out and try again."
    _CALENDAR_URL: str = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?%s&lang=1"
    _PARSER_TYPE: str = "html.parser"

    _JANUARY: int = 1
    _DECEMBER: int = 12
    _SIZE: int = 2

    def get_calendar(self, year: str, month: str):
        if self._validate(year, month):
            events = self._get_events(self._get_calendar_url(year, month))
            return str(events)

        return self._VALIDATION_ERROR

    def _get_events(self, url: str) -> Dict[int, str]:
        events = {}

        soup_page = BeautifulSoup(get(url).content, self._PARSER_TYPE)
        soup_page_list = soup_page.find_all('td', class_='active')

        for soup_page_element in soup_page_list:
            soup_date = BeautifulSoup(str(soup_page_element), self._PARSER_TYPE)
            date = soup_date.find('a').get_text()
            event = soup_date.find('div').get_text()
            events[int(date)] = str(event)

        return events

    def _get_calendar_url(self, year: str, month: str) -> str:
        return self._CALENDAR_URL % f"rok={year}&miesiac={self._get_month(month)}"

    def _get_month(self, month):
        return month if len(month) == self._SIZE else f'0{month}'

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
calendar = CalendarHandler()


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
