import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

import datetime
#1. Escreva um programa que pergunte a velocidade de um carro. Caso
#ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi
#multado.

#inserção de dados
print("Você está dirigindo e se aproxima de um radar!")
#Criação da função
def radar(vel):
    vel=int(input("QUAL SUA VELOCIDADE ATUAL? "))
    #verificação da velociade
    if vel > 80 :
        print("Você foi multado por ultrapassar o limite de velociade")
        multa= "sim"
    else:
        print("Você não foi multado")
        multa="não"
    return multa
vel=0
print("Vocé levou multa ? {} ".format(radar(vel)))

#2. Faça um programa que leia o ano de nascimento de uma pessoa,
#calcule a idade dela e depois mostre se ela pode ou não votar.

#inserção de dados
ano = int(input("Digite seu ano de nascimento: "))
#importação da data atual
ano_atual=datetime.datetime.now().year
idade=ano_atual-ano
#verificação da idade
if (idade>=16):
    print("Você pode votar esse ano")
else:
    print("Você ainda não pode votar")

#3. Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule
#a sua média e mostre na tela. No final, analise a média e mostre se o
#aluno teve ou não um bom aproveitamento (se ficou acima da média
#7.0).
#Criação da função
def inserir_notas():
    # Cria uma lista vazia para armazenar as notas
    notas = []
    # Solicita a quantidade de notas
    num_notas = int(input("Quantas notas deseja inserir? "))
    # Loop para preencher a lista de notas
    for i in range(num_notas):
        nota = float(input(f"Informe a nota {i+1}: "))
        notas.append(nota)
    return notas

def calc_media(notas):
    # Calcula a média das notas
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Solicita o nome do aluno
nome_al = input("Digite o nome do aluno a ser avaliado: ")

# Insere as notas e calcula a média
notas = inserir_notas()
media = calc_media(notas)

# Exibe as notas e a média
print(f"O aluno {nome_al} teve as seguintes notas:\n{notas}\nE a sua média foi: {media:.2f}")

        

#4. Desenvolva um programa que leia um número inteiro e mostre se ele é
#PAR ou ÍMPAR.

num1 = int(input("Digite um numero: "))

if (num1%2==0):
    print("O numero é par")
else:
    print("o numero é impar")

#5. Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar
#descontos para todos, mas especialmente para mulheres. Faça um
#programa que leia nome, sexo e o valor das compras do cliente e calcule
#o preço com desconto. Sabendo que:

#➢ Homens ganham 5% de desconto
#➢ Mulheres ganham 13% de desconto


def calc_desc(sexo, val):
    # Solicita o nome do cliente
    nome = input("Digite o nome do cliente: ")
    
    # Solicita o gênero do cliente e garante que o valor inserido seja válido
    sexo = input("Digite o gênero do cliente M-Masculino / F-Feminino: ").upper()
    while sexo not in ["M", "F"]:
        print("INCORRETO, Digite um dos dois gêneros: M-Masculino / F-Feminino")
        sexo = input("Digite o gênero do cliente M-Masculino / F-Feminino: ").upper()
    
    # Solicita o valor da compra e converte para float
    val = float(input("Digite o valor da compra: "))
    
    # Define o desconto baseado no gênero
    if sexo == "M":
        desc = 0.05
    elif sexo == "F":
        desc = 0.13
    
    # Calcula o valor com desconto e o desconto aplicado
    val_desc = val * (1 - desc)
    desconto_aplicado = val * desc
    
    # Exibe o valor a ser pago e o desconto
    # A formatação para moeda é feita pelo locale.currency
    print("O valor a ser pago é de {}, e o desconto foi de {}".format(locale.currency(val_desc), locale.currency(desconto_aplicado)))
    
    return nome, sexo, val, val_desc


# Exibe os dados da compra do cliente chamando a função calc_desc
print("Dados da compra do cliente: {}".format(calc_desc(sexo, val)))

#6. Faça um algoritmo que pergunte a distância que um passageiro deseja
#percorrer em Km, calcule o preço da passagem cobrando:

#➢ R$0.50 por Km para viagens até 200Km e
#➢ R$0.45 para viagens mais longas.

def viagem():
    dist = float(input("Digite a distância em KM que deseja percorrer: "))
    if dist <= 200:
        val_viagem = dist * 0.50
    else:
        val_viagem = dist * 0.45
    return dist, val_viagem

# Chama a função e armazena o resultado em variáveis
dist, val_viagem = viagem()

# Exibe o resultado formatado corretamente
print("CALCULO DO VALOR DA VIAGEM")
print(f"Distância a ser percorrida: {dist} KM")
print(f"Valor a ser pago: R${val_viagem:.2f}")

#7. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e
#200

num=0
for i in range(1,201):
    if i % 2 !=0:
        num= i
        print(num)

#8. Números ímpares até 20: Escreva um programa que imprima todos os
#números ímpares de 1 até 20 usando um loop while.

num=0
i=0

while i != 20:
    num+=1
    if num %2 !=0:
        print(num)
    i+=1

#9. Calcular Área de um Retângulo: Crie uma função que recebe a largura e a
##A= largura X altura

def calc_area(larg, alt):
    # Calcula a área do retângulo multiplicando a largura pela altura
    area = larg * alt
    return area

# Informa ao usuário que o cálculo da área do retângulo está prestes a começar
print("Cálculo da área do retângulo.")

# Solicita a largura do retângulo ao usuário 
larg = float(input("Digite a largura do retângulo: "))

# Solicita a altura do retângulo ao usuário 
alt = float(input("Digite a altura do retângulo: "))

# Chama a função calc_area com a largura 
print("A área do retângulo é {}".format(calc_area(larg, alt)))
