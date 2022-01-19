from classes import Cliente

cliente1 = Cliente('Pedro', 'Derick', 19)
cliente1.insere_endereco('Fortaleza', 'CE')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 'Eduarda', 17)
cliente2.insere_endereco('Fortaleza', 'CE')
cliente2.insere_endereco('Cascavel', 'CE')
print(cliente2.nome)
cliente2.lista_enderecos()
print()
del cliente2

cliente3 = Cliente('Gabriel', 'Machado', 18)
cliente3.insere_endereco('Fortaleza', 'CE')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
del cliente3
