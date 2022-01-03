"""
Faça um programa que pergunte a hora ao usuário e , baseando-se no horário
descrito, exiba a saudação apropriada.
Ex: Boa madrugada (0-5), Bom dia (6-12), Boa tarde (13-17) e Boa noite (16-23)
"""

nome = input('Digite seu nome: ')
hora = input('Digite o horário atual: ')

if hora.isdigit():
    hora = int(hora)

    if hora > 0 and hora < 6:
        print(f'Boa madrugada {nome}.')

    elif hora > 5 and hora < 13:
        print(f'Bom dia {nome}.')

    elif hora > 12 and hora < 18:
        print(f'Boa tarde {nome}.')

    elif hora > 17 and hora < 0:
        print(f'Boa noite {nome}.')

else:
    print('O que você digitou não é um número. Tente novamente.')
