from cliente import Cliente

class TesteDeBanco(Cliente):
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def checagem_agencia(self, agencia):
        if agencia not in self.__dados:
            print(f'Acesso negado, agencia {agencia} inexistente.')
        else:
            return

    def checagem_cliente(self, nome):
        if nome not in self.__dados:
            print(f'Acesso negado, cliente {Cliente} inexistente.')
        else:
            return

    def checagem_conta(self, conta, nome):
        if conta not in self.__dados:
            print(f'Acesso negado, conta {conta} inexistente.')
            return
        else:
            print(f'Acesso liberado. Bem-Vindo(a) {nome}.')
            return
            
