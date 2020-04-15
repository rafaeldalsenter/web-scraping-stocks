class Quote:
    def __init__(self, codigo, date, value):
        self.__codigo = codigo
        self.__date = date
        self.__value = value
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value