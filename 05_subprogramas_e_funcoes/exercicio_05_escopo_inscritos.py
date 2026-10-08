"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
total_inscritos = 0
def inscrever_aluno (quantidade):
    total_inscritos = 1
    return total_inscritos * quantidade
quantidade = int(input("Digite os números de inscritos: "))
print (f"A quantidade de alunos inscritos antes da chamada é {total_inscritos}")
print (f"A quantidade de alunos inscritos depois da chamada é {inscrever_aluno(quantidade)}")

