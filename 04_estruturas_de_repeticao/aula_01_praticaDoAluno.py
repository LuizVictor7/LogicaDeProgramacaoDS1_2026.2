# TODO: Implemente a tabuada aqui
numero = int(input("Digite um número para ver a tabuada: "))

# Escreva o laço for
for n in range(1,11):
    resultado = numero * n
    print(f"a Tabuada do {numero} x {n} é:")
    print (f"{resultado}")
    print("Fim da Tabuada.")