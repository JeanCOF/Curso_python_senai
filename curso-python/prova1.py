#avaliação 1 dia 30/07/2024

import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

#1 Imprima "A soma de 2 e 3 é:" e depois o resultado da soma.



print("A soma de 2 + 3 é: {} ".format(2+3))

#2 crie um programa que faça as seguintes verificações

print("7 é menor que 8 e maior que 6? {}, 15 é maior que 10 ou menor que 5? {}, 100 é igual a 100 ou 50? {}".format((7<8 and 7>6),(15>10 or 15<5),(100==100 or 100==50)))

#3 Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentualque cada um representa em relação ao total de eleitores

#função para o calculo de porcentagem
def calcular_porc(elet,vts_brac,vts_null,vts_val):
    porc_null= vts_null/elet*100
    porc_brac= vts_brac/elet*100
    porc_val= vts_val/elet*100

    #retorno dos valores do calculo
    return porc_brac,porc_null,porc_val

#inserção dos valores base
elet=int(input("A quantidade de eleitores é de :"))
vts_null=int(input("A quantidade de votos nulos são: "))
vts_brac=int(input("A quantidade de votos brancos são: "))
vts_val=int(input("A quantidade de votos validos são: "))

#Chamada para a função
porc_null,porc_brac,porc_val=calcular_porc(elet,vts_brac,vts_null,vts_val)

print("A quantidade de eleitores são: {}, a de votos nulos são {}%, a de votos brancos são {}%, e de votos validos é de {}%".format(elet,porc_null,porc_brac,porc_val))


#4) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 13% para o Imposto de Renda, 11% para o INSS e 9% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo

#Inserção de dados
sal_hora=float(input("Digite quanto voce ganha por hora: "))
num_horas=float(input("Quantas horas voce trabalhou no mês: "))

#calculo de horas
sal_final= sal_hora*num_horas
#calculo do salario liquido
sal_liq= sal_final-(sal_final*0.13)-(sal_final*0.11)-(sal_final*0.09)

#tratamento para valores monetarios
sal_liq=locale.currency(sal_liq)

print("O seu salario esse mês é {} e com os descontos é de {}, o valor pago de imposto de renda foi {}, de INSS foi de {} e de sindicato de {}".format(locale.currency(sal_final),sal_liq,locale.currency(sal_final*0.13),locale.currency(sal_final*0.11),locale.currency(sal_final*0.09)))

#5) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

#Inserção de dados
num1=int(input("Digite o primeiro numero inteiro: "))
num2=int(input("Digite o segundo numero inteiro: "))
num3=float(input("Digite um numero real: "))


calc=[(num1*2)*(num2/2),(num1*3)+num3,(num3**2)]

print("o produto do dobro do primeiro com metade do segundo , a soma do triplo do primeiro com o terceiro e o terceiro elevado ao cubo é respectivamente : {}/n".format(calc))

#6) Faça um algoritmo que efetue o cálculo do salário líquido de um professor. As informações fornecidas serão: valor da hora aula, número de aulas lecionadas no mês e percentual de desconto do INSS. Imprima na tela o salário líquido final.

#Inserção de dados
sal_hora=float(input("Digite quanto voce ganha por aula: "))
num_aulas=float(input("Quantas aulas voce trabalhou no mês: "))
inss=int(input("Digite o valor percentual de desconto do INSS: "))

#calculo do salario liquido
sal_final= sal_hora*num_aulas
sal_liq= sal_final-(sal_final*(inss*0.01))

print("O salario liquido é {}".format(locale.currency(sal_liq)))

#7) Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado, seguido do seu antecessor, seu sucessor e a soma entre eles.

num1=int(input("Digite um numero inteiro: "))

print("O numero é {} o seu antecessor é {} e seu sucessor é {} ".format(num1,num1-1,num1+1,(num1-1)+(num1+1)))

#8) João recebeu seu salário de R$ 2000,00 e precisa pagar duas contas (C1=R$ 250,00 e C2=R$320,00) que estão atrasadas. Como as contas estão atrasadas, João terá de pagar multa de 4% sobre cada conta. Faça um algoritmo que calcule e mostre quanto restará do salário do João

#Inserção de dados
c1= 250+(c1*0.04)
c2= 320+(c2*0.04)

#calculo da multa
atraso= c1 + c2


print("O salario que restou para joao foi: {} ".format(locale.currency(2000-atraso)))

#9) Faça um algoritmo que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal_maior * diagonal_menor) /2

#Inserção de dados
diag_maior=float(input("Digite a medida da diagonal maior: "))
diag_menor=float(input("Digite a diagonal menor: "))


print("A area desse losango é {}".format(diag_maior*diag_menor/2))

#10) Faça um algoritmo que calcule e mostre a área de um trapézio. Sabe-se que: A = (base maior + base menor) * altura) /2

base_maior=float(input("Digite a medida da base maior: "))
base_menor=float(input("Digite a medida da base menor: "))
alt=float(input("Digite a altura: "))

print("A area desse trápezio é {}".format(((base_maior+base_menor)* alt )/2))