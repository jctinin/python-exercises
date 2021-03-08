# exercicio 1
def congrats(nome, saudacao):
    print(f"Olá {nome}! Tudo bem? {saudacao}")


name = "Julio"
phrase = "Seja bem vindo!!"

congrats(name, phrase)


# exercicio 2
def soma_numeros(num1, num2, num3):
    print(num1 + num2 + num3)


soma_numeros(4, 5, 6)


def calculo_percentual(num, perc):
    return num + (num / 100 * perc)


print(calculo_percentual(100, 10))


def fizz_buzz(num):
    if num % 5 == 0:
        return 'buzz'
    if num % 3 == 0:
        return 'fizz'
    if num % 5 == 0 and num % 3 == 0:
        return 'fizzBuzz'
    return num


print(fizz_buzz(4))
