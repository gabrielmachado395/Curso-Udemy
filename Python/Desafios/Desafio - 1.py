"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print('O número que você digitou é um número par.')

    elif num % 2 != 0:
        print('O número que você digitou é um número impar.')

else:
    print('O que você digitou não é um número')



