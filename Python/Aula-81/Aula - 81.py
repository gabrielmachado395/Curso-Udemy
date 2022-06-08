"""
Comma Separated Valuers - CSV (Valores Separados por Virgula)
É um formato de dados muito em tabelas (Excel, Google Sheets),
bases de dados, clientes de e-mail, etc...
"""
import csv

with open(r'Aula-81\fornecedor.csv', 'r',) as arquivo:
    dados = csv.reader(arquivo)

    for dado in dados:
        print(dado)
    