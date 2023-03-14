numero1 = float(input("Digite o primeiro numero: "))
operador = input("Digite a operação: ")
numero2 = float(input("Digite o segundo numero: "))
try:
    while True:
        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*" or operador.lower() == 'x':
            resultado = numero1 * numero2
        elif operador == "/":
            resultado = numero1 / numero2
        else:
            print("Operador invalido." + operador)
        print("f{numero1} {operador} {numero2} = {resultado}")
        sair = input("Deseja sair: ").lower.startswith('s')
        if sair:
            break
except:
    print("Numero invalido.")