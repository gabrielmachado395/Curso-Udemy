"""
Set em Python
add - adiciona, update - atualiza, clear - limpa, discard - deleta
union | - une, intersection & - todos os elementos presentes nos dois set's
difference - - elementos apenas no set da esquerda, symmetric_difference ^ - elementos que estão nos dois sets,
mas não em ambos
"""
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.discard(2)

# s1 = set()
# s1.update([1, 2, 3, 4, 5], {4, 5, 6, 7})
#
# print(s1)

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 5, 5, 6, 7}
s3 = s1 ^ s2
print(s3)
