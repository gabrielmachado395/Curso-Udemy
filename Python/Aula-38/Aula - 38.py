"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest
# Código
cidades = ['Fortaleza', 'Goiania', 'Salvador', 'Maranhão']

# Mais código
estados = ['CE', 'GO', 'BA']

cidades_estados = zip_longest(cidades, estados, fillvalue='Estado')
print(list(cidades_estados))
