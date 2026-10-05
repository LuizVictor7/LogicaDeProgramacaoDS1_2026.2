"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
cont_positivo = 0
soma_positivo = 0
for n in range(6):
    numero = float(input("Digite um valor: "))
    if numero > 0:
        cont_positivo += 1
        soma_positivo += numero
if cont_positivo > 0:
    media = soma_positivo / cont_positivo
    print(f"{cont_positivo} valores positivos")
    print(f"A média dos números positivos é: {media:.1f}")
else:
    print("Nenhum valor positivo foi digitado.")