# Crie uma classe chamada Produto com os atributos nome e preco. A classe deve ter um método chamado desconto que aplica um desconto percentual ao preço do produto e retorna o preço com desconto. A partir da classe Produto, crie duas subclasses: Livro e Jogo.
# Para a classe Livro, adicione o atributo autor e sobrescreva o método desconto para aplicar um desconto adicional de 10% (além do desconto geral do produto).
# Para a classe Jogo, adicione o atributo plataforma (por exemplo, 'PC', 'PS5', etc.) e não modifique o método desconto.
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto_valor = self.preco * (percentual / 100)
        preco_com_desconto = self.preco - desconto_valor
        return preco_com_desconto

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def desconto(self, percentual):
        desconto_geral = super().desconto(percentual)
        desconto_autor = desconto_geral * 0.10  # 10% de desconto adicional
        preco_com_desconto = desconto_geral - desconto_autor
        return preco_com_desconto

class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma

# Exemplo de uso
produto_generico = Produto("Produto Genérico", 100)
livro = Livro("Aprendendo Python", 50, "John Smith")
jogo = Jogo("The Witcher 3", 120, "PS5")

desconto_produto_generico = produto_generico.desconto(20)
desconto_livro = livro.desconto(15)
preco_jogo = jogo.preco  # Não aplicamos desconto em jogos

print(f"Preço com desconto do produto genérico: R${desconto_produto_generico:.2f}")
print(f"Preço com desconto do livro: R${desconto_livro:.2f}")
print(f"Preço do jogo: R${preco_jogo:.2f}")
