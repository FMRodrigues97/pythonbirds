class Pessoa:
    olhos = 2 #Atributo default ou atributo de classe

    def __init__(self, *filhos, nome=None, idade=23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    alessandra.olhos = 1
    del alessandra.olhos #Apaga o atributo do objeto, e não da classe!
    print(alessandra.__dict__)
    print(fernando.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(fernando.olhos)
    print(alessandra.olhos)
    print(id(Pessoa.olhos), id(fernando.olhos), id(alessandra.olhos))
    print(Pessoa.metodo_estatico(), alessandra.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), alessandra.nome_e_atributos_de_classe())
