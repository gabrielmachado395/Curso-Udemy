# Aqui uma classe depende da outra para funcionar
from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Arroz', 8)
p2 = Produto('Carne', 50)
p2 = Produto('Ps5', 5000)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)

carrinho.lista_produtos()
print(carrinho.soma_total())