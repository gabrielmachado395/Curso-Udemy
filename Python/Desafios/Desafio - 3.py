"""
Faça um programa que peça o primierio nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"seu nome é normal"; maior que 6 escreva "seu nome é muito grande"
"""

nome = input('Digite o seu primeiro nome: ')
nome = len(nome)

if nome == 4:
    print(f'Olá {nome}, o seu nome é curto.')

elif nome > 4 and nome < 7:
    print(f'Olá {nome}, o seu nome é normal.')

elif nome > 6:
    print(f'Olá {nome}, o seu nome é muito grande.')
