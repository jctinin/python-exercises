def funcao(frase='Hello friend'):
    try:
        return(frase.replace('e', '3'))
    except OSError:
       return print('Dessa vez não!')



print(funcao('Olá Mundo!'))
print(funcao('Hello World!'))
funcao()
funcao()

