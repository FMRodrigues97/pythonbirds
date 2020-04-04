class Pessoa:
    def __init__(self, *filhos, nome=None, idade=23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    fernando = Pessoa(nome='Fernando')
    alessandra = Pessoa(fernando, nome='Alessandra')
    print (Pessoa.cumprimentar(alessandra))
    print (id(alessandra))
    print (alessandra.cumprimentar())
    print (alessandra.nome)
    print(alessandra.idade)
    for filho in alessandra.filhos:
        print(filho.nome)
    alessandra.sobrenome = 'Moraes'
    del alessandra.filhos
    print(alessandra.__dict__)
    print(fernando.__dict__)