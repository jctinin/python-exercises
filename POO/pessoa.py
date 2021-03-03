from datetime import  datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False, treinando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.treinando = treinando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
            
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True


    def treinar(self, exercicio):
        if self.treinando:
            print(f'{self.nome} já está treinando')
            return

        print(f'{self.nome} está treinando {exercicio}')
        self.treinando = True

    def parar_falar(self):
        if self.falando:
            print(f'{self.nome}, já está falando faz tempo')
            return

        if self.comendo:
            print(f'{self.nome} está comendo, logo não pode falar')

        print(f'{self.nome}', 'começou a falar')
        self.falando = True

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade