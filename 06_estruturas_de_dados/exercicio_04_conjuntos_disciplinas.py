"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos_web= {"Carlos","Vivian","Savio","Bruno","Jorge","Davi","Clara","Samuel"}
alunos_banco= {"Jorge","Savio","Clara","Witalo","Angella","Samuel"}
inter= alunos_banco & alunos_web
dif= alunos_web - alunos_banco
print(f"A interseção de alunos Web e Banco são {inter}")
print(f"A diferença de alunos apenas em Web, mas não em Banco é {dif}")