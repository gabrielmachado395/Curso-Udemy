class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramentas(self):
        return self.__ferramenta

    @ferramentas.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo.')

class MaquinaDeEscrever:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('A máquina está escrevendo')