

def master(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave
    # Função decoradora

@master
# Decorador
def fala_oi():
    print('Oi')
# Função decorada

fala_oi()