#Tuplas.
#1. Crie uma tupla com 5 números inteiros.
print("Crie uma tupla com 5 números inteiros.")
tupla1=(1,2,3,4,5)
print(tupla1)
#2. Acesse o primeiro elemento de uma tupla.
print("Acesse o primeiro elemento de uma tupla.")
print(tupla1[0])
#3. Acesse o último elemento de uma tupla.
print("Acesse o ulitmo elemento de uma tupla.")
print(tupla1[-1])
#4. Acesse o terceiro elemento de uma tupla.
print("Acesse o terceiro elemento de uma tupla.")
print(tupla1[2])
#5. Verifique o comprimento de uma tupla.
print("Verifique o comprimento de uma tupla.")
print(len(tupla1))
#6. Concatene duas tuplas.
tupla2=(6,7,8,9)
tupla3= tupla1 + tupla2
print("Concatene duas tuplas.")
print("tupla 1 {}".format(tupla1))
print("tupla 2 {}".format(tupla2))
print("tupla 1 + 2 {}".format(tupla3))
#7. Repita uma tupla 3 vezes.
for i in range(1,4):
    print("{}. tupla 3 : {}".format(i,tupla3))

#8. Conte quantas vezes um elemento aparece na tupla.
print("Conte quantas vezes um elemento aparece na tupla.")
tupla4=(2,4,5,6,2,5,8,2,6,2)
# Elemento que queremos contar
elemento = 2

# Contando quantas vezes o elemento aparece na tupla
contagem = tupla4.count(elemento)
print("tupla: {}".format(tupla4))

print(f"O elemento {elemento} aparece {contagem} vezes na tupla.")
#9. Encontre o índice de um elemento específico na tupla.
print("Encontre o índice de um elemento específico na tupla.")
elemento = 3

try:
    # Encontrando o índice do elemento
    indice = tupla3.index(elemento)
    print(f"O elemento {elemento} está no índice {indice}.")
except ValueError:
    print(f"O elemento {elemento} não está presente na tupla.")

#10.Verifique se uma tupla está vazia.
print("Verifique se uma tupla está vazia")
# Definindo a tupla
minha_tupla = ()

# Verificando se a tupla está vazia
print(minha_tupla)
if len(minha_tupla) == 0:
    print("A tupla está vazia.")
else:
    print("A tupla não está vazia.")


#Lista.
#1. Crie uma lista com 5 números inteiros.
print("Crie uma lista com 5 números inteiros")
lista1=[1,2,3,4,5]
print(lista1)
#2. Multiplique todos os elementos de uma lista de números.
print("Multiplique todos os elementos de uma lista de números")
from functools import reduce
import operator

# Usando reduce com uma função lambda
resultado = reduce(lambda x, y: x * y, lista1)

print("A multiplicação dos elementos da lista 1 é: {}".format(resultado))
#3. Encontre o maior número em uma lista de números.
print("Encontre o maior número em uma lista de números")
print("O maior numero da lista 1 é: {}".format(max(lista1)))
#4. Encontre o menor número em uma lista de números.
print("Encontre o menor número em uma lista de números")
print("O maior numero da lista 1 é: {}".format(min(lista1)))
#5. Ordene uma lista de números em ordem crescente.
print("Ordene uma lista de números em ordem crescente")
lista_aleatoria=[1,789,43,674,-10,63,-100,90,2,4,6,-2,-3]
print("Lista : {}".format(lista_aleatoria))
print("Lista ordenada: {}".format(sorted(lista_aleatoria)))

#6. Ordene uma lista de números em ordem decrescente.
print("Ordene uma lista de números em ordem decrescente")
print("Lista : {}".format(lista_aleatoria))
print("Lista ordenada decrescente: {}".format(sorted(lista_aleatoria,reverse=True)))
#7. Inverta a ordem dos elementos em uma lista.
print("Inverta a ordem dos elementos em uma lista")
print("Lista: {}".format(lista1))
# Inverte a lista
lista1.reverse()
# Imprime a lista invertida
print("Lista invertida: {}".format(lista1))
#8. Crie uma cópia de uma lista.
print("Crie uma cópia de uma lista")
copia= lista1.copy()
print("lista: {}".format(lista1))
print("Cópia da lista : {}".format(copia))
#9. Limpe todos os elementos de uma lista.
print("Limpe todos os elementos de uma lista")
lista1.clear()
print("Lista vazia: {}".format(lista1))

#Dicionários.
#1. Crie um dicionário com 3 pares chave-valor de strings.
print("Crie um dicionário com 3 pares chave-valor de strings.")
dicio1={"nome":"jean","cidade":"franca","sexo":"masculino"}
print(dicio1)
#2. Acesse o valor de uma chave específica em um dicionário.
print("Acesse o valor de uma chave específica em um dicionário")
print("O Nome no dicio1: {}".format(dicio1["nome"]))
#3. Adicione um novo par chave-valor a um dicionário.
print("Adicione um novo par chave-valor a um dicionário")
dicio1["idade"]= 22
print(dicio1)
#4. Remova um par chave-valor de um dicionário usando a função pop.
print("Remova um par chave-valor de um dicionário usando a função pop")
removido=dicio1.pop("cidade")
print("O valor de {} foi removido do dicionario {}".format(removido,dicio1))

#5. Verifique se uma chave específica está presente em um dicionário.
print("Verifique se uma chave específica está presente em um dicionário")
print("O chave nome está no diconario? {}".format("nome"in dicio1))
print("O elemento cidade está no dicionario? {}".format('cidade' in dicio1))

#6. Verifique se um valor específico está presente em um dicionário.
print("Verifique se um valor específico está presente em um dicionário")
print("O nome Jean está no dicionario? ")
print("jean" in dicio1.values())

#7. Conte quantos pares chave-valor um dicionário possui.
print("Conte quantos pares chave-valor um dicionário possui")
print("A quantidade de pares de chaves no dicionario é: {}".format(len(dicio1)))
#8. Copie um dicionário para outro.
print("Copie um dicionário para outro")
print(dicio1)
print("Copiando o diconario")
dicio2= dicio1.copy()
print("O dicionario 2 é: {}".format(dicio2))