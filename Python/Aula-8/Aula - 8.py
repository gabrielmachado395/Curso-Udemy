"""
Desafio da aula 8
"""
nome = "Gabriel Machado"
idade = 18
altura = 1.91
peso = 75
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, mede {altura}, pesa {peso}Kg, nasceu em {ano_nascimento}, e seu imc é {imc:.2f}')
