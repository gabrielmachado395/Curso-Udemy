"""
Função lambda em Python.
"""

lista = [
    ['P1', 54],
    ['P2', 78],
    ['P3', 105],
    ['P4', 41],
    ['P5', 54],
]
lista.sort(key=lambda item: item[0], reverse=True)
print(lista)
