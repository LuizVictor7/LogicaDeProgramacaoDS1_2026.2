"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia= input("Digite a distância total percorrida (em Km): ")
combustivel= input("Digite o total de combustível gasto na viagem (Em Litros): ")
combustivel = float(combustivel)
distancia = float(distancia)
consumo_medio = distancia/combustivel
print(f"O consumo médio da motocicleta é: {consumo_medio:.2f} Km/L")
