class Pessoa:
    def __init__(self, idade=34, nome=None, *filhos):
        self.idade = 34
        self.nome = None
        self.filhos= list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    jose = Pessoa(nome='José')
    victor = Pessoa(jose, nome='Victor')
    print(Pessoa.comprimentar(jose))
    print(Pessoa.comprimentar(victor))
    print(id(jose))
    print(id(victor))
    print(victor.nome)
    print(jose.idade)
    print(victor.filhos)
    for filho in victor.filhos:
        print(filho.nome)
    jose.sobrenome = 'Almeida'
    print(jose.sobrenome)
    print(jose.__dict__)
    print(victor.__dict__)

