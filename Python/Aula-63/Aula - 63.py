"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma
superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos
diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B está falando sobre {msg}.')


class C(A):
    def fala(self, msg):
        print(f'C está falando sobre {msg}.')


b = B()
c = C()
b.fala('Filmes')
c.fala('Deep Garage')
