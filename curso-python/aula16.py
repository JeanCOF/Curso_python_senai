"""1) Crie um programa que receba um número e tente dividir um número por
zero e trate a exceção de divisão por zero.

2) Crie um programa que receba uma string para um tipo inteiro e trate a
exceção de valor inválido.

3) Crie um programa que receba um índice e verifique se este índice está
em uma lista.

4) Crie uma função que receba dois argumentos e trate para divisão igual a
0

5) Crie um programa que receba um número decimal e trate o erro caso
invalido

6) Crie um programa que abra um arquivo e trate o erro caso não exista"""

print("Crie um programa que receba um número e tente dividir um número por zero e trate a exceção de divisão por zero .\n")
resultado=0

try:
    x = int(input("Digite um número: "))
    y = 0
    resultado = x / y
    print("O resultado é : {}".format(resultado))
except ZeroDivisionError:
    print("ERRO não é possivel dividir por zero")

print("Crie um programa que receba uma string para um tipo inteiro e trate a exceção de valor inválido.\n")
num1=0
while num1 != int and num1 == 0:
    try:
        num1=int(input("Digite uma Número: "))
    except ValueError:
        print("ERRO por favor digite uma número")

print("Crie um programa que receba um índice e verifique se este índice está em uma lista.\n")

lista = [1, 2, 5, 7, "frango", 10, 15]
i = 0
while i == 0:
    try:
        n = int(input("Digite uma posição para buscar na lista: "))
        # Tenta acessar o valor na posição n da lista
        print("O valor da posição é {}".format(lista[n]))
        i = 1  # Se tudo correr bem, sai do loop
    except IndexError:
        # Captura o erro se a posição estiver fora dos limites da lista
        print("Posição inválida. Por favor, digite um índice válido.")
    except ValueError:
        # Captura o erro se a entrada não for um número
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("Crie uma função que receba dois argumentos e trate para divisão igual a 0")
def dividir(dividendo, divisor):
    """
    Divide dois números e lança uma exceção se o divisor for zero.

    :param dividendo: O número que será dividido.
    :param divisor: O número pelo qual o dividendo será dividido.
    :return: O resultado da divisão se o divisor não for zero.
    :raises ValueError: Se o divisor for zero.
    """
    try:
        if divisor == 0:
            raise ValueError("Erro: Divisor não pode ser zero.")
        resultado = dividendo / divisor
        return resultado
    except ValueError as e:
        return str(e)

# Exemplos de uso
print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Saída: Erro: Divisor não pode ser zero.


print("Crie um programa que receba um número decimal e trate o erro caso invalido")
while True:
    try:
        # Solicita a entrada do usuário
        entrada = input("Digite um número decimal: ")
        
        # Tenta converter a entrada para um número decimal (float)
        numero_decimal = float(entrada)
        
        # Se a conversão for bem-sucedida, imprime o número e sai do loop
        print("Número decimal recebido: {}".format(numero_decimal))
        break
    except ValueError:
        # Captura o erro se a entrada não puder ser convertida para float
        print("Entrada inválida. Por favor, digite um número decimal válido.")


print("Crie um programa que abra um arquivo e trate o erro caso não exista\n")
filename = input("Digite o nome do arquivo que deseja abrir: ")

try:
    # Tenta abrir o arquivo no modo de leitura
    with open(filename, 'r') as file:
        # Lê e exibe o conteúdo do arquivo
        conteudo = file.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    # Captura o erro se o arquivo não for encontrado
    print(f"Erro: O arquivo '{filename}' não foi encontrado.")
except IOError:
    # Captura outros erros relacionados a I/O
    print(f"Erro: Não foi possível abrir o arquivo '{filename}'.")
