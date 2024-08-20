#A manipulação de arquivos é uma importante tarefa em muitas linguagens de programação. Trata-se de uma forma de tentar extrair informações de um arquivo ou uma fonte externa, o que é um começo para que o programador entenda como tornar sua aplicação mais robusta.
#É comum começar a estudar essa questão com arquivos TXT, menores e mais simples. Logo depois, contudo, é interessante evoluir para trabalhar com arquivos, maiores e mais complexos, como CSV. A lógica é muito similar e até alguns métodos são iguais.
#Em Python e em outras linguagens, temos três principais métodos: ler, escrever e adicionar.
#Vamos começar explicando como eles funcionam de forma mais genérica. Depois partiremos para o código. 
#Ler arquivo TXT em Python
##A leitura de um arquivo consiste em tentar extrair as informações presentes no arquivo para trazer para a memória. Então, com outros métodos, é possível manipular como o programador deseja, seja separar linha por linha, seja separar com base em algum marcador separador, seja pegar cada palavra, etc.
#A ideia é extrair as informações e jogar em algum variável ou dispô-las na tela. 
#Isso pode ser muito útil em várias aplicações. Uma delas, por exemplo, é para testar modelos de inteligência artificial. Você pode fazer isso para testar sistemas de recomendação ou sistemas de processamento de linguagem natural (PLN).
#No caso de aplicações de PLN, o programador pode escrever frases em um arquivo e depois importá-las no Python para facilitar e testar de fato como o modelo reage.

#1 Primeira função : a open abre um arquivo já pré criado ou cria o arquivo
#open()
#comando que vai abrir o arquivo.txt ou crialo e o parâmetro W define ser um arquivo write ou seja escrita
arquivo=open("arquivo.txt",'w')

#2 segunda função é a write que você vai inserir o texto no arquivo

arquivo.write("Curso Python \n")
arquivo.write('Aula prática')

#3 terceira função é a close que fecha o arquivo, sendo OBRIGATORIO o encerramento

arquivo.close()

#4 quarta função é a read ao qual você joga o arquivo dentro de uma varievel para ser a leitora, utilizando o comando open porém com o parâmetro r

leitura= open('arquivo.txt','r')
print(leitura.read())
leitura.close()

#Exercicios

#1. Criar arquivo vazio: Crie um programa que cria um arquivo vazio chamado
#exercicio1.txt.
ex1=open("exercicio1.txt","w")
ex1.close()
#2. Escrever em um arquivo: Crie um programa que escreve a mensagem
#"Estou aprendendo Python!" em um arquivo chamado mensagem.txt.
ex2=open("mensagem.txt",'w')
ex2.write("Estou aprendendo python")
ex2.close()
#3. Escrever múltiplas linhas: Crie um programa que escreve três linhas de texto
#em um arquivo chamado notas.txt.
ex3=open("exercicio3.txt",'w')
for i in range(1, 4):
    # Solicita ao usuário a frase
    frase = input("Digite a {} frase: ".format(i))
    # Escreve a frase no arquivo com uma nova linha no final
    ex3.write(frase + '\n')
ex3.close()
#4. Escrever números em arquivo: Crie um programa que escreve os números
#de 1 a 10 em um arquivo chamado numeros.txt, um número por linha.
ex4=open("exercicio4.txt",'w')
for i in range(1, 11):
    ex4.write(str(i) + '\n')
ex4.close()
#6. Ler conteúdo de um arquivo: Crie um programa que lê e exibe o conteúdo do
#arquivo exercicio1.txt na tela.
# Abre o arquivo 'exercicio.txt' para escrita usando o context manager
with open("exercicio1.txt", 'w') as ex1:
    # Escreve uma string longa no arquivo
    ex1.write("O Python é uma linguagem de programação, como você já deve ter ouvido falar de várias outras que existem.\n"
              "Só que foi desenvolvido para ser simples, fácil de aprender e muito versátil, ou seja, você vai poder utilizar essa linguagem para diversas tarefas.\n"
              "Pode construir aplicativos, criar sites, desenvolver programas, criar jogos, fazer análise de dados, inteligência artificial, entre outras atividades.\n"
              "Ao aprender o que é Python, você tem muitas opções. Como é uma linguagem mais fácil de aprender, é excelente para você começar no mundo da programação.")

leitura2=open("exercicio1.txt",'r')
print(leitura2.read())
leitura2.close()