class Pessoa:
    def __init__(self, idade=34):
        self.idade = 34
        self.nome = None
    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('José')
    print(Pessoa.comprimentar(p))
    print(id(p))
    print(p.comprimentar())
    print(p.nome)
    p.nome = 'Victor'
    print(p.nome)
    print(p.idade)