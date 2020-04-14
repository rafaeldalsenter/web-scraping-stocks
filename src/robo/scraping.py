from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

URL_BASE = 'https://www.infomoney.com.br/cotacoes/'
HEADER_BASE = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

class Scraping:
    def __init__(self, path):
        self.path = path

    def __tratamento_html(self, input):
        html = input.decode('utf-8')
        return " ".join(html.split()).replace('> <', '><')

    def get_value(self, stock):
        try:
            url = "{}{}".format(URL_BASE, stock.sufixo_url)

            req = Request(url, headers = HEADER_BASE)
            response = urlopen(req)
            html = response.read()
            soup = BeautifulSoup(self.__tratamento_html(html), 'html.parser')
            find = soup.find('div', {'class' : 'value'}).find('p').get_text()
            
            return find

        except HTTPError as e:
            print(e.status, e.reason)
            return '-1' 
