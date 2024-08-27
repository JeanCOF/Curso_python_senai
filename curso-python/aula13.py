#Os dicionários são uma estrutura de dados fundamental em Python, usada para armazenar pares de chave-valor. Os dicionários funcionam de forma similar as listas no Python, só que você pode atribuir rótulos aos dados.
##Com os dicionários podemos organizar os dados de maneira que possamos acessá-lo de forma intuitiva e eficiente.
#Ao contrário das listas, onde os elementos são acessados por índices numéricos, os dicionários utilizam chaves únicas.
#Dessa forma, você consegue acessar os dados de acordo com os rótulos correspondentes. Por exemplo, ao invés de ter uma lista com as idades dos clientes, você pode ter um dicionário com o nome como a chave e a idade como valor. Facilitando o acesso e a organização dos dados.
#Nesta aula você verá o que são os dicionários Python e como utilizá-los em seus códigos para otimizar e obter melhor resultado deles.

pessoa={"nome":"jean","idade": 22, "gatos":["baji","logan"]}

carro={"marca": "Volkswagen","modelo":"gol","ano": 2020}

auto={"tipo":"moto","marca": "yamaha","modelo":"crosser","ano": 2019}

produtos=[
    {"id": 783,"tipo":"forno","ano":2020},
    {"id": 467,"tipo":"geladeira","ano":2020},
    {"id": 433,"tipo":"celular","ano":2020}
]

lista_tel={"frnaca":"777-777","batatais": "888-888"}

vazio={}

informacao={}

informacao["nome"] = "Jean"

informacao["ocupacao"]= "programador junior"

print(informacao)

informacao["ocupacao"]= "programador senior"

print(informacao)

capitais={"Brasil":"Brasilia","Alemanha":"Berlim","Japao":"Toquio"}
pais= str(input("Digite um páis: "))

if pais in capitais:
    capital = capitais[pais]
    print("A capital de {} é {}".format(pais,capital))
else:
    print("A capita de {} não foi encontrada no dicionário: ".format(pais))

capitais["Italia"]= "Roma"
capital_italia=capitais["Italia"]
print(capital_italia)

capitais["Italia"]="???"

print(capital_italia)

del capitais["Brasil"]
print(capitais)

#1. Crie um dicionário vazio.
dicio1={}
#2. Crie um dicionário com 3 pares chave-valor de strings.
dicio2={"nome":"jean","bairro":"leporace","cidade":"franca"}
#3. Acesse o valor de uma chave específica em um dicionário.
print(dicio2["nome"])
#4. Adicione um novo par chave-valor a um dicionário.
dicio2["idade"]= 22
#5. Remova um par chave-valor de um dicionário usando a função pop.
dicio2.pop()
#6. Verifique se uma chave específica está presente em um dicionário.
print("verificação se bairro está no dicionário")
print("bairro" in dicio2)
#7. Verifique se um valor específico está presente em um dicionário.
print("verificação se leporace está no dicionário")
print("leporace" in dicio2["bairro"])
#8. Conte quantos pares chave-valor um dicionário possui.
print("Quantidade de elementos no didionário")
print(len(dicio2))
#9. Copie um dicionário para outro.
dicio3= dicio2
print(dicio3)
#10. Limpe todos os itens de um dicionário.
dicio3.clear()
print(dicio3)
#11. Crie um dicionário com tipos de frutas e seus respectivos preços.
dicio4={"banana":2.50,"maca":1.75,"uva":4.00}
print(dicio4)
#12. Atualize o valor de uma chave específica em um dicionário.
dicio4["banana"] = 2.30
print(dicio4)
#13. Junte dois dicionários usando o método update.
dicio5={"mamao":3.25,"laranja":2.00}
dicio4.update(dicio5)
print(dicio4)
#14. Acesse todas as chaves de um dicionário usando o método `keys`.
# Definindo o dicionário

# Acessando todas as chaves usando o método keys()
chaves = dicio4.keys()

# Convertendo a visão das chaves para uma lista para facilitar a visualização
lista_chaves = list(chaves)

print(lista_chaves)

#15. Crie um dicionário com informações sobre rios (nome, extensão, país de
#origem, etc.).
# Criando um dicionário com informações sobre rios
rios = [
    {
        'nome': 'Amazonas',
        'extensao_km': 6992,
        'pais_origem': 'Peru',
        'bacia': 'Bacia do Amazonas',
        'desembocadura': 'Oceano Atlântico'
    },
    {
        'nome': 'Nilo',
        'extensao_km': 6650,
        'pais_origem': 'Burundi',
        'bacia': 'Bacia do Nilo',
        'desembocadura': 'Mar Mediterrâneo'
    },
    {
        'nome': 'Yangtze',
        'extensao_km': 6300,
        'pais_origem': 'China',
        'bacia': 'Bacia do Yangtze',
        'desembocadura': 'Mar da China Oriental'
    },
    {
        'nome': 'Mississippi',
        'extensao_km': 3730,
        'pais_origem': 'Estados Unidos',
        'bacia': 'Bacia do Mississippi',
        'desembocadura': 'Golfo do México'
    }
]

