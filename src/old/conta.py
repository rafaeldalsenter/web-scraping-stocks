class Conta:
    def __init__(self, numero, titular, saldo, nome):
        print("Construindo objeto")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.__nome = nome

    # Podemos trabalhar com getters e setters
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    # assim poderá chama-lo como propriedade
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # métodos privados
    def __pode_printar_extrato(self):
        return True
    
    # métodos normais
    def extrato(self):
        if(self.__pode_printar_extrato()):
            print("Saldo {} do titular {}".format(self.saldo, self.titular))

    # método statics
    @staticmethod
    def codigo_banco():
        return "001"