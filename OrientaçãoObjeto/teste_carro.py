from unittest import TestCase
from OrientaçãoObjeto.carro import Motor

class CarroTestCase(TestCase):
    def teste_de_velocidade_inicial(self):
        motor = Motor()
        self.assertSetEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertSetEqual(1, motor.velocidade)