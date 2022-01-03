"""
Variáveis:
Iniciam com letra, pode conter números, separa com _, somente letras minúsculas
"""
nome = 'Gabriel Machado'
idade = 18  # int
altura = 1.91  # float
e_maior = idade >= 18  # bool
peso = 75
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}.')
