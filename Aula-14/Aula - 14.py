"""
Formatando valores com modificadores

:s - textos (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float) :.2f
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
nome = 'Gabriel Machado'
nome_format = '{n:0<20}'.format(n=nome)
print(nome_format)

