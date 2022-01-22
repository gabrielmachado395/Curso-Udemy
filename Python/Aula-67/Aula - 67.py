"""
# arquivo = open('abc.txt', 'w')
# arquivo.write('Alguma coisa.')
# arquivo.close()
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando arquivo.')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo.')
        self.arquivo.close()
        # Tratei a exceção
        return True


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma outra coisa.')
    # Um jeito melhor de abrir arquivos em Python sem precisar fecha-los manualmente.
"""
from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print('Abrindo arquivo')
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
