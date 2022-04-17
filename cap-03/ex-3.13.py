''' Escreva um programa que converta uma tempreratura digitada em °C em °F. A fórmula para essa conversão é: F = ((9xC)/5)+32'''

print("Este programa faz a conversão da temperatura em °C para F")
temp_C = float(input("Digite o valor da temperatura na escala graus Celcius: "))

#Fórmula de conversão
temp_F = 9*temp_C/5 + 32

print(f"A temperatura fornecida em graus Celcius foi {temp_C}°C. Essa temperatura em Fahrenheit é {temp_F} F. ")