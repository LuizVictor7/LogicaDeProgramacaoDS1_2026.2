"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
def emitir_alerta_fatura(nome_cliente, valor, data_vencimento):
    return (f"Prezado(a) {nome_cliente}, sua fatura da Cagece no valor de R$ {valor} vence no dia {data_vencimento}")
nome_cliente = str(input("Digite o nome do cliente: "))
valor = float(input("Digite o valor da fatura: "))
data_vencimento = (input("Digite a data de vencimento: "))
print(emitir_alerta_fatura(nome_cliente, valor, data_vencimento))