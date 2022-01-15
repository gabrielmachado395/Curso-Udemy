"""
raise - Levantando minhas próprias exceções em Python.
"""


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser zero")    # Aqui é levantado uma exceção própria
    return n1 / n2


try:
    print(divide(55, 0))
except ValueError as error:
    print(error)
