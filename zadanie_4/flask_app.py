from requests import get
from bs4 import BeautifulSoup
from flask import Flask, Response, render_template, request, redirect


class Company:
    def __init__(self,
                 name: str = None,
                 mail: str = None,
                 address: str = None,
                 number: str = None,
                 page: str = None
                 ):
        self.name = name
        self._mail = mail
        self._address = address
        self._number = number
        self._page = page


class SearchEngine:
    LINK_TAG = "a"
    DIV_TAG = "div"

    _URL: str = "https://panoramafirm.pl/szukaj?k="
    _PARSER_TYPE: str = "html.parser"

    def search(self, searching_key):
        return self._get_data(self._get_url(searching_key))

    def _get_data(self, url: str):
        companies = []
        companies_append = companies.append

        soup_page = BeautifulSoup(get(url).content, self._PARSER_TYPE)
        soup_page_list = soup_page.find_all('li', class_='company-item')

        for item in soup_page_list:
            soup_page = BeautifulSoup(str(item), self._PARSER_TYPE)

            try:
                companies_append(self.set_company(soup_page))
            except:
                pass

        return companies

    @staticmethod
    def set_company(soup_page):
        return Company(SearchEngine.find_data(soup_page, SearchEngine.LINK_TAG, "company-name").get_text().strip(),
                       SearchEngine.find_data(soup_page, SearchEngine.LINK_TAG, "icon-envelope")["data-company-email"],
                       SearchEngine.find_data(soup_page, SearchEngine.DIV_TAG, "address").get_text().strip(),
                       SearchEngine.find_data(soup_page, SearchEngine.LINK_TAG, "icon-telephone")["title"],
                       SearchEngine.find_data(soup_page, SearchEngine.LINK_TAG, "icon-website")["href"]
                       )

    @staticmethod
    def find_data(soup_page, tag: str, key: str):
        return soup_page.find(tag, class_=key)

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

        return render_template("index.html", title=TITLE, companies=search_engine.search(data.get('searching_key')))
    return redirect('/')


@flask_app.route('/health')
def health():
    return Response("", 200)


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=80)
