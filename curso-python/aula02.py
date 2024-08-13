#Descrição dos tipos de dados

#int= 1,2,3,4,5

#numeros inteiros

#float=1.10,2.65,1000.00

#numeros decimais

#logico=False

#recebe valores logicos como verdadeiro ou falso

#charac="uma frase"

#recebe valores alfanumericos

#Comando para entradas de Dados

#print #imprime os dados
#input #recebe os dados

#operadores de atribuição

#adição = +
#subtração = -
#multiplicação = *
#divisão = \
#exponeciação = ''

#hierarquia das opereções

#1.Pareteses (1 * 2)
#2. Exponenciação ''
#3. Multiplicação e divisão
#4. adição e subtração

#Operadores relacionais

# == Igual
# != diferente que
# > Maior que
# >= maior ou igual
# < menor
# <= menor ou igual

#Operadores Logicos

#& = and
#ou = or
#não = not

#Exemplos de operadores logicos

#3>5 & 8>1 = falso
#3>1 & 8>1 = verdadeiro
# para o & ambos tem que ser verdadeiros para o resultado ser verdadeiro

# 3>5 or 8>1 = verdadeiro 
# 3>5 or 8>9 = falso
#Para o Or é necessario que apenas uma das variaveis seja verdadeiro para o resultado ser verdadeiro

#not 3>5 = falso
#not 8<1 = verdadeiro
# o Not nega o resultado, ou seja se ele é verdadeiro ele será falso 

#Exercicios

#1. Use os operadores logicos para calcular a seguinte tabela

#A=5
#B=3

# A==B=false
# A!=B=true
# A>B=true
# A<B=false
# A>=B=true
# A<=B=false

#2.

#A= 5
#B= 8
#c= 1

#A==B & B>C =false
#A!=B or B<c= true
#A>B not = true
#A<B & B>C = true
#A>=B or B=C = false
#A<=B not = false

#3.

print(2>1)

print(5<10)

print("a"=="a")

print(8>5 & 8<10)

print(0 == 0 or 0 != 1)

print(9<10 or 9>20)

print("x" != "y")

print(1<2 & 3>2)

print("gato" == "gato" or "gato" == "cachorro")

print(10>5 or 10<15)

print(2+2 == 4)

print(7<8 & 7>6)

print(15>10 or 10<5)

print(100 == 100 or 100 == 50)

#Exercicios variaveis

#1
nome = str(input("Seu nome é:"))

print(f"{nome} seja bem vindo")

#2
numero = input("Digite um numero:")


print(f"O dobro desse numero é{int(numero)*2}")

#3
idade= int(input("digite a sua idade:"))

print(f"A sua idade é {idade}")

#4
num1= int(input("Digite o primeiro numero:"))

num2= int(input("Digite o segundo numero:"))

soma= num1 + num2

print(f"A soma dos numeros {num1} e {num2} é {soma}")

#5
numQua= int(input("Digite um numero:"))

print("o numero {} ao quadrado fica {}".format(numQua,numQua *numQua))

#6
graus= float(input("Digite a temperatura em celcius"))

print("A temperatura em Celsius é {} e em farenheit é {} ".format(graus,graus*1.8+32))

#7

idade= int(input("digite sua idade:"))

print("A sua idade é {} e em meses são {}".format(idade,idade*12))

#8

tam= int(input("digite uma distancia em metros:"))

print("A distancia de {} metros em centimetros é {}".format(tam,tam*100))

#9

nome= str(input("digite seu nome: "))

sobre= str(input("Digite seu sobrenome "))

print("Seu nome completo é {}" .format(nome + sobre))

#10

sal= int(input("Qual o valor de sua hora trabalhada? "))

horas= int(input("Quantas horas você trabalhou? "))

print("O valor que você recebeu é:{}R$".format(sal*horas))

#11

raio= float(input("digite um raio de um circulo: "))

dia= 3.14*raio**2

print("O diametro do raio é {}".format(dia))

#12

num3= int(input("Digite um numero: "))

raiz= math.sqrt(num3)

print("A raiz quadrada do numero {} é {}".format(num3,raiz))

#13

alt= float(input("Digite sua altura: "))
peso= float(input("Digite seu peso: "))

print("Seu imc é {}".fomart(peso/(alt*alt)))

#14

nome= str(input("Digite seu nome: "))

print("Seu nome em minusculo é: {}".format(nome.lower()))

#15

frase= str(input("Digite uma frase: "))

print("o tamanho da sua frase em caracteres é {}".format(len(frase)))

#16

far= float(input("Digite a temperatura em farenheit"))

print("A temperatura em Celsius é {} e em farenheit é {} ".format(far,far*(9/5)+32))

#17

nome =str(input("digite seu nome: "))
idade = int(input("Digite sua idade; "))
cid= str(input("Digite o nome de sua ciadade: "))

print("Voce é o {} de {} anos e mora na {}".formta(nome,idade,cid))

#18

num1= int(input("Digite um numero: "))
num2= int(input("Digite o seu divisor: "))

print("A divisão de {} por {} é {} ".format(num1,num2,num1/num2))

#19

nome= str(input("Digite seu nome: "))

print("Seu nome em maiusculas é : {}".format(nome.upper()))

#20

num1= int(input("Digite um numero: "))
num2= int(input("Digite o seu exponeciador: "))

print("A exponenciaÇão de {} por {} é {} ".format(num1,num2,num1**num2))

#21

num1= int(input("Digite um numero: "))
num2= int(input("Digite o segundo numero: "))

print("O produto de {} por {} é {} ".format(num1,num2,num1-num2))

#22

num1= int(input("Digite um numero: "))
num2= int(input("Digite o segundo numero: "))

print("A média de {} por {} é {} ".format(num1,num2,num1+num2/2))

#23

peso= float(input("Digite seu peso: "))
print("Seu peso é: {}".format(peso))

#24

alt= float(input("Digite sua altura : "))
print("Sua altura é: {}".format(alt))

#25

num1= int(input("Digite um numero: "))
num2= int(input("Digite o segundo numero: "))

print("A soma de {} por {} é {} a diferença é {} o produto é {} o quociente é {} ".format(num1,num2,num1+num2,num1-2,num1/num2,num1*num2))

#26

num1= int(input("Digite um numero: "))
tabuada=[num1*1,num1*2,num1*3,num1*4,num1*5,num1*6,num1*7,num1*8,num1*9,num1*10]
for num1 in tabuada:
    print(num1)

#27

nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))

print("A media das notas é {}".format((nota1+nota2)/2))

#28

tam= int(input("digite uma distancia em metros:"))

print("A distancia de {} metros em centimetros é {} e em milimetros é {}".format(tam,tam*100,tam*1000))

#29

cart= float(input("Quanto você tem em sua carteira?"))

print("Isso em doláres é :{}".format(cart*5,30))

#30

alt= int(input("Digite a altura de uma parede:"))
larg= int(input("Digite a largura dessa parede:"))

area= alt*larg
tinta= area/2

print("A área dessa parede é: {} e a quantidade de tinta é {}".format(area,tinta))
