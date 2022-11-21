qt_hospedes = int(input("Digite a quantidade de hóspedes: "))
quarto = []

if qt_hospedes <= 4:
    for pessoas in range(qt_hospedes):
        nome = input(str("Digite o nome do hóspede: "))
       
        c = int(input("Digite seu CPF: "))
        hospedes = ["Nome: {}".format(nome), "CPF: {}".format(c)]
        quarto.append(hospedes)
        print(quarto) 
else:
    print("Erro! nossos quartos só suportam ate 4 pessoas.")    
