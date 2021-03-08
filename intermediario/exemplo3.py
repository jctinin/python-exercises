# seção 3, aula 54


def func(a1, a2, a3, a4, a5, nome=None, a6="João"):
    print(a1, a2, a3, a4, a5, nome, a6)


func(1, 2, 3, 4, 5, "Julio", "Josefa")

lista = ["Julio", "Josefa", 3, 4, 5, 6]
n1, n2, *n = lista  # desempacotamento da lista, equivalente a desestruturação
print(n1, n2)
print(*lista, sep="--")


def func1(*args, **kwargs):
    n1, n2, n3, *n = args
    print(n1, n2, n3)
    print(args[-1])
    args = list(args)
    args[3] = "José"
    print(args, "aqui")
    print(kwargs)
    sobrenome = kwargs.get("sobrenome")
    print(sobrenome)


func1(1, 2, 3, 4, 5, 6)
func1(*lista, 20, 30, nome="Diego", sobrenome="Tinin")


def func2(arg1, arg2="função2"):
    return arg1, arg2


def func3():
    return "função1"


var = func3()
var1 = func2(var)

print(func2(func3()))
print(var1)


a = lambda x, y: x * y

print(a(10, 5))


lista = [["a4", 22], ["a1", 15], ["a2", 2], ["a5", 50], ["a3", 8], ["a6", 32]]


def func4(item):
    return item[0]


lista.sort(key=func4, reverse=True)
print(lista)


print(sorted(lista, key=lambda i: i[0]))
lista.sort(key=lambda item: item[1])
print(lista)
