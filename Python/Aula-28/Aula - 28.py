"""
Funções (def) em Python - *args, **kwargs
"""


def func(*args, **kwargs):
    print(args, kwargs)

    idade = kwargs['idade']


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista, nome='Gabriel', sobrenome='Machado', idade=18)
