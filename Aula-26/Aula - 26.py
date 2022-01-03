"""
Funções - def em Python
"""


def saudação(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variável = saudação()
print(variável)
