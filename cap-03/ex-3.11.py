'''Faça um programa um programa que solicite o preço de uma mercadoria e o percentual de desconto e o preço a pagar'''

print("Esse programa irá exibir o preço atual da mercadoria, o desconto concedido e o preço a ser pago")

valor_mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Qual será o valor de desconto concedido: "))

valor_desconto = desconto * valor_mercadoria / 100
novo_valor_mercadoria = valor_mercadoria - valor_desconto

print(f"O valor da mercadoria era de: {valor_mercadoria}. O valor do desconto concedido foi {valor_desconto} e o valor da mercadoria após o desconto foi de {novo_valor_mercadoria}")
