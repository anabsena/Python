# Crie duas classes: Autor e Livro.
# A classe Autor deve possuir os atributos: nome e data_nascimento.
# A classe Livro deve ter os atributos: titulo e autor, onde autor será uma instância da classe Autor
class autor1:
    def __init__(self, autor, data_nasc):
        self.autor = autor
        self.data_nasc = data_nasc
class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

autor_livro = autor(nome="ana", data_nasc="2004.07.14")
meu_livro = livro(titulo="biografia", autor1(autor=autor)