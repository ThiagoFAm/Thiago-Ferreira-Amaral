produto = input(str("Digite o Nome produto: "))
categoria = input(str("Digite a categoria do produto: "))
qt_Estoque = int(input("Digite a Q° no Estoque: "))

alimentos = ["Arroz", "feijão", "macarrão", "açúca", "café","carne"]

bebidas = ["guaraná", "coca-cola","magistral", "real", "pepsi"]

limpeza = ["desinfetante", "água sanitária", "sabão em pó"]

if (produto in alimentos) and (categoria == "alimentos") and (qt_Estoque >= 50):
    print(f"Temos {produto} suficiente, no estoque temos {qt_Estoque} unidades")

elif (produto in bebidas) and (categoria == "bebidas") and (qt_Estoque >= 60):
    print(f"Temos {produto} suficiente, no estoque temos {qt_Estoque} unidades")

elif (produto in limpeza) and (categoria == "limpeza") and (qt_Estoque >= 30):
    print(f"Temos {produto} suficiente, no estoque temos {qt_Estoque} unidades")

elif (qt_Estoque < 50):
    print(f"Solicitar {produto} à equipe de compras, temos apenas {qt_Estoque} em estoque")

elif produto == "" or categoria == "" or qt_Estoque == "":
    print("Você não respondeu alguma pergunta!")
    
