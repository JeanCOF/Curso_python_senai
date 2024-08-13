#Apresentação das caracteristicas do python
#
# linguagem de alto nivel
# Orientado a objetos
# Alta comunidade
# Linguagem interpretada
# facil aprendiza


#Exercicios

#1
nome = str(input("Digite seu nome: "))
idade= int(input("Digite sua idade: "))
end= str(input("Digite seu endereço: "))
sex= str(input("Digite seu genero: "))
prof= str(input("Digite sua profissão: "))

print("Seu nome é {} seu endereço é {} sua idade é {} seu genero é {} e sua profissão é {}".format(nome,idade,end,sex,prof))

#2

num1= int(input("Digite um numero: "))
num2= int(input("Digite um numero: "))
num3= int(input("Digite um numero: "))
num4= int(input("Digite um numero: "))
num5= int(input("Digite um numero: "))
num6= int(input("Digite um numero: "))

print("A soma desses numeros são: {}".format(num1+num2+num3+num3+num4+num5+num6))

#3

data= int(input("Digite o ano que voce nasceu: "))

print("A sua idade é {}".format(2024-data))

#4

num1= int(input("Digite um numero: "))
print("O quadrado desse numero é : {}".format(num1**2))

#5
num1= int(input("Digite um numero: "))

print("O sucessor e antecessor do numero {} são respectivamente {}, {}".format(num1,num1-1,num+1))

#6

num1= int(input("Digite um valor: "))
rea= num1 + (num1 *0.05)

print("O valor com reajuste de 55 é : {}".format(rea))

#7

val_aula= float(input("Digite o valor recebido por aula: "))

aulas= int(input("Digite a quantidade de aulas: "))

inss= int(input("Digite o desconto de INSS: "))

print("O seu salario vai ser {}, por {} aulas, e foi descontado {}".format((val_aula*aulas)-inss,aulas,inss))

#8
num1= int(input("Digite um numero: "))
num2= int(input("Digite um numero: "))
num3= float(input("Digite um numero real: "))

num4= num1*2 + num2/2
num5= num1*3+num3**3

print("Os resultados são: {} , {} ".format(num4,num5))

#9

alt= float(input("Digite a sua altura: "))

peso_ideal= (72.7*altura) - 58

print("Seu peso idela é : {}".format(peso_ideal))

#10

val_hora= float(input("Digite o valor recebido por hora: "))

horas= float(input("Digite a quantidade de horas: "))

val_mes= (((val_hora*horas)*24)*30)
val_desc= val_mes*0.24

print("O seu salario é {}, o bruto foi {}, o desconto do imposto de renda {}, imposto de inss {}, imposto de sindicato {}".format(val_desc,val_mes,val_mes*0.11,val_mes*0.08,val_mes*0.05))

#11

def calcular_porc(ind,vts_brac,vts_null,vts_val):
    porc_null= vts_null/ind*100
    porc_brac=vts_brac/ind*100
    porc_val=vts_val/ind*100
    return porc_null,porc_brac,porc_val

ind= int(input("Digite a qauntidade de eleitores: "))
vts_brac = int(input("Digite a quantidade de votos brancos: "))
vts_null = int(input("Digite a quantidade de votos nulos: "))
vts_val = int(input("Digite a quantidade de votos validos: "))

porc_null,porc_brac,porc_val =calcular_porc(ind,vts_brac,vts_null,vts_val)
print("A quantidade de votos foram {}, a de votos brancos são {}%, as de nulo foram {}%, e a de validos foram {}%,respectivamente em porcentagem. ".format(ind,porc_brac,porc_null,porc_val))

#12

numA- int(input("Digite o numero A:"))
numB= int(input("Digite o numero B: "))

print("O numero B é {}/nO numero A é {}".format(numB,numA))

#13

alt = float(input("Digite a altura: "))
larg= float(input("Digite a largura: "))
prof= float(input("Digite a profundidade: "))

vol= alt*larg*prof

print("O volume do determinado objeto é {}".format(vol))

#14

alt = float(input("Digite a altura: "))
raio= float(input("Digite a Raio "))

vol= raio*alt

print("O volume de uma lata de oleo com essas medidas é: ".format(vol))

#15

r1= float(input("Digite o valor da primeira resistencia: "))
r2 = float(input("Digite o valor da segunda resistencia: "))
r3 = float(input("Digite o valor da terceira resistencia: "))

print("A resistencia do circuito completo é :".format(r1+r2+r3))



