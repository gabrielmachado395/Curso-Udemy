from Dados import produtos, pessoas, lista
from functools import reduce

# soma_precos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
# print(round(soma_precos / len(produtos)))

media_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(round(media_idade / len(pessoas)))
