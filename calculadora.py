numero1 = float(input("Digite o primeiro numero: "))
operador = input("Digite a operação: ")
numero2 = float(input("Digite o segundo numero: "))
try:
    while True:
        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*":
            resultado = numero1 * numero2
        elif operador == "/":
            resultado = numero1 / numero2
        else:
            ("Operador invalido." + operador)
    