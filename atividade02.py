#02
class Estudante:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def nomeIdade(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


aluno1 = Estudante("Ana", 19)
aluno2 = Estudante("Beatriz", 19)
aluno3 = Estudante("Guilherme", 21)

aluno1.nomeIdade()
aluno2.nomeIdade()
aluno3.nomeIdade()