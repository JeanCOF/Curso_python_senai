"""1) Crie uma função que verifica se uma variável contém apenas
números
2) Crie uma função que verifica se uma string é minúscula
3) Crie uma função que verifica se uma string é maiúscula
4) Crie uma função que verifica se uma string começa com uma letra
específica
5) Crie uma função que verifica se uma string termina com uma letra
específica
6) Crie uma função que verifica se um valor é um número inteiro
7) Crie uma função que verifica se uma string contém apenas espaços
em branco"""

#exercicio 1

def veriNum(n):
    if n.isnumeric():
        print("A variável '{}' contém apenas números".format(n))
    else:
        print("A variável '{}' contém mais de um tipo de dado ou não é um dado numérico. Por favor, insira apenas números.".format(n))    
    return n

# Solicite a entrada do usuário e passe para a função
entrada = input("Digite um valor numérico: ")
veriNum(entrada)

#Exercico 2 e 3
def veriFra(frase):

    if frase.isalpha():
        print("A frase {} é uma string.\n".format(frase))
        if frase.isupper():
            print("A frase está em maiúsculas.")
        elif frase.islower():
            print("A frase está em minúsculas.")
    else:
        printi("A váriavel {} possui mias de um tipo de dado ou não é um dado de string.Por favor, insira apenas letras ou palávras")
    return frase

frase=input("Digite uma frase ou palavra: ")
veriFra(frase)

#Exercicio 4 e 5 combinados em pequeno jogo
def coleta_palavras(letra_inicial, letra_final):
    palavras_digitadas = []  # Lista para armazenar as palavras digitadas
    
    print(f"Digite palavras que comecem com a letra '{letra_inicial}' e terminem com a letra '{letra_final}'. Para encerrar, insira uma palavra que não cumpra essas condições.")

    while True:
        palavra = input("Digite uma palavra: ").strip()
        
        # Verifica se a palavra começa e termina com as letras definidas
        if palavra.startswith(letra_inicial) and palavra.endswith(letra_final):
            palavras_digitadas.append(palavra)
            print(f"Você digitou: {palavra}")
            print("Palavras digitadas até agora:", palavras_digitadas)
        else:
            print(f"Palavra '{palavra}' não começa com a letra '{letra_inicial}' ou não termina com a letra '{letra_final}'. Encerrando...")
            break

# Defina as letras com as quais as palavras devem começar e terminar
letra_inicial = input("Digite a letra com a qual as palavras devem começar: ").strip()
letra_final = input("Digite a letra com a qual as palavras devem terminar: ").strip()

# Chama a função com as letras definidas
coleta_palavras(letra_inicial, letra_final)

#Exercicio 6
def e_numero_inteiro(valor):
    try:
        int(valor)  # Tenta converter o valor para inteiro
        return True
    except ValueError:
        return False

# Exemplo de uso
numInt = input("Digite um valor: ").strip()
if e_numero_inteiro(numInt):
    print(f"'{numInt}' é um número inteiro.")
else:
    print(f"'{numInt}' não é um número inteiro.")

#exercicio 7

def contem_apenas_espacos(s):
    # Verifica se a string contém apenas espaços em branco
    return s.isspace() if s else False

# Exemplo de uso
entrada = input("Digite uma string: ")
if contem_apenas_espacos(entrada):
    print("A string contém apenas espaços em branco.")
else:
    print("A string não contém apenas espaços em branco.")
