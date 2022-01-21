class TaErradoError(Exception):
    pass
    # 2 Linhas de código, uma exceção.


def testar():
    raise TaErradoError('Tá Serto.')


try:
    testar()
except TaErradoError as serto:
    print(f'Erro: {serto}')
