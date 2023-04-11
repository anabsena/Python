velocidade_media = float(input("Digite a velocidade média durante a viagem: "))
tempo_gasto = float(input("Digite o tempo gasto durante a viagem: "))

def distancia(velocidade_media, tempo_gasto):
    return velocidade_media * tempo_gasto

def litros(distancia):
    return distancia / 12

def resultados(velocidade_media, tempo_gasto):
    dist = distancia(velocidade_media, tempo_gasto)
    litros_usados = litros(dist)
    print(f"A velocidade média foi: {velocidade_media} km/h, o tempo gasto foi: {tempo_gasto} horas, a distância percorrida foi: {dist} km e foram gastos {litros_usados:.2f} litros de combustível.")

resultados(velocidade_media, tempo_gasto)
