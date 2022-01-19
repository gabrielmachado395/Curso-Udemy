class A:
    vc = 1234

    def __init__(self):
        pass


a1 = A()
a2 = A()

A.vc = 'Alterada'

print(a1.vc)
print(a2.vc)
print(A.vc)
