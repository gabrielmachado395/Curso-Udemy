# Herança - Uma classe é outra
from classes import *

c1 = Cliente('Luiz', 45)
a1 = Aluno('Pedro', 16)

print(c1.nome)
print(a1.nome)

c1.comprar()
a1.estudar()
a1.falar()
