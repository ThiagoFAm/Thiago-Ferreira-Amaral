Algoritmo "Folha de pagamento"
// Disciplina   : [Linguagem e L?gica de Programa??o]
// Professor   : Hiram Amaral
// Descri??o   : Aqui voc? descreve o que o programa faz! (fun??o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/04/2022
Var
   x : inteiro
   salario_minimo, novo_salario,  salario, reajuste, reajuste_total, aux : real
   nome : caractere
Inicio

   Escreval("Reajuste Sal?rial")
   Escreval("Quanto est? o sal?rio min?mo : ")
   leia(salario_minimo)
   para x de 0 ate 1 faca
      limpatela
      escreval("Digite o nome: ")
      leia(nome)
      escreval("Informe o sal?rio atual deste funcion?rio: ")
      leia(salario)
      se (salario<salario_minimo*3)  ent?o
         Escreval("===================================")
         Escreval("Nome = ", nome)
         Escreval("Sal?rio = ", salario)
         Escreval(">>>Reajuste = 50%")
         reajuste <- (salario * 50)/100
         novo_salario <- salario + reajuste
         escreval(">>>Novo sal?rio = ", novo_salario)
         Escreval("===================================")
      sen?o
         se (salario > salario_minimo * 3) e (salario < salario_minimo * 10 ) ent?o
            Escreval("==================================")
            Escreval("Nome = ", nome)
            Escreval("Sal?rio = ", salario)
            Escreval(">>>Reajuste = 20%")
            reajuste <- (salario * 20)/100
            novo_salario <- salario + reajuste
            escreval(">>>Novo sal?rio = ", novo_salario)
            Escreval("===================================")
         sen?o
            se (salario > salario_minimo * 10) e (salario < salario_minimo * 20 ) ent?o
               Escreval("================================")
               Escreval("Nome = ", nome)
               Escreval("Sal?rio = ", salario)
               Escreval(">>>Reajuste = 15%")
               reajuste <- (salario * 15)/100
               novo_salario <- salario + reajuste
               escreval(">>>Novo sal?rio = ", novo_salario)
               Escreval("================================")
            sen?o
               Escreval("================================")
               Escreval("Nome = ", nome)
               Escreval("Sal?rio = ", salario)
               Escreval(">>>Reajuste = 10%")
               reajuste <- (salario * 10)/100
               novo_salario <- salario + reajuste
               escreval(">>>Novo sal?rio = ", novo_salario)
               Escreval("================================")
            fimse
         fimse
      fimse
   fimpara
Fimalgoritmo