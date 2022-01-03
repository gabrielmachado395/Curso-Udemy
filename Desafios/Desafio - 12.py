"""
Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da
função2 executada.
"""


def hello():                    # Aqui será a função que será executada
    return 'Olá Mundo'


def master(função):             # Aqui onde a função inicial será inserida
    return função()


var = master(hello)             # Aqui onde a função mestre recebe a função inicial para que ela possa ser executada
print(var)
