# OBS: a temperatura em fahrenheit estava com formula errada.
temp = float(input("Digite uma temperatura em graus Celsius: "))

def temperatura(temp):
    Far = (9*temp/5) + 32
    print(f"A temperatura em graus Fahrenheit é de {Far}F°")

temperatura(temp)
