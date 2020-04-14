from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

def tratamento_html(input):
    html = input.decode('utf-8')
    return " ".join(html.split()).replace('> <', '><')

def ler_infoMoney():
    url = 'https://www.infomoney.com.br/cotacoes/smiles-smls3/'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    try:
        req = Request(url, headers= headers)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(tratamento_html(html), 'html.parser')
        find = soup.find('div', {'class' : 'value'}).find('p').get_text()
        print(find)

    except HTTPError as e:
        print(e.status, e.reason) 

def ler_investing():
    url = 'https://br.investing.com/equities/smiles-on'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    try:
        req = Request(url, headers= headers)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(tratamento_html(html), 'html.parser')
        find = soup.find('span', {'id' : 'last_last'}).get_text()
        print(find)

    except HTTPError as e:
        print(e.status, e.reason) 


if __name__ == '__main__':
    ler_investing()
    ler_infoMoney()
      
    


    

    
    


