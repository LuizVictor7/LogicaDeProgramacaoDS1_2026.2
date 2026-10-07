"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
fase1= float(input("Digite a pontuação da fase 1: "))
fase2= float(input("Digite a pontuação da fase 2: "))
fase3= float(input("Digite a pontuação da fase 3: "))

def calcular_pontuacao_total(fase1, fase2, fase3):
    # vai somar as pontuações das três fases e retornar o total
    pontuacao_total= fase1 + fase2 + fase3
    return pontuacao_total

print(f"A pontuação total da equipe Astro Lume Devs é: {calcular_pontuacao_total(fase1, fase2, fase3):.2f}")