Algoritmo "Consumo de gasosa"
// Disciplina   : [Linguagem e L?gica de Programa??o]
// Professor   : Hiram Amaral 
// Descri??o   : Escrever um algoritmo para determinar o consumo m?dio de um
// autom?vel sendo fornecida a dist?ncia total percorrida pelo autom?vel e
// o total de combust?vel gasto.
// Autor(a)    : Thiago
// Data atual  : 29/03/2022
Var

combustivel, distancia: Real
consumo_medio: Real
valor_gasosa: real 
valor_dinheiro : real

Inicio
Escreval("Distacia total percorrida no trajeto em Km:")
leia(distancia)

Escreval("Combustivel gasto em litros:")
leia(combustivel)

consumo_medio <- distancia/combustivel
Escreval("O consumo m?dio de gasolina foi de ", consumo_medio, "Km/L")

escreval("Quanto reais voc? ainda tem?")
leia(valor_dinheiro)
valor_gasosa <- 8
escreva("Com este dinheiro voce pode p?r ", valor_dinheiro/valor_gasosa,"L")


Fimalgoritmo