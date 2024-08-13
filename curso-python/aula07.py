
#1. Imprima os números de 1 a 10.
for i in range(10):
    i + 1 == 10 
    print(i+1)
#2. Imprima uma mensagem 5 vezes.
for i in range(5):
    i + 1 == 5
    print("mensagem numero {}".format(i+1))
#3. Imprima os números de 80 a 1 (em ordem decrescente).

for i in range(80,1,-1):
    print(i)
#4. Imprima os números de 1 a 100, pulando de 5 em 5.
for i in range(1,101,5):
    print(i)
#5. Imprima os números de 100 a 1, pulando de 10 em 10.
for i in range(100,0,-10):
    print(i)
#6. Escreva um algoritmo que exiba 20 vezes a mensagem “Eu gosto de estudar Algoritmos!”.
for i in range(20):
    i + 1 == 20
    print("{}.Eu gosto de estudar aloritimos".format(i+1))
#7. Leia o nome do usuário e escreva o nome dele na tela 10 vezes.
nome=str(input("Digite seu nome: "))
for i in range(10):
    i + 1 == 10
    print("{}.Seu nome é {}".format(i+1,nome))
#8. Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.

a=[]
for i in range(5):
    num1= float(input("Digite um numero:"))
    a.append(num1)

    if num1 > 0:
        print("{} numero ({}) é positivo".format(i+1,num1))
    else:
        print("{} numero ({}) é negativo".format(i+1,num1))

#9. Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.

num=0
for i in range(1,501):
    if  i % 2 !=0 and i % 3 ==0:
        num+= i
        print(num)

#10. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200

num=0
for i in range(1,201):
    if i % 2 !=0:
        num= i
        print(num)

#11. Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
num = int(input("Digite um numero: "))

for i in range(1,11):
    res= num * i
    print(res)
#12. Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10. Use o formato de apresentação (considerando que o usuário informou o número 5):
# Recebe o número do usuário
numero = int(input("Digite um número para calcular a tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):  
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#13. Modifique o algoritmo do exercício 11, de maneira que sejam impressos somente as multiplicações da tabuada cujo resultado seja um número par.
numero = int(input("Digite um número para calcular a tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):  
    resultado = numero * i
    if resultado % 2 == 0 :
        print(f"{numero} x {i} = {resultado}")
