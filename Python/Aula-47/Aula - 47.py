

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
        # Tentando converter o valor para inteiro
    except ValueError:
        try:
            valor = float(valor)
            return valor
            # Tentando converter o valor para bool
        except ValueError:
            pass


while True:
    print('=-' * 22)
    numero = converte_numero(input('Digite um número: '))

    if numero is None:
        print('Erro: Isso não é um número. Tente novamente.')
    else:
        print(numero * 2)
