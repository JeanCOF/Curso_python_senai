#O comando Do While é uma estrutura fundamental em muitas linguagens de programação, sendo utilizado para executar repetidamente um bloco de código enquanto uma condição específica permanecer verdadeira.

x=1 
while x<= 15:
    print(x)
    x+=1


val=0
soma=0
media=0

val= float(input("Digite um valor: "))

while val >0.0:
    soma+=val
    qtd+=1
    val= float(input("Digite um valor: "))

media = soma/qtd

print("Tota da soma {}\nQuantidade de valores somados{}\nTotal do valor{}".format(soma,qtd,media))

#1. Contagem regressiva simples: Escreva um programa que conte de 10 até 1 usando um loop while.
x=10
while x>=0:
    print(x)
    x-=1
#2. Faça um programa, utilizando while, que mostre na tela os números de 0 a 100.
x=0
while x<=100:
    print(x)
    x+=1
#3. Soma até 100: Escreva um programa que some números começando do 1 até que a soma ultrapasse 100 usando um loop while.
x=0
soma=0
while soma <100:
    x=float(input("Digite um valor para ser somado:"))
    if x > 100 :
        print("digite um valor abaixo de 100")
    elif x==100:
        soma += x
        print("O valor é {}".format(soma))
    else:
        soma+=x
        print("O valor é {}".format(soma))
            
#4. Tabuada do 7: Escreva um programa que imprima a tabuada do 7 usando um loop while.
i=1
while i != 11:
    print("A tabuada do 7 é 7 X {} = {} ".format(i,7*i))
    i+=1
#5. Números ímpares até 20: Escreva um programa que imprima todos os números ímpares de 1 até 20 usando um loop while.
i=0
while i < 21:
    i+=1
    if i % 2 !=0:
        print("Numeros impares até o 20 = {}".format(i))

#6. Validação de senha: Escreva um programa que peça ao usuário para digitar uma senha até que ele acerte usando um loop while. Senha 123
senha=int(input("DIGITE A SENHA: "))

while senha != 123:
    print("Senha Inválida")
    senha=int(input("DIGITE A SENHA: "))
print("Acesso permitido")

#7. Elabore um programa que mostre todos os números múltiplos de 5 de 100 até 0.
x=100

while x>=0:
    print(x)
    x-=5

#8. Escreva um laço while para imprimir cada uma das seguintes situações: 
# a) Todos os quadrados menores que n. Por exemplo, se n for 100, imprimir
# 0 1 4 9 16 25 36 49 64 81.
num=int(input("Digite um valor: "))
x=1

while(x**2 < num):
    print('{} ^ 2 = {}'.format(x,(x**2)))
    x = x + 1
#b) todos os números positivos que são divisíveis por 10 e menores que n.
#Por exemplo, se n for 100,
#imprimir 10 20 30 40 50 60 70 80 90.
num=int(input("Digite um valor: "))
x=1

while(x < num):
    x = x + 1
    if x % 10 ==0:
        print('todos os números positivos que são divisíveis por 10 e menores que {} \n'.format(num))  
        print(x)
   
#c) Todas as potências de dois menores que n. Por exemplo, se n for 100,
#imprimir 1 2 4 8 16 32 6
num=int(input("Digite um valor: "))
x=1

while(2**x < num):
   print("Todas as potências de dois menores que {}".format(num))
   print("2^{}={}".format(x,2**x))
   x+=1