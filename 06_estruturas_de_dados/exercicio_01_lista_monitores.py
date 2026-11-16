"""
EXERCÍCIO 01: Lista de Monitores
Disciplina: Lógica de Programação com Python

ENUNCIADO:
1. Crie uma lista com o primeiro monitor: "Ryan Mesquita Damasceno".
2. Adicione 2 novos monitores com .append().
3. Demonstre a mutabilidade alterando o nome na posição 0.
4. Imprima a lista final.
"""

# TODO: Desenvolva o algoritmo abaixo:
list =["Ryan Mesquita Damasceno"]
for n in range(2):
    monitor= str(input("Digite o nome do novo monitor: "))
    list.append(monitor)
list[2]="Ryan Mesquita Damasceno"
list[0]=monitor
print(list)