"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    litro = distancia_km / consumo_kml
    custo_transporte = litro * preco_combustivel
    return custo_transporte
def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo_alimentacao = qtd_pessoas * dias * diaria_alimentacao
    return custo_alimentacao

distancia_km = float(input("Digite a distância da viagem em km: "))
consumo_kml = float(input("Digite o consumo do veículo em km/l: "))
preco_combustivel = float(input("Digite o preço do combustível por litro: "))
qtd_pessoas = int(input("Digite a quantidade de pessoas da viagem: "))
dias = int(input("Digite a duração em dias da viagem: "))
diaria_alimentacao = float(input("Digite o valor da diária de alimentação: "))
total_viagem = calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel) + calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)

print(f"Custo total do transporte: R$ {calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):.2f}")
print(f"Custo total da alimentação: R$ {calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):.2f}")
print(f"Custo total da viagem: R$ {total_viagem:.2f}")