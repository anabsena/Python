# import os
# carros = ("Fusca", "Verona", "Gol")
# nome = "Ana "
# os.system("cls") #Limpa terminal
# print(type(carros))
# for tuplas in carros:
#     print(tuplas)
#     print("--------------------------------------")
# for letra in nome:
#     print(letra)
# lista1 = 
# listaCompras = ("arroz", "Feijão", "banana")
# for tuplas in listaCompras:
#     print(listaCompras)
#     print("--------------------------------------")
lista_de_compras = []
def mostrar_lista_de_compras():
    if len(lista_de_compras) == 0:
        print("Sua lista de compras está vazia!")
    else:
        print("Sua lista de compras:")
        for item in lista_de_compras:
            print("- " + item)
def adicionar_item():
    item = input("Digite o item que deseja adicionar: ")
    lista_de_compras.append(item)
    print(item + " foi adicionado à sua lista de compras.")
def editar_item():
    mostrar_lista_de_compras()
    indice = int(input("Digite o número do item que deseja editar: "))
    novo_item = input("Digite o novo valor para o item: ")
    lista_de_compras[indice-1] = novo_item
    print("O item " + str(indice) + " foi atualizado para " + novo_item + ".")
def remover_item():
    mostrar_lista_de_compras()
    indice = int(input("Digite o número do item que deseja remover: "))
    item_removido = lista_de_compras.pop(indice-1)
    print(item_removido + " foi removido da sua lista de compras.")
def menu():
    while True:
        print("\nMENU:")
        print("1 - Mostrar lista de compras")
        print("2 - Adicionar item à lista")
        print("3 - Editar item da lista")
        print("4 - Remover item da lista")
        print("5 - Sair do programa")
        opcao = int(input("Digite o número da opção desejada: "))
        if opcao == 1:
            mostrar_lista_de_compras()
        elif opcao == 2:
            adicionar_item()
        elif opcao == 3:
            editar_item()
        elif opcao == 4:
            remover_item()
        elif opcao == 5:
            print("Obrigado por usar o programa!")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()