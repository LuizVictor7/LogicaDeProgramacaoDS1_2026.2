# TODO: Desenvolva seu algoritmo aqui
# Mão na massa
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valor_da_conta=input("Digite o valor da conta:")
valor_da_conta= float(valor_da_conta)
quantidade_pessoas_mesa=input("Qual a quantidade de pessoas na mesa?")
quantidade_pessoas_mesa=int(quantidade_pessoas_mesa)
valor_final= valor_da_conta / quantidade_pessoas_mesa
valor_final= str(valor_final)
print(f"O valor total é",valor_da_conta,"e cada pessoa irá pagar", valor_final, "de forma igualmente")