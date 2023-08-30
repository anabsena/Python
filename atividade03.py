# Desenvolva duas classes: Computador e SistemaOperacional.A classe SistemaOperacional deve possuir os atributos: nome (ex: Windows, Linux, MacOS) e versao.A classe Computador deve possuir um atributo chamado sistema, que será uma instância da classe SistemaOperacional
class SistemaOperacional:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao

class Computador:
    def __init__(self, sistema):
        self.sistema = sistema

sistema_windows = SistemaOperacional(nome="Windows", versao="10")
meu_computador = Computador(sistema=sistema_windows)

print(f"Meu computador está usando o sistema operacional {meu_computador.sistema.nome} versão {meu_computador.sistema.versao}")