"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
X = int(input("Digite o primeiro valor "))
Y = int(input("Digite o segundo valor "))
minimo = min(X, Y)
maximo = max(X, Y)
print(f"Os números com o resto da divisão por 5 sendo igual 2 ou 3 do intervalo entre {X} e {Y} é: ")
for n in range (minimo, maximo + 1):
    if n % 5 == 2 or n % 5 == 3:
        print (n)