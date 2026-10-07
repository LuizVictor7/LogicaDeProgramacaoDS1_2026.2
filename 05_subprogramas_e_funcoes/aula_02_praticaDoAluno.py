# TODO: Crie a função lambda aqui
calcular_acrescimo = lambda valor: valor * 1.10

# Teste
valor = float(input("Digite um valor: "))
print(f"O acrescimo do valor {valor} em 10% é: {calcular_acrescimo(valor):.2f}")