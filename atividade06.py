#Definir o conceito de composição.
# Criar dois exemplos práticos usando Python que demonstrem a aplicação da composição.
# Composição é um dos princípios fundamentais da programação orientada a objetos (POO), onde um objeto é construído a partir de outros objetos, combinando suas funcionalidades para formar um novo objeto mais complexo. Isso permite criar estruturas mais flexíveis e modulares, onde as partes individuais podem ser reutilizadas em diferentes contextos.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}")

livro1 = Livro("Aprendendo Python", "John Smith")
livro2 = Livro("Introdução à POO", "Jane Doe")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
produto1 = Produto("Camiseta", 25)
produto2 = Produto("Calça", 40)

pedido = Pedido()
pedido.adicionar_produto(produto1)
pedido.adicionar_produto(produto2)

total_pedido = pedido.calcular_total()
print(f"Total do pedido: R${total_pedido:.2f}")