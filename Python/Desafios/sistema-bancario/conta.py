from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, cliente, conta, saldo):
        self.agencia = agencia
        self.cliente = cliente
        self.conta = conta
        self.saldo = saldo
    
    @property
    def agencia(self):
        return self.agencia
    
    def agencia(self, num_agencia):
        if num_agencia not in self.__dados:
            print(f'Acesso negado, agencia {num_agencia} inexistente.')
        else:
            pass

        self.agencia = num_agencia   

    @property
    def cliente(self):
        return self.cliente

    @property
    def conta(self):
        return self.conta

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser númerico.')
        
        self.saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor do depósito precisa ser numérico.')

        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' | ')
        print(f'Cliente: {self.cliente}', end=' | ')
        print(f'Conta: {self.conta}', end=' | ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass
