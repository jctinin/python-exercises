perguntas = {
    "Pergunta 1": {
        "pergunta": "Quanto é 2 + 2?",
        "respostas": {"a": "1", "b": "4", "c": "17"},
        "resposta_certa": "b",
    },
    "Pergunta 2": {
        "pergunta": "Qual é capital de São Paulo?",
        "respostas": {"a": "Guarulhos", "b": "Santo André", "c": "São Paulo"},
        "resposta_certa": "c",
    },
    "Pergunta 3": {
        "pergunta": "Quanto é 3 * 2?",
        "respostas": {"a": "6", "b": "4", "c": "17"},
        "resposta_certa": "a",
    },
}

print()
respostas_certas = 0

for pk, pv in perguntas.items():
    print()
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha uma opção abaixo:')
    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')

    resposta = input('Sua resposta: ')
    if resposta == pv["resposta_certa"]:
        print('Parabéns!! Você acertou!!')
        respostas_certas += 1
    else:
        print('Droga! Você errou')

    print()

qtd_perguntas = len(perguntas)
percentual = respostas_certas / qtd_perguntas * 100

print(f'Seu percentual de acerto foi de {round(percentual)}%')
