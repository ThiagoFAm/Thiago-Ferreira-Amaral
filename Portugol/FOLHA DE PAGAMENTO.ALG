Algoritmo "Folha de pagamento"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Hiram Amaral
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/04/2022
Var
   x : inteiro
   salario_minimo, novo_salario,  salario, reajuste, reajuste_total, aux : real
   nome : caractere
Inicio

   Escreval("Reajuste Salárial")
   Escreval("Quanto está o salário minímo : ")
   leia(salario_minimo)
   para x de 0 ate 1 faca
      limpatela
      escreval("Digite o nome: ")
      leia(nome)
      escreval("Informe o salário atual deste funcionário: ")
      leia(salario)
      se (salario<salario_minimo*3)  então
         Escreval("===================================")
         Escreval("Nome = ", nome)
         Escreval("Salário = ", salario)
         Escreval(">>>Reajuste = 50%")
         reajuste <- (salario * 50)/100
         novo_salario <- salario + reajuste
         escreval(">>>Novo salário = ", novo_salario)
         Escreval("===================================")
      senão
         se (salario > salario_minimo * 3) e (salario < salario_minimo * 10 ) então
            Escreval("==================================")
            Escreval("Nome = ", nome)
            Escreval("Salário = ", salario)
            Escreval(">>>Reajuste = 20%")
            reajuste <- (salario * 20)/100
            novo_salario <- salario + reajuste
            escreval(">>>Novo salário = ", novo_salario)
            Escreval("===================================")
         senão
            se (salario > salario_minimo * 10) e (salario < salario_minimo * 20 ) então
               Escreval("================================")
               Escreval("Nome = ", nome)
               Escreval("Salário = ", salario)
               Escreval(">>>Reajuste = 15%")
               reajuste <- (salario * 15)/100
               novo_salario <- salario + reajuste
               escreval(">>>Novo salário = ", novo_salario)
               Escreval("================================")
            senão
               Escreval("================================")
               Escreval("Nome = ", nome)
               Escreval("Salário = ", salario)
               Escreval(">>>Reajuste = 10%")
               reajuste <- (salario * 10)/100
               novo_salario <- salario + reajuste
               escreval(">>>Novo salário = ", novo_salario)
               Escreval("================================")
            fimse
         fimse
      fimse
   fimpara
Fimalgoritmo