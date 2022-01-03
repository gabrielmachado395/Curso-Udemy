variavel = 'valor'                    # Valor global ou universal como eu prefiro chamar.


def func():
    print(variavel)


# def func2():
#     global variavel                 # Essa linha altera o valor da variável universal(prática não-recomendada)
#     variavel = 'Outro valor'        # Nessa função a variável é alterado mas a original se mantem.
#     print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
var = func2(arg=variavel)

print(var)
