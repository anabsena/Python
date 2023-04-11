lista={}
somanotas = 0
for i in range(3):
    nome = input("digite o nome do aluno: ")
    nota = int(input("digite a nota do aluno: "))
    lista[nome] = nota
    
for nota in lista.values():
    somanotas +=nota

media = somanotas/len(lista)
print(f'media : {media}')