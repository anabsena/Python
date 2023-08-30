class Veiculo:
    def __init__(self, cor, preco):
        self.cor = cor
        self.preco = preco

    def detalhes(self):
        return f"Cor: {self.cor}, Preço: {self.preco}"

class Carro(Veiculo):
    def __init__(self, cor, preco, numero_portas):
        super().__init__(cor, preco)
        self.numero_portas = numero_portas

    def detalhes(self):
        return f"Tipo: Carro, Cor: {self.cor}, Preço: {self.preco}, Número de Portas: {self.numero_portas}"

class Bicicleta(Veiculo):
    def __init__(self, cor, preco, tipo):
        super().__init__(cor, preco)
        self.tipo = tipo

    def detalhes(self):
        return f"Tipo: Bicicleta, Cor: {self.cor}, Preço: {self.preco}, Tipo: {self.tipo}"

# Exemplo de uso
carro = Carro("Azul", 25000, 4)
bicicleta = Bicicleta("Vermelha", 800, "Montanha")

print(carro.detalhes())
print(bicicleta.detalhes())
