class Stock:
    def __init__(self, codigo, url):
        self.__codigo = codigo
        self.__url = url
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url