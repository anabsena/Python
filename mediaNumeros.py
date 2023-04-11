def calcular_media(lista_numeros):
    media = sum(lista_numeros) / len(lista_numeros)
    return media

numeros = [10, 20, 30, 40, 50]
media_calculada = calcular_media(numeros)

print(f"A média dos números {numeros} é {media_calculada:.2f}")
