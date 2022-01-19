from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    # Não utiliza nenhuma instância somente a classe em si
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    # Não utiliza nem instância nem a classe em si
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa('Gabriel', 19)
print(f'Nome: {p1.nome}')
print(f'Idade: {p1.idade}')
p1.get_ano_nascimento()
print(f'Id: {p1.gera_id()}')
