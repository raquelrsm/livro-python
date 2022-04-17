'''Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos'''
print("Quantos segundos tem? Informe uma determinada hora para saber quantos segundos tem.")
hora = int(input("Digite qual a hora: "))
minuto = int(input("Digite quantos minutos: "))
segundos = int(input("Digite quantos segundos: 4"))

hora = hora*3600
minuto = minuto*60

total_segundos = hora + minuto + segundos

print(f"O total de segundos é: {total_segundos}")