class Pessoa:
    def __init__(self, idade=34, nome=None, *filhos, email='@python.com', olhos = 2):
        self.idade = 34
        self.nome = None
        self.filhos= list(filhos)
        self.email = email
        self.olhos = 2

    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_sobrenome_de_classe(cls):
        return f'{cls} - olhos'


if __name__ == '__main__':
    jose = Pessoa(nome='José')
    victor = Pessoa(jose, nome='Victor')
#    email = '@python.com'
    emailjose = jose.email
    emailvictor = victor.email
    print(jose.email)
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
    del jose.olhos
    print(jose.sobrenome,emailjose)
    print(jose.__dict__)
    print(victor.__dict__)
    print(Pessoa.metodo_estatico())




