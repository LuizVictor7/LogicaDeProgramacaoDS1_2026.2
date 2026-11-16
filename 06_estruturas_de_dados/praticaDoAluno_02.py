# TODO: Crie a matriz 2x2 e calcule a soma
matriz = [
    [0, 0],
    [0, 0]
]

# Escreva a lógica de soma aqui
for i in range(2):
    for n in range(2):
        num= int(input("Digite um número: "))
        matriz[i][n]= num
# print (matriz)
sla=0
for linha in matriz:
    s1= linha[0]
    s2= linha[1]
    sla += s1+s2
print(f"A soma da matriz 2x2({matriz}) é:")
print (sla)