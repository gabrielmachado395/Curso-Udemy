"""
Sistemas de perguntas em Python
"""
print('''Olá Usuário. 
Hoje será testado um simples sistema de perguntas e respostas.
Basta responder digitando a alternativa.''')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '8'},
        'resposta_correta': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5*4? ',
        'respostas': {'a': '20', 'b': '45', 'c': '10'},
        'resposta_correta': 'a'
    },
}

respostas_corretas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas: ')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Digite sua resposta: ')

    if resposta_user == pv['resposta_correta']:
        print('Parabéns!!! Você acertou!!!')
        respostas_corretas += 1
    else:
        print('Que pena, você errou.')

num_perguntas = len(perguntas)
porcentagem_acertos = respostas_corretas / num_perguntas * 100

print(f'Você acertou {respostas_corretas} de 2 questões.')
print(f'Sua porcentagem de acertos foi de {porcentagem_acertos}%.')
