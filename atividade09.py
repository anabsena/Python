# Crie uma classe chamada ContaBancaria com os atributos titular e saldo. A classe deve ter dois métodos: depositar(valor) para adicionar um valor ao saldo e sacar(valor) para subtrair um valor do saldo.
# A partir da classe ContaBancaria, crie duas subclasses: ContaPoupanca e ContaCorrente. Para a classe ContaPoupanca, sobrescreva o método sacar(valor) de modo que, a cada saque, seja descontada uma taxa de R$ 2.
# Para a classe ContaCorrente, adicione um atributo limite e sobrescreva o método sacar(valor) de modo que o saque possa ser realizado mesmo que o saldo seja insuficiente, desde que não ultrapasse o limite definido.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        if self.saldo >= valor + taxa:
            self.saldo -= valor + taxa
            return True
        else:
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        else:
            return False
conta_poupanca = ContaPoupanca("João", 100)
conta_corrente = ContaCorrente("Maria", 200, 100)

conta_poupanca.depositar(50)
conta_corrente.depositar(80)

print("Saldo da conta poupança:", conta_poupanca.saldo)
print("Saldo da conta corrente:", conta_corrente.saldo)

saque_poupanca = conta_poupanca.sacar(30)
saque_corrente = conta_corrente.sacar(250)

print("Saque da conta poupança:", saque_poupanca)
print("Saque da conta corrente:", saque_corrente)

print("Saldo da conta poupança após saque:", conta_poupanca.saldo)
print("Saldo da conta corrente após saque:", conta_corrente.saldo)
