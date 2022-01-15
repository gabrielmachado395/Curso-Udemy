# Mutável: Listas, Dicionários
# Imutável: Tuplas, Strings, Números, True, False, None

def lista_de_clientes(clientes_iteravel, lista=None):
    # Não se deve colocar itens mutáveis dentro de parâmetros de funções
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes = ['Gabriel']
clientes1 = lista_de_clientes(['João', 'Gustavo', 'Eduarda'], lista_clientes)
clientes2 = lista_de_clientes(['Pedro', 'Luiz', 'Júlia'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
