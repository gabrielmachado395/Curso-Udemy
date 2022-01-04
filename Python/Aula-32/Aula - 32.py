"""
Dicionários em Python
"""
clientes = {
    'cliente1': {
        'nome': 'Gabriel',
        'sobrenome': 'Machado',
    },
    'cliente2': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio',
    },
    'cliente3': {
        'nome': 'Gustavo',
        'sobrenome': 'Guanabara',
    },
}

for clientes_n, clientes_v in clientes.items():
    # Aqui ocorre o loop no dicionário mestre
    print(f'Exibindo {clientes_n}')

    for dados_n, dados_v in clientes_v.items():
        # Aqui ocorre o loop nos dicionários menores
        print(f'\t{dados_n} = {dados_v}')
