# TODO: Implemente o carrinho de compras
carrinho_compras = []

# Adicione 3 produtos e ordene a lista
for n in range(3):
    produto= str(input(f"Digite o nome do {n+1} produto: "))
    carrinho_compras.append(produto)
carrinho_compras.sort()
print(f"A lista de compra é:")
print(carrinho_compras)