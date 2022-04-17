'''Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado pelo usuário, assim como a quantidade de dias
pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado.'''

print("O programa fornece o valor a ser pago pelo aluguel do carro (Diária + km rodado")

aluguel_dias = float(input("Quantidade de dias que o carro foi alugado: "))
km_rodados = float(input("Quantos foram os quilomentos rodados com o carro: "))

valor_diaria = aluguel_dias*60 + km_rodados*0.15

print(f"Sendo {aluguel_dias} o total de dias de aluguel do carro e {km_rodados} a quantidade de quilômetros rodados o valor a pagar será de {valor_diaria}.")