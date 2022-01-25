from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, agencia, nome, conta):
        self._agencia = agencia
        self._nome = nome
        self._conta = conta
        return
        