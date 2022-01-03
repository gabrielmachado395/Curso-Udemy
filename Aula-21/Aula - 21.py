"""
Split, Join, Enumerate em Python
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # iteráveis
"""
# string = 'O Brasil é o país do futebol, é é Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

# string = 'O Brasil é o país do futebol, é é Brasil é penta.'
# lista = string.split(' ')
# string_2 = ',' .join(lista)
# print(string_2)

# string = 'O Brasil é o país do futebol, é é Brasil é penta.'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor)

lista =[
    ['Manuel', 'Levi', 'Pedro'],
    ['Luiz', 'Gustavo', 'José'],
    ['Lays', 'Pablo', 'Gabriel'],
]

print(lista[2][2])
