'''Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos
anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante perderá.
Exiba o total de dias.'''

print("Exte programa calcula o tempo de redução de vida de um fumante.")

quantidade_de_cigarros = float(input("Qual a quantidade de cigarros fumados por dia? "))
tempo_fumante = float(input("Tem quanto anos que você é fumante? "))

quantidade_total_cigarros = quantidade_de_cigarros * tempo_fumante * 365 # Quantidade total de cigarros fumados
tempo_reduzido = quantidade_total_cigarros*0.00694444

print(f"O total de dias que serão perdidos devido ao uso do cigarro é de {round((tempo_reduzido),2)} dias.")