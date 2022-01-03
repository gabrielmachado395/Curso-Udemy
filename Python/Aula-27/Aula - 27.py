"""
Funções (def) em Python - return
"""


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(85, 85)

if divide:
    print(divide)
else:
    print('Conta inválida.')
