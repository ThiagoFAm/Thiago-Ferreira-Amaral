import time



usuarios = ['gerente']
senhas = [2303567]



    
comando = 0
while comando != 3:
    print('1 - Cadastro.\n2 - login.\n3 - Finalizar o programa')
    comando = int(input("Digite o número desejado: "))

    if comando == 1:
        novo_user = input("Digite novo usuario: ").lower()
        
        confirme_cadastro = 'erro'
        while confirme_cadastro != 'sucesso':
            senha_novo_user = int(input(f"digite a senha para {novo_user}: "))
            confirme_senha_novo_user = int(input('confirme senha: '))
            if senha_novo_user == confirme_senha_novo_user:
                usuarios.append(novo_user)
                senhas.append(senha_novo_user)
                print("usuario registrado com sucesso!")
                confirme_cadastro = 'sucesso'
                time.sleep(3)
                    
            else:
                print('Senhas não coincidem!')
                confirme_cadastro = 'erro'
                print('Refaça o processo')
    elif comando == 2:
        comando_password = 'erro'
        comando_user = 'erro'
        while comando_user != 'sucesso':
            login = input("Digite Usuario: ").lower()
            if login in usuarios:
                print('usuário encontrado!')
                comando_user = 'sucesso'
                comando = 3
            else:
                print("Usuario NÃO encontrado!")

        comando_user= 'erro'
        while comando_password != 'sucesso': 
            senha = int(input("Digite senha: "))
            
            if (senha in senhas):
                print("usuario logado com sucesso!")
                comando_password = 'sucesso'
            else:
                print("ERRO na senha!")
    elif comando == 3:
        break
    
    
            
        



                




