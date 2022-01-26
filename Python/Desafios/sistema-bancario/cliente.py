from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self._conta = None
    

    def inserir_conta(self, conta):
        self.conta = conta
        