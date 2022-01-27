"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
"""
from dataclasses import dataclass

@dataclass(eq=True, order=True, frozen=False, init=True)
# Para deixar imútavel basta colocar tudo como False.
class Pessoa:
    nome: str
    sobrenome: str

    def __port_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Tipo inválido {type(self.nome).__name__} != strm em {self}'
                )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('A', '3')
p2 = Pessoa('C', '2')
p3 = Pessoa('544', '1')
p4 = Pessoa('B', '4')

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
print(p1) 