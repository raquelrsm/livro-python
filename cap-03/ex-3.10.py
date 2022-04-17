'''Faça um programa que calcule o aumento de salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário'''

print("Esse programa irá exibir o valor do aumento e o valor do novo salário")
salario = float(input("Digite o valor atual do salário: "))
aumento = float(input("Digite o valor da  porcentagem de aumento condecidido: "))

valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento

print(f"O valor do novo salário é {novo_salario} e o aumento concedido foi de {valor_aumento}")