numero1 = float(input("Digite o primeiro numero: "))
operador = input("Digite a operação: ")
numero2 = float(input("Digite o segundo numero: "))
while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        numero2 = float(input("Digite o segundo número: "))
        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*" or operador.lower() == 'x':
            resultado = numero1 * numero2
        elif operador == "/":
            resultado = numero1 / numero2
        else:
            print("Operador inválido:", operador)
            continue
        print(f"{numero1}, {operador}, {numero2}, = {resultado}")
        sair = input("Deseja sair (s/n)? ").lower().startswith('s')
        if sair:
            break
    except ValueError:
        print("Entrada inválida, tente novamente.")