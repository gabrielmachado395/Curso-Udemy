"""
Gerando CPF com Python
"""

from random import randint

numero = str(randint(100000000, 999999999))
novo_cpf = numero               # Elimina os dois últimos dígitos do CPF
reverso = 10                    # Contador reverso
total = 0

# Loop do CPF
for index in range(19):
    if index > 8:               # O primeiro índice vai de 0 a 9
        index -= 9              # São os 9 primeiros dígitos do CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

    reverso -= 1                # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:               # Se o dígito for maior que 9 o valor é 0
            d = 0
        total = 0               # Zera o total
        novo_cpf += str(d)      # Concatena o dígito gerado no novo CPF

print(novo_cpf)
