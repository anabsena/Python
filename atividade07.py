# Crie uma classe chamada Documento que tenha os atributos titulo e conteudo e um método exibir que retorna uma representação do documento no formato: "Título: [título], Conteúdo: [conteúdo]". A partir dessa classe, crie duas subclasses: Email e Relatorio.

# Para a classe Email, adicione os atributos remetente e destinatario, e sobrescreva o método exibir para incluir essas informações adicionais.

# Para a classe Relatorio, adicione um atributo data e também sobrescreva o método exibir para exibir essa informação.
class documento:
    def __init__ (self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"
class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}, Data: {self.data}"

documento_generico = Documento("Documento Genérico", "Este é um documento de exemplo.")

email = Email("Convite", "Você está convidado para o evento!", "remetente@example.com", "destinatario@example.com")

relatorio = Relatorio("Relatório Mensal", "Este é o relatório de vendas.", "01/08/2023")

print(documento_generico.exibir())
print(email.exibir())
print(relatorio.exibir())





