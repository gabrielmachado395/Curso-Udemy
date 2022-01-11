# lista = "012345"
# lista = iter(lista)
# print(hasattr(lista, '__next__'))

import sys

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))

# Mostra o espaço em que as listas consomem, em Bytes
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
