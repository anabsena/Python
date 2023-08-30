# Você deve criar uma hierarquia de classes para representar uma biblioteca. Inicie com uma classe base chamada Publicacao que tem atributos para titulo e ano_publicacao. A partir da classe Publicacao, derive duas subclasses: Livro e Revista.
# Para a classe Livro, adicione os atributos autor e numero_paginas.
# Para a classe Revista, adicione os atributos editora e edicao.
# Ambas as subclasses devem ter um método descricao que retorna uma string descrevendo a publicação (título, ano, autor/editora e outros detalhes relevantes).
class Publicacao:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def descricao(self):
        return f"Título: {self.titulo}, Ano de Publicação: {self.ano_publicacao}"

class Livro(Publicacao):
    def __init__(self, titulo, ano_publicacao, autor, numero_paginas):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor
        self.numero_paginas = numero_paginas

    def descricao(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Número de Páginas: {self.numero_paginas}"

class Revista(Publicacao):
    def __init__(self, titulo, ano_publicacao, editora, edicao):
        super().__init__(titulo, ano_publicacao)
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"Título: {self.titulo}, Editora: {self.editora}, Ano de Publicação: {self.ano_publicacao}, Edição: {self.edicao}"

livro = Livro("Aprendendo Python", 2023, "John Smith", 300)
revista = Revista("Tech Magazine", 2023, "Tech Publishing", "Vol. 1, Edição 3")

print(livro.descricao())
print(revista.descricao())
