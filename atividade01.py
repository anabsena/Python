# Desenvolva três exemplos de códigos em Python (.py), demonstrando diferentes tipos de funções. Crie uma função sem parâmetros e sem retorno, outra função com parâmetros e sem retorno, e uma terceira função com parâmetros e retorno. Seja criativo e explore a versatilidade das funções em Python. Certifique-se de fornecer comentários explicativos em seu código para facilitar a compreensão

def limpa_tela():
    import os
    os.system("cls")
sem retorno e sem parametro
limpa_tela()
print("aloou")


def limpa_tela_soma(n1, n2):
    import os
    os.system("cls")
    print(n1+n2)
com parametro e sem return
limpa_tela_soma(2,3)

def limpa_tela_soma(n1, n2):
    import os
    os.system("cls")
    return n1+n2
result = limpa_tela_soma(2,3)
print(result)