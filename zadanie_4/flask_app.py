from typing import Dict

from requests import get
from bs4 import BeautifulSoup
from flask import Flask, Response, render_template, request, redirect

from icalendar import Calendar, Event
from datetime import datetime
from pytz import timezone
#
#
# class CalendarHandler:
#     _VALIDATION_ERROR: str = "ERROR, given year or month is not correct data, please, check out and try again."
#     _CALENDAR_URL: str = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?%s&lang=1"
#     _PARSER_TYPE: str = "html.parser"
#
#     _JANUARY: int = 1
#     _DECEMBER: int = 12
#     _SIZE: int = 2
#
#     _TIMEZONE = timezone("Europe/Warsaw")
#     _FORMAT = "%Y-%m-%d_%H:%M:%S_%Z%z"
#
#     def get_calendar(self, year: str, month: str) -> Response:
#         if self._validate(year, month):
#             return Response(
#                 self._fill_calendar(month, year),
#                 mimetype="text/plain",
#                 headers={
#                     "Content-Disposition":
#                     f"attachment;filename=weeia_{year}_{self._get_month(month)}.ics"
#                 }
#             )
#
#         return Response(self._VALIDATION_ERROR, 404)
#
#     def _fill_calendar(self, month: str, year: str) -> bytes:
#         cal = self._get_calendar(month, year)
#         events = self._get_events(self._get_calendar_url(year, month))
#
#         for key, value in events.items():
#             event = self._set_event_to_calendar(key, month, value, year)
#             cal.add_component(event)
#
#         return cal.to_ical()
#
#     def _set_event_to_calendar(self, key: int, month: str, value: str, year: str) -> Event:
#         date_now, date_start_event, date_stop_event = self._get_dates(key, month, year)
#
#         event = Event()
#         event.add('summary', value)
#         event.add('dtstart', date_start_event)
#         event.add('dtend', date_stop_event)
#         event.add('dtstamp', date_now)
#
#         event['uid'] = f'{date_start_event.strftime(self._FORMAT)}@mxm.dk'
#         return event
#
#     def _get_dates(self, key, month, year):
#         date_start_event = self._TIMEZONE.localize(datetime(int(year), int(month), int(key), 0, 0, 0))
#         date_stop_event = self._TIMEZONE.localize(datetime(int(year), int(month), int(key), 23, 59, 0))
#         date_now = self._TIMEZONE.localize(datetime.now())
#         return date_now, date_start_event, date_stop_event
#
#     def _get_calendar(self, month: str, year: str) -> Calendar:
#         cal = Calendar()
#         cal.add('prodid', f'-//WEEIA calendar {self._get_month(month)}-{year}//mxm.dk//')
#         cal.add('version', '2.0')
#         return cal
#
#     def _get_events(self, url: str) -> Dict[int, str]:
#         events = {}
#
#         soup_page = BeautifulSoup(get(url).content, self._PARSER_TYPE)
#         soup_page_list = soup_page.find_all('td', class_='active')
#
#         for soup_page_element in soup_page_list:
#             soup_date = BeautifulSoup(str(soup_page_element), self._PARSER_TYPE)
#             date = soup_date.find('a').get_text()
#             event = soup_date.find('div').get_text()
#             events[int(date)] = str(event)
#
#         return events
#
#     def _get_calendar_url(self, year: str, month: str) -> str:
#         return self._CALENDAR_URL % f"rok={year}&miesiac={self._get_month(month)}"
#
#     def _get_month(self, month) -> str:
#         return month if len(month) == self._SIZE else f'0{month}'
#
#     def _validate(self, year: str, month: str) -> bool:
#         try:
#             int(year)
#             month = int(month)
#             return self._JANUARY <= month <= self._DECEMBER
#         except ValueError:
#             pass
#
#         return False


TITLE = "Zadanie 4"
flask_app = Flask(__name__)
# calendar = CalendarHandler()


@flask_app.route('/')
def main():
    return render_template("index.html", title=TITLE)


@flask_app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        data = request.form

        return render_template("index.html", title=TITLE, content=data.get('searching_key'))
    return redirect('/')


@flask_app.route('/health')
def health():
    return ""


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
