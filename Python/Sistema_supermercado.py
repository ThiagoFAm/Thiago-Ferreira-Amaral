produtos = []
qtde_total = []
produto_qt = []
produto = "i"

while produto != "":
    print("SISTEMA DE SUPERMERCADO")
    produto = input("Digite o nome do produto: ")
    qtde = (input("Digite quantidade"))
    produto_qt.append(f"Produto: {produto} || quantidade vendida: {qtde}")
    
print(produto_qt)