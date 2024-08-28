import random
nomes=[]
for i in range(4):
 
    aluno=str(input("Digite o nome do aluno: "))
    nomes.append(aluno)
    

escolhido = random.choice(nomes)
print(nomes)
print("O nome escolhido foi: {} ".format(escolhido))
random.shuffle(nomes)
print("A lista de alunos foi {}".format(nomes))