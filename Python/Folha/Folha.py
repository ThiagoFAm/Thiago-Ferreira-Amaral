
#importação de bibliotecas    

import re
import os
import requests
from bs4 import BeautifulSoup


#pegando valor de salario na WEB


url = "http://www.guiatrabalhista.com.br/guia/salario_minimo.htm"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers = headers)

soup = BeautifulSoup(site.content, 'html.parser')

salario = soup.find('span', style="font-size: 12pt; text-align: justify;")


a = (salario.string)

b = a

b = re.sub('[^0-9]', '', b)

c = b.split('0')


#funções diversas


def tela1():
    print("#" * 71)
    print("#" * 71)
    print("#" * 20, "SISTEMA DE REAJUSTE", "#" * 30)
    print("#" * 71)
    print("#" * 71)
    print('\n\n ###############: Franklin Dantas')
    print('\n ###############: Thiado Amaral')
    print('\n ###############: Maria Fernanda\n\n ')
    print('#' * 71)
    print('#' * 71)
    print('#' * 71)
    print('#' * 71)
    print('#' * 71)
  
def tela2():
    print("#" * 71)
    print("#" * 71)
    print("#" * 20, "SISTEMA DE REAJUSTE", "#" * 30)
    print("#" * 71)
    print("#" * 71)
   

def iniciar_sistema(iniciar):
    
    iniciar=input('\nPara iniciar digite S/N : ')
    print('\n ')
    return(iniciar)
    

def limpar():
    os.system('cls')
    os.system('color 1F')


def pausar():
    os.system('pause')


# Lançamento de variaveis

sma = float(c[0])
print("\n")
folha = 0
nvfolha = 0
reajuste = 0

# Lançamento de Lista

func = []
slant = []
reaj = []
novosal = []
por = []

limpar()
tela1()

inicio=iniciar_sistema('s')


if inicio == 's' or inicio =='S':
        
    # Mostra na tela o valor do salário atual
    limpar()
    tela2()
    print("\nLANÇAMENTOS DO SISTEMA       VALOR DO SALARIO ATUALMENTE     R$ {:.2f}\n".format(sma))
    
    #Adição do while e das variaveis comando e reutilização da varivel qtd
    
    qtd = 0
    comando = "S"
    
    # While para repetição do sistema e entrada no sistema
    
    while comando != "N":
        
        limpar()
        tela2()
        
        print("\nLANÇAMENTOS DO SISTEMA       VALOR DO SALARIO ATUALMENTE     R$ {:.2f}\n".format(sma))
        print("\n{}º - Lançamento".format(1 + qtd))
        
        nome = str(input('Digite o nome do funcionario : '))
        func.append(nome)
        sal = float(input('Digite o salário atual       : '))
        slant.append(sal)
        qtd = qtd + 1
        comando = input("\n\nDeseja registrar mais um funcionário? S/N: ").capitalize()
            
        
    
    # Fim do While
    
    #desvios e calculos
    
        if sal <= sma * 3:
            reajuste = (sal * 50 / 100)
            reaj.append(reajuste)
            nvsal = (reajuste + sal)
            novosal.append(nvsal)
            por.append("50%")
            folha = (folha + sal)
            nvfolha = (folha + reajuste)
    
        elif sal >= sma * 3 and sal <= sma * 10:
            reajuste = (sal * 20 / 100)
            reaj.append(reajuste)
            nvsal = (reajuste + sal)
            novosal.append(nvsal)
            por.append("20%")
            folha = (folha + sal)
            nvfolha = (folha + reajuste)
    
        elif sal >= sma * 10 and sal <= sma * 20:
            reajuste = (sal * 15 / 100)
            reaj.append(reajuste)
            nvsal = (reajuste + sal)
            novosal.append(nvsal)
            por.append("15%")
            folha = (folha + sal)
            nvfolha = (folha + reajuste)
    
        elif sal > sma * 20:
            reajuste = (sal * 10 / 100)
            reaj.append(reajuste)
            nvsal = (reajuste + sal)
            novosal.append(nvsal)
            por.append("10%")
            folha = (folha + sal)
            nvfolha = (folha + reajuste)
    
    limpar()
    tela2()
    
    
    # Cabeçalho da tela final
    
    print("\nLANÇAMENTOS DO SISTEMA       VALOR DO SALARIO ATUALMENTE      R$ {}\n".format(sma))
    print("\nNº  FUNCIONARIO             SALARIO  PORC          REAJUSTE  VLOR FINAL")
    print("=======================================================================\n")
    
    #lista de funcionários e reajustes
    for x in range(0, qtd):
    
        print(f'{x+1} - {func[x]:17} {slant[x]:13.2f}  {por[x]:5} {reaj[x]:15.2f} {novosal[x]:12.2f}')
    
    
    # Formatação de saida
    
    cfolha=folha
    folha = f'R$ {folha:_.2f}'
    folha = folha.replace('.',',').replace('_','.')
    vlReajust = (sum(reaj))
    vlReajust = f'R$ {vlReajust:_.2f}'
    vlReajust = vlReajust.replace('.',',').replace('_','.')
    vlFinal = (cfolha+sum(reaj))
    vlFinal = f'R$ {vlFinal:_.2f}'
    vlFinal = vlFinal.replace('.',',').replace('_','.')
    
    # Saida depois de processado e formatado
    
    print("\nRESUMO DE IMPACTO NA FOLHA DE PAGAMENTO ")
    print("=======================================================================\n")
    print(f"Valor da folha de pagamento.....: {folha}")
    print(f"Valor de Reajuste...............: {vlReajust}")
    print(f"Valor da nova Folha de Pagamento: {vlFinal}\n")
    print("=======================================================================\n\n")
    
    # Saida TXT
    
    with open('nova_folha.txt','w') as arquivo:
       arquivo.write("RESUMO EM TXT DOS LANÇAMENTOS\n\n")
       arquivo.write ("Nº  FUNCIONARIO             SALARIO  PORC          REAJUSTE  VLOR FINAL\n")
       arquivo.write("=======================================================================\n\n")
       for x in range(0,qtd):
           arquivo.write(str((f'{x+1} - {func[x]:17} {slant[x]:13.2f}  {por[x]:5} {reaj[x]:15.2f} {novosal[x]:12.2f}'))+'\n')
    
       arquivo.write("\nRESUMO DE IMPACTO NA FOLHA DE PAGAMENTO "+"\n\n")
       arquivo.write("=======================================================================\n\n")
       arquivo.write(f"Valor da folha de pagamento.....: {folha}"+"\n")
       arquivo.write(f"Valor de Reajuste...............: {vlReajust}"+"\n")
       arquivo.write(f"Valor da nova Folha de Pagamento: {vlFinal}\n"+"\n")
       arquivo.write("=======================================================================\n")
       
       pausar()
else:
    limpar()
    tela2()
    print('\n\n\nObrigado por usar nosso sistema\n\n\n\n')
    pausar()
    