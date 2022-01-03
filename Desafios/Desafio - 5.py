"""
Use um laço para fazer dois contadores contarem de formas opostas.
O primeiro irá contar de 0 á 8
O segundo irá contar de 10 á 2
"""

cont_crescente = -1
cont_decrescente = 11

while cont_crescente < 8 and cont_decrescente > 2:
    cont_crescente += 1
    cont_decrescente -= 1

    print(cont_crescente, cont_decrescente)
