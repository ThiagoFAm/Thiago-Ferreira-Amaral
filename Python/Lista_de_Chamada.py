alunos = []
presentes = []
a = 0
faltosos = []
f = 0

for aluno in range(3):
    nome = input(str("Nome do Aluno: "))
    alunos.append(nome)
    presença = input(str("F = Faltasos/ P = Presentes: "))
    if (nome in alunos) and (presença == "p") or (presença == "P"):
        a = a + 1
        presentes.append(nome)
    if (nome in alunos) and (presença == "f") or (presença == "F"):
        f = f - 1
        faltosos.append(nome)
print(alunos)
print(f"Total de alunos = {len(alunos)}")
print("-----------------------------------------------------------------------------------------------------------------------")
print(f"Alunos presentes = {presentes}")
print(f"Total de alunos presentes = {a}")
print("-----------------------------------------------------------------------------------------------------------------------")
print(f"Alunos faltosos = {faltosos}")
print(f"Total de alunos faltosos = {f}")
print("-----------------------------------------------------------------------------------------------------------------------")