#16. Crie um dicionário com informações sobre oceanos (nome, área,
#profundidade média, etc.).
# Criando um dicionário com informações sobre oceanos
oceanos = {
    'Oceano Pacífico': {
        'área_km2': 168_723_000,
        'profundidade_média_m': 4_280,
        'profundidade_maxima_m': 10_994,
        'localização': 'Entre a Ásia, Austrália, América do Norte e América do Sul'
    },
    'Oceano Atlântico': {
        'área_km2': 106_460_000,
        'profundidade_média_m': 3_646,
        'profundidade_maxima_m': 8_376,
        'localização': 'Entre a América do Norte e América do Sul, e a Europa e África'
    },
    'Oceano Índico': {
        'área_km2': 70_560_000,
        'profundidade_média_m': 3_741,
        'profundidade_maxima_m': 7_258,
        'localização': 'Entre a África, Ásia, Austrália e a Índia'
    },
    'Oceano Ártico': {
        'área_km2': 15_558_000,
        'profundidade_média_m': 1_205,
        'profundidade_maxima_m': 5_450,
        'localização': 'No Ártico, cercado pela América do Norte, Europa e Ásia'
    }
}


#17. Crie um dicionário com informações sobre esportes (nome, modalidades,
#país de origem, etc.).
# Criando um dicionário com informações sobre esportes
esportes = {
    'Futebol': {
        'modalidades': ['11 jogadores', 'Futsal', 'Futebol de Areia'],
        'país_de_origem': 'Inglaterra',
        'origem': 'Século XIX',
        'popularidade': 'Alta'
    },
    'Basquete': {
        'modalidades': ['Basquete', 'Basquete de Rua', 'Basquete 3x3'],
        'país_de_origem': 'Estados Unidos',
        'origem': '1891',
        'popularidade': 'Alta'
    },
    'Tênis': {
        'modalidades': ['Tênis de Campo', 'Tênis de Mesa', 'Tênis de Praia'],
        'país_de_origem': 'França',
        'origem': 'Século XII',
        'popularidade': 'Média'
    },
    'Judô': {
        'modalidades': ['Judô', 'Judô Paralímpico'],
        'país_de_origem': 'Japão',
        'origem': '1882',
        'popularidade': 'Média'
    },
    'Críquete': {
        'modalidades': ['Críquete de Teste', 'Críquete ODI', 'Críquete T20'],
        'país_de_origem': 'Inglaterra',
        'origem': 'Século XVI',
        'popularidade': 'Alta'
    }
}

#18. Crie um dicionário com informações sobre artistas de cinema (nome, filmes
#famosos, prêmios recebidos, etc.).
# Criando um dicionário com informações sobre artistas de cinema
artistas = {
    'Meryl Streep': {
        'filmes_famosos': ['O Diabo Veste Prada', 'A Escolha de Sofia', 'Kramer vs. Kramer'],
        'prêmios_recebidos': ['Oscar', 'Globo de Ouro', 'BAFTA'],
        'nacionalidade': 'Americana',
        'ano_nascimento': 1949
    },
    'Leonardo DiCaprio': {
        'filmes_famosos': ['A Origem', 'O Lobo de Wall Street', 'O Regresso'],
        'prêmios_recebidos': ['Oscar', 'Globo de Ouro', 'BAFTA'],
        'nacionalidade': 'Americana',
        'ano_nascimento': 1974
    },
    'Cate Blanchett': {
        'filmes_famosos': ['O Senhor dos Anéis', 'Blue Jasmine', 'Thor: Ragnarok'],
        'prêmios_recebidos': ['Oscar', 'Globo de Ouro', 'BAFTA'],
        'nacionalidade': 'Australiana',
        'ano_nascimento': 1969
    },
    'Denzel Washington': {
        'filmes_famosos': ['Dia de Treinamento', 'Malcolm X', 'Fences'],
        'prêmios_recebidos': ['Oscar', 'Globo de Ouro', 'BAFTA'],
        'nacionalidade': 'Americana',
        'ano_nascimento': 1954
    },
    'Penélope Cruz': {
        'filmes_famosos': ['Volver', 'Vicky Cristina Barcelona', 'Piratas do Caribe: Navegando em Águas Misteriosas'],
        'prêmios_recebidos': ['Oscar', 'Globo de Ouro', 'Premio Goya'],
        'nacionalidade': 'Espanhola',
        'ano_nascimento': 1974
    }
}

#19. Crie um dicionário com informações sobre marcas de roupas (nome, país de
#origem, estilo, etc.).
# Criando um dicionário com informações sobre marcas de roupas
marcas_roupas = {
    'Gucci': {
        'país_de_origem': 'Itália',
        'estilo': 'Luxo',
        'ano_fundação': 1921,
        'fundador': 'Guccio Gucci'
    },
    'Nike': {
        'país_de_origem': 'Estados Unidos',
        'estilo': 'Esportivo',
        'ano_fundação': 1964,
        'fundador': 'Phil Knight e Bill Bowerman'
    },
    'Chanel': {
        'país_de_origem': 'França',
        'estilo': 'Luxo',
        'ano_fundação': 1910,
        'fundador': 'Coco Chanel'
    },
    'Adidas': {
        'país_de_origem': 'Alemanha',
        'estilo': 'Esportivo',
        'ano_fundação': 1949,
        'fundador': 'Adi Dassler'
    },
    'Zara': {
        'país_de_origem': 'Espanha',
        'estilo': 'Casual',
        'ano_fundação': 1974,
        'fundador': 'Amancio Ortega e Rosalía Mera'
    }
}

