"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_investido=float(input("Digite o valor Investido na campanha:"))
numero_cliques=int(input("Digite o número total de Cliques obtidos durante a campanha:"))
CPC= valor_investido/numero_cliques
print("O Custo por Clique médio gerado durante a campanha foi",CPC,)
