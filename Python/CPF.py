CPF = str(input("Digite o seu CPF (use somente números): "))

if (len(CPF) == 11) and (CPF.isnumeric()):
    print(f"CPF válido\nCPF = {CPF[:-8]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:11]}")
else:
    print("CPF inválido \nRefaça o processo atento \nOBS: CPF deve ter apenas 11 números e apenas números!")