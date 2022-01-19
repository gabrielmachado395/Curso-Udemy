"""
public - Fica acessível dentro e fora da classe
protected - '_' é usado para deixar o atributo privado(de maneira masi fraca)
private - '__' é usado para deixar o atributo totalmente privado
"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados
        # Aqui estou liberando o acesso para os dados

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'Pedro')
bd.inserir_clientes(2, 'Rose')
print(bd.dados)

