def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(10,0)

if divide:
    print(divide)
else:
    print('Conta inválida!')


def f(var):
    print(var)
    print(id(var))

def dumb():
    return f

dumb()('frase na função f especificamente!')