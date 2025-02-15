"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes

1)  Motor
2)  Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1)  Atributo de dado velocidade
2)  Metodo Acelerare, que devera incrementar a velodade de uma unidade
3)  Metodo frear que defera decrementar a velocidade em duas unidades

A Direção terá a responsaibilidade de controlar a direção. Ela oferece os seguintes atributos:
1)  Valor de direção com valores possiveis: Norte, sul, Leste Oeste.
2)  Metodo girar_a_direita
3)  Metodo girar_a_esquerda

    N
O       L
    S


    Exemplo
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'NORTE'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'LESTE'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'SUL'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'OESTE'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'NORTE'
    >>> direcao.virar_a_esquerda()
    >>> direcao.valor
    'OESTE'
    >>> direcao.virar_a_esquerda()
    >>> direcao.valor
    'SUL'
    >>> direcao.virar_a_esquerda()
    >>> direcao.valor
    'LESTE'
    >>> direcao.virar_a_esquerda()
    >>> direcao.valor
    'NORTE'
    >>> direcao.virar_a_esquerda()
    >>> direcao.valor
    'OESTE'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'NORTE'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'OESTE'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'OESTE'



"""

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_esquerda(self):
        direcao = self.direcao.virar_a_esquerda

    def girar_a_direita(self):
        direcao = self.direcao.virar_a_direita

NORTE  ='NORTE'
SUL = 'SUL'
LESTE = 'LESTE'
OESTE = 'OESTE'

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def virar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def virar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)



