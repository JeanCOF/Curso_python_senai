#Uma lista em Python é uma estrutura de dados que armazena uma sequência de valores. As listas em Python são classificadas como um tipo de dado mutável, e portanto não possuem tamanho fixo: podemos adicionar ou remover elementos de listas de maneira dinâmica ao longo do código.

#Mostrando uma lista de anos
print([1951,1969,1984])

#Mostrando uma lista de frutas
print(["maças","laranjas","morangos"])

#mostrando uma lista vazia
print([])

#lista simples
lista=[1,2,3,4,5]

listaSegundo= list(range(1,3))

print(lista)
print(listaSegundo)

#Criando a lista primeiro

primeiro=[1,2,3,4]

print(len(primeiro))
print(primeiro[0])
print(primeiro[2:4])

#print concatenação

print(primeiro+[5,6])

for n in[1,2,3,4]:
    print(n,end=" ")

print(3 in primeiro)
print(1 in primeiro)

#1. Crie uma lista vazia.
lista=[]
#2. Crie uma lista com 5 números inteiros.
lista=[1,2,3,4,5]
#3. Crie uma lista com 3 strings.
lista=["Joao","carro","banana"]
#4. Crie uma lista mista com números inteiros e strings.
lista_mista=["joao",12345678912,"av.dr.joaquin"]
#5. Acesse o primeiro elemento de uma lista.
lista_num=[1,2,3,4,5,6,7,8,9,]
print("lista: {}".format(lista_num))
print("Primeiro elemento: {}".format(lista_num[0]))
#6. Acesse o último elemento de uma lista.
print("Ultimo elemento: {}".format(lista_num[8]))
#7. Acesse o terceiro elemento de uma lista.
print("Terceiro elemento: {}".format(lista_num[3]))
#8. Adicione um novo elemento no final da lista.
lista_num.append(10)
lista_num.append(11)
print("Adicionando 10 e 11 para a lista")
print("lista: {}".format(lista_num))
#9. Adicione um novo elemento no início da lista.
print("Adicionando mais elementos no inicio da lista")
lista_num.insert(0,0)
lista_num.insert(0,-1)
lista_num.insert(0,-2)
lista_num.insert(0,-3)
lista_num.insert(0,-4)
lista_num.insert(0,-5)
print("lista: {}".format(lista_num))       
#10. Remova o último elemento da lista.
ultimo=lista_num.pop()
print("lista: {}".format(lista_num))
print("ultimo elemento removido: {}".format(ultimo))
#11. Remova o primeiro elemento da lista.
ultimo=lista_num.pop(0)
print("lista: {}".format(lista_num))
print("primeiro elemento removido: {}".format(ultimo))
#12. Verifique se um elemento específico está na lista.
print("Verificação se 2 está na lista")
print(2 in lista_num)
#13. Conte quantos elementos a lista possui.
print("Contagem de quantos elementos estão na lista")
print(len(lista_num))
#14. Some todos os elementos de uma lista de números.
print("lista: {}".format(lista_num))
print("soma dos elementos da lista : {}".format(sum(lista_num)))
#15. Multiplique todos os elementos de uma lista de números.
from functools import reduce
import operator

produto = reduce(operator.mul, lista_num, 1)
print("Produto dos valores da lista: {}".format(produto))
#16. Encontre o maior número em uma lista de números.
print("lista: {}".format(lista_num))
print("O maior elemento é : {}".format(max(lista_num)))
#17. Encontre o menor número em uma lista de números.
print("lista: {}".format(lista_num))
print("O menor elemento é : {}".format(min(lista_num)))
#18. Ordene uma lista de números em ordem crescente.
lista_aleatoria=[1,789,43,674,-10,63,-100,90,2,4,6,-2,-3]
print("Lista : {}".format(lista_aleatoria))
print("Lista ordenada: {}".format(sorted(lista_aleatoria)))
#19. Ordene uma lista de números em ordem decrescente.
print("Lista : {}".format(lista_aleatoria))
print("Lista ordenada decrescente: {}".format(sorted(lista_aleatoria,reverse=True)))
#20. Inverta a ordem dos elementos em uma lista.
print("Lista: {}".format(lista_num))
# Inverte a lista
lista_num.reverse()
# Imprime a lista invertida
print("Lista invertida: {}".format(lista_num))
#21. Crie uma cópia de uma lista.
copia= lista_num.copy()
print("lista: {}".format(lista_num))
print("Cópia da lista : {}".format(copia))
#22. Limpe todos os elementos de uma lista.
print("lista: {}".format(lista_num))
print("Lista limpa : {}".format(lista_num.clear()))
#23. Verifique se todos os elementos de uma lista são números inteiros.
lista_num=[1,2,3,4,5]
print("Verificando se todos os valores da lista são numero inteiros: ")
print("lista: {}".format(lista_num))
todos_sao_inteiros = all(isinstance(x, int) for x in lista_num)
print("Todos os numeros são inteiros: {}".format(todos_sao_inteiros))
print("lista: {}".format(lista_mista))
todos_sao_inteiros = all(isinstance(x, int) for x in lista_mista)
print("Todos os numeros são inteiros: {}".format(todos_sao_inteiros))
