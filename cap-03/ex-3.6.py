''' Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem 
ser maiores que 7. Cosidere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: materia1,
materia2 e materia3'''

# Pelo enunciado:
materia1 > 7 and materia2 > 7 and materia3 > 7

# Na prática, o aluno é aprovado se obtiver nota maior ou igual a média, logo:
materia1 >= 7 and materia2 >= 7 and materia3 >= 7