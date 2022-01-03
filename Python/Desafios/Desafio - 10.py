"""
Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (Ex: 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
# valores = 0
#
# num = input('Digite um valor: ')
# per = input('Digite o percentual no qual ele será somado: ')


def num(n, p):
    print(n + (n * p / 100))


num(50, 10)
num(15, 100)
