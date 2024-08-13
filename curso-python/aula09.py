#1. Soma Simples: Crie uma função que recebe dois números e retorna a soma deles.
def soma(a1,a2):
    val=a1+a2
    return val
a1=float(input("Digite o 1° numero para soma: "))
a2=float(input("Digite o 2° numero para soma: "))

print("O valor da soma é {}".format(soma(a1,a2)))
#2. Subtração Simples: Crie uma função que recebe dois números e retorna a
#diferença entre o primeiro e o segundo.
def subtracao(a1,a2):
    val=a1-a2
    return val
a1=float(input("Digite o 1° numero para subtração: "))
a2=float(input("Digite o 2° numero para subtração: "))

print("O valor da subtração é {}".format(soma(a1,a2)))
#3. Multiplicação Simples: Crie uma função que recebe dois números e retorna
#o resultado da multiplicação deles.
def multiplicacao(a1,a2):
    val=a1*a2
    return val
a1=float(input("Digite o 1° numero para Multiplicação: "))
a2=float(input("Digite o 2° numero para Multiplicação: "))

print("O valor da multiplicação é {}".format(soma(a1,a2)))
#4. Divisão Simples: Crie uma função que recebe dois números e retorna o
#resultado da divisão do primeiro pelo segundo.
def divisao(a1,a2):
    val=a1/a2
    return val
a1=float(input("Digite o 1° numero para Divisão: "))
a2=float(input("Digite o 2° numero para Divisão: "))

print("O valor da divisão é {}".format(soma(a1,a2)))
#5. Mensagem de Saudação: Crie uma função que recebe um nome como
#argumento e retorna uma mensagem de saudação, como "Olá, [nome]!".
def saudacao(nome):
    msg=print("Olá {} seja bem vindo".format(nome))
    return msg

nome=str(input("Digite seu nome: "))
print(saudacao(nome))
#6. Verificação de Número Par: Crie uma função que verifica se um número é
#par. A função deve retornar True se for par e False caso contrário.
def veri_par(n1):
    if n1%2==0:
        par="Verdadeiro"
    else:
        par="Falso"
    return par

n1=int(input("Digite um numero par saber se ele é par: "))

print("O {} é par?: {}".format(n1,veri_par(n1)))
#7. Verificação de Número Ímpar: Crie uma função que verifica se um número é
#ímpar. A função deve retornar True se for ímpar e False caso contrário.
def veri_impar(n1):
    if n1%2==0:
        impar="Falso"
    else:
        impar="Verdadeiro"
    return impar

n1=int(input("Digite um numero par saber se ele é impar: "))

print("O {} é impar?: {}".format(n1,veri_impar(n1)))
#8. Calcular Área de um Retângulo: Crie uma função que recebe a largura e a
#altura de um retângulo e retorna a sua área.
#A= largura X altura
def calc_area(larg,alt):
    area=larg*alt
    return area

print("Calculo da área do retangulo.")
larg=float(input("Digite a largura do retangulo: "))
alt=float(input("Digite a altura do retangulo: "))

print("A área do retangulo é {}".format(calc_area(larg,alt)))
#9. Calcular Área de um Círculo: Crie uma função que recebe o raio de um
#círculo e retorna a sua área. Utilize π = 3.14.
#A = 3.14 X R ^ 2
def calc_area(raio):
    area=3.14*raio**2
    return area

print("Calculo da área do Circulo.")
raio=float(input("Digite o raio do circulo: "))


print("A área do circulo é {}".format(calc_area(raio)))
#10.Conversão de Celsius para Fahrenheit: Crie uma função que recebe uma
#temperatura em graus Celsius e retorna a temperatura equivalente em
#Fahrenheit.
#F = C X 1.8 + 32
def calc_graus(temp):
    temp_far=temp*1.8+32
    return temp_far

print("Calculo da Temperatura em fahrenheit")
temp=float(input("Digite a quantidade de graus em celsius: "))


print("A temperatura em fahrenheit é {}".format(calc_graus(temp)))
#11.Média de uma Lista: Crie uma função que recebe 3 números e retorna a
#média aritmética deles.
def calc_media(nums):
        for i in range(0,3):
            num=float(input(f"Informe o Numero {i+1}:"))
            nums.append(num)

            soma_nums = sum(nums)/3
        return soma_nums
nums = []          

media= calc_media(nums)

print("A media é {:.3f}".format(media))

#12.Maior Elemento da Lista: Crie uma função que recebe uma lista de números
#e retorna o maior elemento presente na lista.
def maior_num(nums):
    qtd_num=int(input("Digite a quantidade de numeros que vai inserir: "))
    for i in range(qtd_num):
        num=float(input(f"Informe o Numero {i+1}: "))
        nums.append(num)

        maior = max(nums)
    return maior
nums = []          

print("O maior numero da sequencia é {}".format(maior_num(nums)))
#13.Contagem regressiva: Crie uma função e imprime uma contagem regressiva
#de 0 até 10.
def cont():
    x=10
    print("Contagem de 10 a 0")
    while x>0:
        print(x)
        x-=1

c=cont()
print(c)
#14.Verificação de número positivo: Crie uma função que recebe um número e
#verifica se ele é positivo, retornando True ou False.
def veri_posi(n1):
    if n1>0:
        positivo=True
    else:
        positivo=False
    return positivo

n1=int(input("Digite um numero par saber se ele é postivo: "))

print("O {} é positivo?: {}".format(n1,veri_posi(n1)))

#15.Conversão de horas para minutos: Crie uma função que recebe um número
#de horas e retorna quantos minutos são (considere que 1 hora tem 60
#minutos).
def cont_min(hrs):
    min=hrs*60
    return min

hrs=int(input("Digite a quantidade de horas: "))
print("A quantidade de minutos é {}".format(cont_min(hrs)))

#16.Dobro de um número: Crie uma função que recebe um número e retorna o
#dobro dele.
def dobro(num1):
    num_dobro=num1*2
    return num_dobro

num1=float(input("Digite um numero: "))
print("O dobro de {} é {}".format(num1,dobro(num1)))

#17.Faça uma função que recebe por parâmetro o raio de uma esfera e
#calcula o seu volume (v = 4/3.P .R3).

import math

def calc_vol(raio):

    return (4/3) * math.pi * (raio ** 3)

print("Calculo do volume da esfera.")
raio=float(input("Digite o raio da esfera: "))

volume=calc_vol(raio)
print(f"O volume da esfera é {volume:.2f} cm³")
#18.Escreva uma função que receba dois números inteiros retorne o menor número
def maior_num(nums):
    for i in range(0,2):
        num=float(input(f"Informe o Numero {i+1}: "))
        nums.append(num)

        maior = min(nums)
    return maior
nums = []          

print("O menor numero da sequencia é {}".format(maior_num(nums)))