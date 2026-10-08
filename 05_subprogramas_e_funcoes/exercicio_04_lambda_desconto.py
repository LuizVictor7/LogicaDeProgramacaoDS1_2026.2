"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
aumento_valor = lambda v: v * 0.85
v = float(input("Digite o valor do produto: "))
print (f"O valor do produto com desconto de 15% é {aumento_valor(v)}")