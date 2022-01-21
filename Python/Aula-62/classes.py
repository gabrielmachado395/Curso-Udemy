class A:
    def falar(self):
        print('Falando em A.')


class B(A):
    def digitar(self):
        print('Falando em B.')


class C(A):
    def falar(self):
        print('Falando em C')
        # B e C não têm ligação.


class D(B, C):
    pass
    # Essa classe tem herança múltipla porque herda de B e C.
    # E essa classe está no Problema do Diamante, porque herda de duas ou mais classes que tem métodos iguais.
    # Caso receba um método próprio será executado somente ele.


d = D()
# Aqui será executado somente o primeiro método encontrado, que nesse caso, é o de B.
# Mas caso ocorra uma alteração em B será executado C.
d.falar()
