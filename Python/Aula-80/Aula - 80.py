"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de leve utilização. Muito utilizado por API's
"""

from dados import *
import json

dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)

#dicionario = json.loads(clientes_json)
#
#for chave, valor in dicionario.items():
#   print(chave)
#   print(valor)
