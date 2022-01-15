
with open('abc.txt', 'a+') as file:
    file.write('Linha 1 \n')
    file.write('Linha 2 \n')
    file.write('Linha 3 \n')
    file.write('Outra Linha \n')

    file.seek(0)
    print(file.read())
    file.close()
    # Devo lembrar de sempre fechar um arquivo após usa-lo ao final do código de uso

# Estou pedindo para abrir um arquivo que ainda não existe e pedindo para ler e escrever

# file.write('Arquivo criado ao executar o código da Aula 49\n')
# file.write('Linha1\n')
# file.write('Linha2\n')
# file.write('Linha3\n')
#
# file.seek(0, 0)
# print('Lendo linhas:')
# print(file.read())
