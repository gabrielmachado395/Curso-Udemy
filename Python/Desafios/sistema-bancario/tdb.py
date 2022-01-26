class TesteDeBanco():
    def __init__(self):
        self.__dados = {(111, 'Pedro', 222, 0), (333, 'Carla', 444, 8)}

    @property
    def dados(self):
        return self.__dados

    def checagem_agencia(self, agencia):
        if agencia not in self.__dados:
            print(f'Acesso negado, agencia {agencia} inexistente.')
        else:
            pass

    def checagem_cliente(self, nome):
        if nome not in self.__dados:
            print(f'Acesso negado, cliente {nome} inexistente.')
        else:
            pass

    def checagem_conta(self, conta, nome):
        if conta not in self.__dados:
            print(f'Acesso negado, conta {conta} inexistente.')
        else:
            print(f'Acesso liberado. Bem-Vindo(a) {nome}.')
            return
            
            
TesteDeBanco(111, 'Pedro', 222, 0)
