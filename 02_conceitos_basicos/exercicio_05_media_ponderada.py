"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
n1= float(("Digite a primeira nota"))
n2= float(("Digite a segunda nota"))
n3 = float(("Digite a terceira nota"))
media_ponderada = (n1*2 + n2*3 + n3*5)/(2+3+5)
print = (f"A média ponderada final das três avaliações do curso técnico: {media_ponderada:.2f}")