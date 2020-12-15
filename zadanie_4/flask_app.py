from requests import get
from bs4 import BeautifulSoup
from flask import Flask, Response, render_template, request, redirect


class SearchEngine:
    _URL: str = "https://panoramafirm.pl/szukaj?k="
    _PARSER_TYPE: str = "html.parser"

    def search(self, searching_key):
        return self._get_data(self._get_url(searching_key))

    def _get_data(self, url: str):
        list_ = []
        list_append = list_.append

        soup_page = BeautifulSoup(get(url).content, self._PARSER_TYPE)
        soup_page_list = soup_page.find_all('td', class_='li')

        for item in soup_page_list:
            print(item)
            soup_page = BeautifulSoup(str(item), self._PARSER_TYPE)
            list_append(soup_page)

        return str(soup_page)

    def _get_url(self, searching_key: str):
        return f"{self._URL}{searching_key}"


TITLE = "Zadanie 4"
flask_app = Flask(__name__)
search_engine = SearchEngine()


@flask_app.route('/')
def main():
    return render_template("index.html", title=TITLE)


@flask_app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        data = request.form

        return render_template("index.html", title=TITLE, content=search_engine.search(data.get('searching_key')))
    return redirect('/')


@flask_app.route('/health')
def health():
    return Response("", 200)


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
