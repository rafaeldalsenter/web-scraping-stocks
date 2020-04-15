from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

URL_STOCKS_LIST = 'https://www.infomoney.com.br/cotacoes/empresas-b3/'
HEADER_BASE = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

class Scraping:
    def __tratamento_html(self, input):
        html = input.decode('utf-8')
        return " ".join(html.split()).replace('> <', '><')

    def get_stock_value(self, stock):
        req = Request(stock.url, headers = HEADER_BASE)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(self.__tratamento_html(html), 'html.parser')
        find = soup.find('div', {'class' : 'value'}).find('p').get_text()
        
        return find

    def set_urls(self, list):
        req = Request(URL_STOCKS_LIST, headers = HEADER_BASE)
        response = urlopen(req)

        html = response.read()
        soup = BeautifulSoup(self.__tratamento_html(html), 'html.parser')

        for item in list:
            item.url = soup.find('td', {'class' : 'strong'}, text=item.codigo).find('a')['href']



