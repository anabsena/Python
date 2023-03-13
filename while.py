sistema = True

while sistema:
    nome = input ('Escreva seu nome: ')
    print(f"O nome recebido foi: {nome}")

    if nome == "sair":
        print("Finalizou o sistema")
        break
        