from Dados import produtos, pessoas, lista

# nova_lista = list(map(lambda x: x * 2, lista))
# # nova_lista = [x * 2 for x in lista]
# # Faz a mesma coisa
# print(nova_lista)

valores = map(lambda v: v['preço'], produtos)
# Aqui estou retornando apenas os nomes das pessoas

for valor in valores:
    # Aqui estou organizando os valores automaticamente
    print(round(valor))
