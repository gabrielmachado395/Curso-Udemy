# Classes abstratas força as suas herdeiras a terem funções próprias.
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando na B.')


a = B()
a.falar()


