class A:
    def __new__(cls, *args, **kwargs):
        print('Eu sou o Neo')
        return object().__new__(cls)

    def __init__(self):
        print('Eu sou o INIT.')


a = A()
