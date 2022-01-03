"""
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne "Fizz",
se o parâmetro da função for divisível por 5, retorne "Buzz". Se o parâmetro da
função for divisível por 5 e 3, retorne "FizzBuzz", caso contrário, retorne o
número enviado.
"""
from random import randint


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisível por 3 e por 5'
    if n % 5 == 0:
        return f'Buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'Fizz, {n} é divisível por 3'
    return n


for i in range(50):
    aleatorio = randint(0, 50)
    print(fb(aleatorio))
