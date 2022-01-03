"""
Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.
"""
valores = 0

for números in range(3):                    # Loop para o usuário digitar os 3 valores a serem somados
    num = input('Digite um valor: ')
    num = num.isnumeric()

    if num is not True:                     # Teste para caso o usuário digite uma letra o sistema não dê erro
        print('Você deve digitar um número.')

    def soma(n1, n2, n3):
        return n1 + n2 + n3

    valores += num

print(valores)
