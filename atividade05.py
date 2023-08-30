# Elabore duas classes: Carro e Motor.
# A classe Motor deve ter os atributos: tipo (ex: Gasolina, Diesel, Elétrico) e potencia (em cavalos).
# A classe Carro deve possuir um atributo chamado motor, que será uma instância da classe Motor.
class Motor:
    def __init__(self, combustivel, potencia):
        self.combustivel = combustivel
        self.pontencia = potencia
class carro:
    def __init__(self, motor)
    self.motor = motor
motor_gasolina = Motor("Gasolina", 150)
carro_gasolina = Carro(motor_gasolina)

motor_eletrico = Motor("Elétrico", 200)
carro_eletrico = Carro(motor_eletrico)
