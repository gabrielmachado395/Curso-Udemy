"""
While / Else
Contadores e Acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    acumulador += contador
    contador += 1
    print(contador, acumulador)

else:
    print('Cheguei no else.')

