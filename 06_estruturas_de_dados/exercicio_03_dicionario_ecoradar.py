"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:
ecoradar= {"1": "Analista de Dados","2": "Dev","3": "Administração"}
for n in ecoradar:
    sla= input("Digite um numero de matricula: ")
    cargo = ecoradar.get(sla)
    if cargo:
        print(cargo )
    else:
        print("Nada")
print("Fim do Dicionario")