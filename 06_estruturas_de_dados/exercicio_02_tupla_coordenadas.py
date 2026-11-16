"""
EXERCÍCIO 02: Tupla de Coordenadas e Imutabilidade
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma tupla com as cidades ("Tianguá", "São Benedito").
Tente alterar a posição 1 e use try-except para capturar o TypeError,
exibindo uma mensagem explicativa sobre imutabilidade.
"""

# TODO: Desenvolva o algoritmo abaixo:
cidades=("Tianguá, São Benedito")

try:
    cidades[1] = "Ubajara"
except TypeError:
    print("Erro de mutabilidade. Tuplas são imutáveis, sem a possibilidade de alterar seus elementos")