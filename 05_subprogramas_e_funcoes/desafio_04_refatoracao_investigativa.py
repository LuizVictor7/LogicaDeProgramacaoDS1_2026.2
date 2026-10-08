"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    preco_final = preco_base - taxa_desc + taxa_imp
    return preco_final
preco_base = float(input("Digite o preço base do produto: "))
taxa_desc = float(input("Digite o desconto: "))
taxa_imp = float(input("Digite o imposto: "))
print (f"O preço final do produto é {calcular_preco_final(preco_base, taxa_desc, taxa_imp)}")
numero_item = int(input("Digite o número de item:"))
print (f"O produto de codigo {numero_item}, valor R$ {calcular_preco_final(preco_base, taxa_desc, taxa_imp)}")