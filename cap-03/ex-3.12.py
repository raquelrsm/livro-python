'''Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem'''

print("Exxe programa irá fornecer o tempo de viagem")
distancia = float(input("Digite qual a distância a ser percorrida em km: "))
velocidade_media = float(input("Digite o valor da velocidade média em km/h: "))

tempo = distancia / velocidade_media

print(f"O valor da distância percorrida foi de {distancia} e a velocidade média do percurso foi de {velocidade_media}. O tempo gasto durante o percurso será de {tempo} horas. ")