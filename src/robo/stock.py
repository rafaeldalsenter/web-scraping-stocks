class Stock:
    def __init__(self, codigo, nome, sufixo_url):
        self.__codigo = codigo
        self.__nome = nome
        self.__sufixo_url = sufixo_url
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def sufixo_url(self):
        return self.__sufixo_url

    @sufixo_url.setter
    def sufixo_url(self, sufixo_url):
        self.__sufixo_url = sufixo_url