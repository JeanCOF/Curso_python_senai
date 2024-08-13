import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

import datetime

#Indentação
#A divisão do código com a indentação Python é uma prática essencial para organizar e estruturar seu código de forma eficiente. A indentação consiste em utilizar espaços ou tabulações para definir blocos de código em Python. Essa técnica facilita a leitura e compreensão do código, além de torná-lo mais legível e organizado.

#Iserção de dados
idade = int(input("Digite sua idade: "))

#se idade maior ou igual a 18 
if (idade>=18):
    print("Você é maior de idade")
    #se idade for diferente de maior ou igual a 18  
else:
    print("Você é menor de idade ")

#Estrutura de decisão
#Comandos de decisão ou desvio fazem parte das técnicas de programação,para construir estruturas de algoritmos que não são totalmenteseqüenciais;Com as instruções de desvio pode-se fazer com que o algoritmo proceda de uma ou outra maneira, de acordo com as decisões lógicas tomadas em função dos dados ou resultados anteriores.

#Estrutura de decisão simples IF(SE)

#1. Verifique se um número é positivo.
num1 = int(input("Digite um numero: "))

if (num1>0):
    print("Seu numero é positivo")
else:
    print("O numero é negativo")
#2. Verifique se um número é negativo.
num1 = int(input("Digite um numero: "))

if (num1<0):
    print("Seu numero é negativo")
else:
    print("O numero é positivo")
#3. Verifique se um número é zero.
num1 = int(input("Digite um numero: "))

if (num1==0):
    print("O numero é 0")
else:
    print("o numero não é zero")
#4. Verifique se um número é par.
num1 = int(input("Digite um numero: "))

if (num1%2==0):
    print("O numero é par")
else:
    print("o numero é impar")
#5. Verifique se um número é ímpar.
num1 = int(input("Digite um numero: "))

if (num1%2!=0):
    print("O numero é impar")
else:
    print("o numero é par")
#6. Verifique se um número é maior que outro.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um segundo numero: "))

if (num1>num2):
    print("O numero {} é maior que {}".format(num1,num2))
else:
    print("o numero {} é maior que {}".format(num2,num1))
#7. Verifique se um número é menor que outro.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um segundo numero: "))

if (num1<num2):
    print("O numero {} é menor que {}".format(num1,num2))
else:
    print("o numero {} é menor que {}".format(num2,num1))
#8. Verifique se um número é igual a outro.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um segundo numero: "))

if (num1==num2):
    print("O numero {} é igual ao {}".format(num1,num2))
else:
    print("o numero {} é diferente de {}".format(num1,num2))

#9. Verifique se um número é diferente de outro.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um segundo numero: "))

if (num1!=num2):
    print("O numero {} é diferente de {}".format(num1,num2))
else:
    print("o numero {} é igual ao {}".format(num1,num2))
#14. Verifique se uma pessoa é adulta (idade >= 18).

idade = int(input("Digite sua idade: "))


if (idade>=18):
    print("Você já é adulto")
else:
    print("Você ainda não é adulto")
#15. Verifique se uma pessoa é adolescente (idade entre 13 e 17).
idade = int(input("Digite sua idade: "))


if (idade>=13 and idade<=17):
    print("Você é adolescente")
elif (idade>=18):
    print("Você já é adulto")
else:
    print("Você é criança")

#16. Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano
ano = int(input("Digite seu ano de nascimento: "))
ano_atual=datetime.datetime.now().year
idade=ano_atual-ano
if (idade>=16):
    print("Você pode votar esse ano")
else:
    print("Você ainda não pode votar")

#17. Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens: ACESSO PERMITIDO caso a senha seja válida. ACESSO NEGADO caso a senha seja inválida.

senha= int(input("Digite a senha: "))

if (senha==1234):
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")

#18. As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

macas= float(input("Digite a quantidade de maças compradas: "))

if (macas>=12):
    macas=locale.currency(macas*0.25)
    print("O total a pagar é {}".format(macas))
else:
    macas=locale.currency(macas*0.30)
    print("O total a pagar é {}".format(macas))

#19. Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas: - para homens: (72.7 * Altura) – 58 - para mulheres: (62.1 * Altura) – 44.7

alt= float(input("Digite sua altura: "))
sex= str(input("Digite seu genero MASCULINO-M FEMININO-F : "))

if (sex.upper()=="M"):
    print("Seu peso ideal deve ser {:.2f}KG".format((72.7*alt)-58))
else:
    print("Seu peso ideal deve ser {:.2f}KG".format((62.1*alt)-44.7))

#20. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte: − Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área − Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área. − Se o número de lados for igual a 5 escrever PENTÁGONO

num_lado = int(input("Digite a quantidade de lados (3-5): "))

if (num_lado==3):
    print("A forma é um triângulo")
elif(num_lado==4):
    print("A forma é um quadrado")
elif(num_lado==5):
    print("A forma é um pentágono") 

#21. Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso. − Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO. − Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
num_lado = int(input("Digite a quantidade de lados (3-5): "))

if (num_lado==3):
    print("A forma é um triângulo")
elif(num_lado==4):
    print("A forma é um quadrado")
elif(num_lado==5):
    print("A forma é um pentágono") 
elif(num_lado<3):
    print("Não é um poligono")
elif(num_lado>5):
    print("Poligono não identificado")    
#22. Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que: Triângulo Retângulo: possui um ângulo reto. (igual a 90o) Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90o) Triângulo Acutângulo: possui três ângulos agudos. (menor que 90o)

ang1 = float(input("Digite o valor do primeiro angulo do triângulo: "))
ang2 = float(input("Digite o valor do segundo angulo do triângulo: "))
ang3 = float(input("Digite o valor do terceiro angulo do triângulo: "))

if (ang1+ang2+ang3==90):
    print("é um triângulo retângulo")
elif (ang1+ang2+ang3>90):
    print("é um triângulo obtusângulo")
elif (ang1+ang2+ang3<90):
    print("é um triângulo Acutângulo")
else:
    print("Valores incorretos")

#23. Faça um programa que leia um número e escreva na tela se o número é menor, igual ou maior que zero. 

num1=int(input("Digite um numero: "))

if (num1>0):
    print("O numero é maior que zero")
elif (num1==0):
    print("O numero é zero")
if (num1<0):
    print("O numero é menor que zero")

# 24. O IMC (índice de massa corpórea) indica o grau de obesidade de uma pessoa. Este índice é obtido pelo peso (em kg) dividido pelo quadrado da altura (em metros). A tabela a seguir apresenta as faixas deste índice:

peso=float(input("Digite sua massa: "))
alt=float(input("Digite sua altura: "))

imc= peso / (alt**2)

if (imc<20):
    print("Abaixo do normal")
elif(imc >= 20 and imc <=25):
    print("Normal")
elif(imc >= 25 and imc <=30):
    print("sobrepeso")
elif(imc >= 30 and imc <=35):
    print("Obesidade leve")
elif(imc >= 35 and imc <=40):
    print("obesidade moderada")
else:
    print("Obesidade mórbida")