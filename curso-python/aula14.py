"""Os módulos em Python são uma forma de organizar e reutilizar código. Um módulo é um arquivo contendo definições e instruções Python que podem ser importadas e utilizadas em outros programas. Com os módulos, é possível agrupar funções, classes e variáveis relacionadas em um único local, facilitando a manutenção e o compartilhamento de código entre diferentes projetos."""

"""
import math

num=int(input("Digite um numero: "))

print(math.ceil(num))

from math import sqrt

import math as matematica

print(matematica.sqrt(num))
"""
#1) Calcule a raiz quadrada de um número digitado pelo usuário
#math.sqrt()
import math

num=int(input("Digite um numero: "))
numQua= math.sqrt(num)
print(numQua)

#2) Calcule a raiz quadrada arredondado para cima
#math.ceil()
print(math.ceil(numQua))
#3) Calcule a raiz quadrada arredondado para baixo
#.floor()
print(math.floor(numQua))
#4) Crie um programa que leia um número Real qualquer pelo teclado e
#mostre na tela a sua porção Inteira.
#math.trunc()
num=float(input("Digite um numero: "))
print(math.trunc(num))
#5) Faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triângulo retângulo. Calcule e mostre o comprimento da
#hipotenusa.
#hipotenusa = math.hypot(catetoOposto,catetoAdjacente)
compOp=float(input("Digite o comprimento do cateto oposto: "))
compAd=float(input("Digite o comprimento do cateto adjascente: "))

print("A hipotenusa dos catetos é {}".format(math.hypot(compOp,compAd)))

#6) Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse ângulo.
#seno = math.sin(math.radians(angulo))
#cosseno = math.cos(math.radians((angulo)))
#tangente = math.tan(math.radians(angulo))

angulo=float(input("Digite um angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians((angulo)))
tangente = math.tan(math.radians(angulo))
print("O seno é {} o cosseno é {} e a tangente é {}".format(seno,cosseno,tangente))

#7) Um professor quer sortear um dos seus quatro alunos para apagar o
#quadro. Faça um programa que ajude ele, lendo o nome dos alunos e
#escrevendo na tela o nome do escolhido.
#Import random
#(Dica) leia quatro números em variáveis do tipo string e depois adicione
#em uma lista
#escolhido = random.choice(lista)

import random
nomes=[]
for i in range(4):
 
    aluno=str(input("Digite o nome do aluno: "))
    nomes.append(aluno)
    

escolhido = random.choice(nomes)
print(nomes)
print("O nome escolhido foi: {} ".format(escolhido))

#8) O mesmo professor do desafio 019 quer sortear a ordem de
#apresentação de trabalhos dos alunos. Faça um programa que leia o
#nome dos quatro alunos e mostre a ordem sorteada.
#lista = [n1,n2,n3,n4]
#random.shuffle(lista)

random.shuffle(nomes)
print("A lista de alunos foi {}".format(nomes))