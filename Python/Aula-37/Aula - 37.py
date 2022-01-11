# list, tuples, str -> Sequences -> Iterável
nome = 'Gabriel Machado'
iterador = iter(nome)
gerador = (x for x in nome)
print(next(gerador))
print(next(iterador))
