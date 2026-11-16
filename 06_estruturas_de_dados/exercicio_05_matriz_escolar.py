"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
matriz= [
    ["Jorge", 10,10],
    ["Davi", 8.0, 6.8],
    ["Witalo", 7.8,7.5]
]

for n in matriz:
    aluno = n[0]
    n1= n[1]
    n2= n[2]
    media= (n1+n2)/2
    if media >= 6.0:
        status = "aprovado"
    else:
        status = "reprovado"
    print(f"O aluno {aluno} está com a média {media} e está {status}")