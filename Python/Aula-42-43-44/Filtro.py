from Dados import produtos, pessoas, lista
from itertools import groupby

# def filtro(pessoa):
#     if pessoa['idade'] < 18:
#         return True
# Retorna pessoas menores de idade


def filtro(pessoa):
    if pessoa['idade'] >= 18:
        return True


nova_lista = filter(filtro, pessoas)

for idade in nova_lista:
    print(idade)


# nova_lista = filter(lambda x: x > 0, lista)
# print(list(nova_lista))

