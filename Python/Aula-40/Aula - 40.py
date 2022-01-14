"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa(No caso não repete "valor1, valor2" como "valor2, valor1")
Permutação - Ordem importa(Nesse caso repete)
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos(Ex: "valor1, valor1" )
"""
from itertools import combinations, permutations, product

lista = ['Gabriel', 'Luiz', 'Pedro', 'Gustavo', 'Pablo', 'Levi']

for pessoas in product(lista, repeat=2):
    print(pessoas)
