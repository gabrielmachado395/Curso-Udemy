segredo = 'lofi'
digitadas = []
chances = 2

while True:
    if chances == 0:
        print('Você perdeu.')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Você só pode digitar uma letra.')
        continue

    digitadas.append(letra)

    if letra in segredo:
        print(f'A letra {letra} existe na palavra secreta.')
    else:
        print(f'A letra {letra} não existe na palavra secreta.')
        digitadas.pop()

    segredo_temporário = ''
    for letra_secreta in segredo:
        if letra_secreta in digitadas:
            segredo_temporário == letra_secreta
        else:
            segredo_temporário += '*'

        if segredo_temporário == segredo:
            print(f'PARABÉNS, VOCÊ GANHOU !!! A palavra secreta é {segredo_temporário}.')
        else:
            print(f'Que pena, você perdeu. A palavra secreta é {segredo_temporário}.')

        if letra not in segredo:
            chances -= 1

        print(f'Você ainda tem {chances} chances.')
