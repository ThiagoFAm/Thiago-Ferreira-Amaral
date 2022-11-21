#Lista para que o for execute o programa 3 vezes.
#Constantes
codigo = ['f0', 'f1', 'f2'] #Lista
reajuste1 = int(10)
meta = int(1000)

for codigo in ['f0', 'f1', 'f2']:
        
    #informações do funcionário
    nome = input(str("nome do funionário: ")).strip()
    salario_fx = int(input("Salário fixo do funcionário: "))
    valor_vendas = int(input("Valor em vendas : "))
    
    #Operação com variaveis e constantes para que assim resulte um novo salário
    novo_salario = salario_fx + (valor_vendas * reajuste1)/100
    
    print("===================================") #Apenas para organizar.
    
    #Se funcionário bater a meta ou for superior a meta, funcionário recebe promoção de 10%
    if valor_vendas >= meta:
       
        print(f"Parabens {nome}! Você atingiu a meta!")
        print(f"Você recebeu um bônus de 10%\nBônus = {novo_salario}")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") #Apenas para organizar.
    
    #Se funcionário não atingir a meta. Exiba
    else:
    
        print(f"{nome}, infelizmente você não atingiu a meta\nNão há bônus algum para você!")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") #Apenas para organizar.