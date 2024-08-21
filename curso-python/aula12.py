#As tuplas são estruturas de dados imutáveis em Python, o que significa que, uma vez criadas, não podem ser alteradas. Essa é uma característica distintiva que as separa de outras estruturas de dados como listas, que são mutáveis. Uma tupla em Python é definida por elementos separados por vírgulas e, opcionalmente, os mesmos podem ser envolvidos por parênteses. As tuplas podem conter tipos de dados heterogêneos, incluindo inteiros, strings, outras tuplas, e mais. Essa versatilidade as torna uma escolha valiosa para armazenar uma coleção de itens que não requer alteração.
#Empregadas corretamente, as tuplas contribuem para a criação de códigos mais seguros e otimizados, especialmente em situações onde a integridade dos dados é prioritária. Por serem imutáveis, as tuplas garantem que os dados permaneçam consistentes e não sejam inadvertidamente modificados, um aspecto crítico em muitas aplicações de software.

frutas=("Banana","maça")
print(frutas)

carne=("peixe","alcatra")
print(carne)

comidas= frutas + carne
print(comidas)

vegetais=("abobrinha","pepino")

print(vegetais)

lanche=("tomate","pão","alface")

print(lanche)

print(lanche[1])
print(lanche[2])
print(lanche[-2])

print(lanche[:2])

for i in lanche:
    print("Eu comi: {}".format(i))

print(len(lanche))
print(sorted(lanche))

pessoa=("jean",22,"m",True)
print(pessoa)

del(pessoa)

#exercicios

#1. Crie uma tupla vazia.
tupla=()
#2. Crie uma tupla com 5 números inteiros.
tupla2=(1,2,3)
#3. Crie uma tupla com 3 strings.
tupla3= ("abacate","abacaxi","amora")
#4. Crie uma tupla mista com números inteiros e strings.
tupla4=(1,2,"macarrão",3,"cenoura")
#5. Acesse o primeiro elemento de uma tupla.
print(tupla2[0])
#6. Acesse o último elemento de uma tupla.
print(tupla3[-1])
#7. Acesse o terceiro elemento de uma tupla.
print(tupla4[2])
#8. Verifique o comprimento de uma tupla.
print(len(tupla4))
#9. Concatene duas tuplas.
print(tupla3+tupla4)
#10. Repita uma tupla 3 vezes.
for i in range(3):
    print(tupla4)
#11. Verifique se um elemento específico está presente na tupla.
print("Verificação se um elemento está na tupla")
print(2 in tupla4)
#12. Conte quantas vezes um elemento aparece na tupla.
# Definindo a tupla
minha_tupla = (1, 2, 3, 2, 4, 2, 5)

# Elemento que queremos contar
elemento = 2

# Contando quantas vezes o elemento aparece na tupla
contagem = minha_tupla.count(elemento)

print(f"O elemento {elemento} aparece {contagem} vezes na tupla.")

#13. Encontre o índice de um elemento específico na tupla.
# Definindo a tupla
minha_tupla = (10, 20, 30, 40, 50)

# Elemento que queremos encontrar o índice
elemento = 30

try:
    # Encontrando o índice do elemento
    indice = minha_tupla.index(elemento)
    print(f"O elemento {elemento} está no índice {indice}.")
except ValueError:
    print(f"O elemento {elemento} não está presente na tupla.")

#14. Verifique se uma tupla está vazia.
# Definindo a tupla
minha_tupla = ()

# Verificando se a tupla está vazia
if len(minha_tupla) == 0:
    print("A tupla está vazia.")
else:
    print("A tupla não está vazia.")
