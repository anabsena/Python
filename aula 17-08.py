# ATIVIDADE 01
# Desenvolva três exemplos de códigos em Python (.py), demonstrando diferentes tipos de funções. Crie uma função sem parâmetros e sem retorno, outra função com parâmetros e sem retorno, e uma terceira função com parâmetros e retorno. Seja criativo e explore a versatilidade das funções em Python. Certifique-se de fornecer comentários explicativos em seu código para facilitar a compreensão

# def limpa_tela():
#     import os
#     os.system("cls")
# sem retorno e sem parametro
# limpa_tela()
# print("aloou")


# def limpa_tela_soma(n1, n2):
#     import os
#     os.system("cls")
#     print(n1+n2)
# com parametro e sem return
# limpa_tela_soma(2,3)

# def limpa_tela_soma(n1, n2):
#     import os
#     os.system("cls")
#     return n1+n2
# result = limpa_tela_soma(2,3)
# print(result)
#   ATIVIDADE 02


# class SistemaOperacional:
#     def __init__(self, nome, versao):
#         self.nome = nome
#         self.versao = versao

# class Computador:
#     def __init__(self, sistema):
#         self.sistema = sistema

# sistema_windows = SistemaOperacional(nome="Windows", versao="10")
# meu_computador = Computador(sistema=sistema_windows)

# print(f"Meu computador está usando o sistema operacional {meu_computador.sistema.nome} versão {meu_computador.sistema.versao}")

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

# print(f"Meu computador está usando o sistema operacional {meu_computador.sistema.nome} versão {meu_computador.sistema.versao}")