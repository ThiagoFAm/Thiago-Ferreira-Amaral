# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 17:43:19 2022

@author: Hiram Amaral
"""

import numpy as np

def sigmoid(soma):
    return 1 / (1+ np.exp(-soma))

def sigmoidDerivada(sig):
    
    return sig * (1 - sig)
a = sigmoid(0.5)
b = sigmoidDerivada(a)

# a = np.exp(2)
# b = np.exp(0)

xi = np.array([[0,0],
                    [0,1],
                    [1,0],
                    [1,1]])
wi = np.array([[0],[1],[1],[0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, -0.469]])

pesos1 = np.array([[-0.017],[-0.893],[0.148]])

epocas = 2
taxaAprendizagem = 0.3
momento = 1

for j in range(epocas):
    camadaEntrada = xi
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = wi - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    print(f'Erro da RNA = {mediaAbsoluta}')
    
    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    
    
    
    camadaOcultaTransposta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)
    
    #Ex: a partir das entradas [1,1]
    
    #Para iniciar iremos calcular todas as entradas * peso (xi * wi)
    
    #Entradas = [1,1] 
    #Pesos para a primeira camada da camada oculta = [-0.424, 0.358] --> 1 * -0.424 + 1 * 0.358 = -0.66
    #ou seja, a soma da primeira camada da camada oculta é -0.66, aghora que temos a soma, descobriremos 
    #o valor de ativação do mesmo, Ativação(ou também Sigmoide)= 1 / ( 1 ^ (0.66) = 0.484 
    
    #Repetiremos o mesmo processo para as demais camadas, que ao total são duas camadas.
    
    #Entradas = [1,1]
    #Pesos para a segunda camada da camada oculta = [-0.740, -0.577] --> 1 * (-0.740) + 1 * (-0.577) = -1.317
    #Soma da segunda camada da camada oculta = -1.317
    #Ativação(ou também Sigmoide)= 1 / ( 1 ^ (1.317) = 0.211
    
    #Entradas = [1,1]
    #Pesos para a terceira camada da camada oculta = [-0.961, -0.469] --> 1 * (-0.961) + 1 * (-0.469) = -1.430
    #Soma da terceira camada da camada oculta = -1.430
    #Ativação(ou também Sigmoide)= 1 / ( 1 ^ (1.430) = 0.193
    
    #Valores da CAMADA OCULTA:
    #1 camada = [soma = -0.66] [Ativação = 0.484]
    #2 camada = [soma = -1.317] [Ativação = 0.211]
    #3 camada = [soma = -1.430] [Ativação = 0.193]
    #----------------------------------x----------x---------x--------x-------x-------x-------x-------x--------x--------x---------------------
    
    #Agora faremos o mesmo calculo (xi * wi) para obtermos o resultado do valor de ativação da camada de saída.
    #Repetiremos o mesmo processo repetido na camada oculta, porem, os valores que conseguimos como ativação na camada oculta
    #Passaram a ser nossas novas entradas e os pesos que nos foram dados são: [-0.017, -0.893, 0.148] OBS: Estão colocados por ordem de camada.
    
    # 0.484 * (-0.017) = -0.008
    # 0.211 * (-0.893) = -0.188
    # 0.193 * 0.148    = 0.028
     
    # -0.008 -0.188 + 0.028 = -0.168
    
    # Soma da camada saida = -0.168
    #Ativação da camada saida = 1 / ( 1 ^ (0.168) = 0.458
    
    #O resultado correto é 0, mas conseguimos 0.458, portanto houve um erro.
    #Para calcular o erro usamos a seguinte formula:
    #(erro = resposta correta - resposta errada) --> erro = 0 - 0.458
    
    #No Delta saida usamos o (erro * derivada saida). porém ainda não temos o valor de derivada saida.
    #derivada Saida = ativação * (1 - ativação) --> Derivada Saida = 0.458 * (1 - 0.458) --> Derivada Saida = 0.248
    #OBS: Derivada Saida também é chamada derivada Sigmoide
   
    #Agora que temos os valores necessários, podemos resolver a equação Delta Saída:
    #Delta Saída = erro * Derivada Saída ----> Delta Saída = -0.458 * 0.248 ----> Delta Saida = -0.113 
    
    #Assim como nas matrizes, iremos tranformar os pesos em matrizes transpostas,
    #O que antes estava assim:--> -0.013 ficará assim: -0.014  -0.89  0.149
    #                             -0.89
    #                              0.15
   
    #Agora vamos encontrar o Delta da camada oculta(Tambem chamado de Delta Escondida), usaremos a seguinte formula:
    #Delta escondido = Derivada Sigmoide * Peso * DeltaSaida
    #A derivada Sigmoide não é a mesma que encontramos anteriormente, a que encontramos um pouco mais acima é da camada de saida
    #Agora nós queremos a Derivada sigmoide da camada Oculta, pegaremos o resultado das ativações que conseguimos em cada camada da camada oculta
    
    #Derivada sigmoide da camada Oculta = 0.484 * (1 - 0.484) = 0.250
    #Derivada sigmoide da camada oculta = 0.211 * (1 - 0.211) = 0.167
    #Derivada sigmoide da camada oculta = 0.193 * (1 - 0.193) = 0.156
    
    #Agora que temos a Derivada Sigmoide das camadas ocultas podemos descobrir o Delta Escondida
    
    #Delta escondida = 0.250 * (-0.017) * (-0.114) = 0.000
    #Delta escondida = 0.167 * (-0.893) * (-0.114) = 0.017
    #Delta escondida = 0.156 * (0.148) * (-0.114) = -0.003
    
    #Ao final vamos corrigir os pesos para que consigamos um erro menor, do que antes
    #Para isso usaremos a formula do Peso n+1 = (peso * memomento) + (EntradaxDelta*Taxa de aprendizagem)
    #Nessa formula iremos precisar de valores de outras entradas, bem como: soma, peso, entradas, mas já deixarei pronto esses dados para apenas serem aplicados.
    
    #Vamos antes de calcular o peso descobrir quem é a EntradaxDelta
    #então somaremos os produtos de todas as entradas da camada oculta pelo Delta saida.
    
    #1° EntradaxDelta = 0.5 * (-0.098) + 0.589 * 0.139 + 0.396 * 0.139 + 0.484 * (-0.114) = 0.032
    #2° EntradaxDelta = 0.5*(-0.098) + 0.360 * 0.139 + 0.323 * 0.139 + 0.211 * (-0.114) = 0.022
    #3° EntradaxDelta = 0.5 * (-0.098) + 0.385 * 0.139 + 0.277 * 0.139 + 0.193 * (-0.114) = 0.021
    
    #Peso n+1 = (peso * memomento) + (EntradaxDelta*Taxa de aprendizagem)
    
    #Peso n+1 = (-0.017 * 1) + 0.032 * 0.3 = -0.007
    #Peso n+1 = (-0.893 * 1) + 0.022 * 0.3 = -0.886
    #Peso n+1 = (0.148 * 1) + 0.021 * 0.3 = 0.154 
    
    #xi * wi --> 0.484 * (-0.007) + 0.211 * (-0.886) + 0.193 * 0.154 = 0.029
    #Ativação(ou também Sigmoide)= 1 / ( 1 ^ (0.029) = 0.507 
    
    #Erro = 0 - 0.507 = -0.507
    
    
   