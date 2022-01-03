"""
Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da função2 executada.
Faça a função1 executar duas funções que recebam um número diferente de argumentos.
"""


def master(função, *args, **kwargs):
    return função(*args, **kwargs)


def name(nome):
    return f'Olá {nome}'


def saudação(nome, saudação):
    return f'{saudação} {nome}'


var1 = master(name, 'Gabriel')
var2 = master(saudação, 'Gabriel', saudação='Boa Noite')
print(f'{var1} \n{var2}')