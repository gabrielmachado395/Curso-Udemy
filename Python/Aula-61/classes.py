class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando')


class ClienteVIP(Cliente):
    # ClienteVIP recebe Cliente que recebe Pessoa.
    # Logo todos os conceitos dentro de Pessoa e Cliente o ClienteVip possui.
    def falar(self):
        super().falar()
        # Esse comando faz com que o conceito escolhido seja executado antes do código abaixo
        print(f'{self.nomeclasse} está falando')

