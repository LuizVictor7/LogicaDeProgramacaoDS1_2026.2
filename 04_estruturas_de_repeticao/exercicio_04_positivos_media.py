"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
contadorPositivo = 0
lista_numeropositivos = list()
soma_positivos = 0.0
for n in range(6):
    numero = float(input("Digite um valor: "))
    if numero > 0:
        contadorPositivo += 1
        lista_numeropositivos.append(numero)
        media=  soma_positivos /contadorPositivo
print (f"a média dos valores positivos é {media:.1f} e a quantidade de números positivos é {contadorPositivo}")