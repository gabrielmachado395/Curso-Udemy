"""
count - Itertools
"""
from itertools import count

contador = count(start=2, step=2)

lista = ['Gabriel', 'Pedro', 'Luiz', 'Gustavo', 'Levi']
lista = zip(contador, lista)
print(list(lista))
