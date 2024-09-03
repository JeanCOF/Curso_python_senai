"""Como funciona o Try Except no Python
O Try Except é uma construção fundamental na linguagem de programação Python para lidar com exceções e erros. Ele permite que o desenvolvedor controle o fluxo do programa e trate de forma adequada as situações inesperadas que possam ocorrer durante a execução do código.

A estrutura básica do Try Except
A estrutura básica do Try Except consiste em um bloco Try, onde o código suscetível a erros é colocado, e um bloco Except, onde o tratamento do erro é definido. Quando um erro ocorre dentro do bloco Try, o programa pula para o bloco Except correspondente ao tipo de erro ocorrido e executa as instruções ali presentes.

Funcionamento do Try Except no Python
O Try Except no Python funciona da seguinte maneira: o código dentro do bloco Try é executado normalmente, e caso nenhum erro ocorra, o programa segue adiante. No entanto, se um erro é lançado durante a execução do código dentro do bloco Try, o programa interrompe sua execução normal e pula para o bloco Except correspondente ao tipo de erro.

Existem diversos tipos de exceções que podem ser tratadas pelo Try Except, como por exemplo ValueError, TypeError, FileNotFoundError, entre outros. É importante conhecer os diferentes tipos de exceções para poder lidar com elas adequadamente em seu código."""

#value error
# x= int("hello")

#zero divison error
#resultado = 10/0

#index error
#lista=[1,2,3]
#print(lista[5])
#Não possui o index 5 na lista

#Syntax errors 
#print("hello"

#erro de indentação
#if true:
#print("Verdadeiro")
#O print não está na identação correta
resultado=0
while resultado != int and resultado == 0:
    try:
        x = int(input("Digite um número: "))
        y = int(input("Digite um número: "))
        resultado = x / y
    except ZeroDivisionError:
        print("ERRO não é possivel dividir por zero")
    except ValueError:
        print("ERRO por favor digite um número")
    except Exception as e:
        print("Ocorreu um erro : {}".format(e))
    else:
         print("O resultado é : {}".format(resultado))
    finally:
        print("Execução finalizada")

def dividir(a,b):
    if b == 0:
        raise ValueError("O dividor não pode ser zero")
    return a/b

try:
    resultado = dividir(18,0)
except ValueError as e:
    print("Erro: {}".format(e))

try:
    f= open('arquivo_inexistente.txt','r')
except FileNotFoundError:
    print("ERRO: Arquivo encontrado")

capitais={"Brasil":"Brasilia","Alemanha":"Berlim","Japao":"Toquio"}

try:
    print(capitais["Inglaterra"])
except KeyError:
    print("Erro chave não encontrada no dicionario")

try:
    resultado = "abc" + 123
except TypeError:
    print("ERRO: não é possivel somar uma string e um número")

try:
    import biblioteca_inexistente
except ModuleNotFoundError:
    print("ERRO Biblioteca não encontrada")


   