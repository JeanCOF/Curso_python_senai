"""
x = input("Digite algo: ")

try:
    x = int(x)
    print("A variável é do tipo inteiro")
except ValueError:
    print("A variável não é do tipo inteiro")

"""
i = 0
while i != 1:
    i = int(input("Digite 1 para encerrar ou 0 para continuar: "))
    if i == 1:
        print("Encerrando o programa.")
        break  # Encerra o loop se o usuário digitou 1
    elif i > 1 or i < 0:
        print("ERRO: Digite 1 para encerrar ou 0 para continuar")
        continue  # Volta ao início do loop para pedir a entrada novamente
    
    var = input("Digite algo: ")

    if var.isalpha():
        print("O valor digitado é uma string.")
        if var.isupper():
            print("O valor está em maiúsculas.")
        elif var.islower():
            print("O valor está em minúsculas.")
        elif var.istitle():
            print("O valor começa com maiúscula e as outras letras estão em minúsculas.")
    elif var.isspace():
        print("O valor está em branco.")
    elif var.isnumeric():
        print("O valor é numérico.")
    elif var.isalnum():
        print("O valor é alfanumérico (apenas números e letras).")
    else:
        print("O valor não é reconhecido como uma string válida, numérica ou alfanumérica.")

        
def obter_cpf():
    while True:
        cpf = input("Digite o CPF (somente números, 11 dígitos): ")
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        else:
            print("ERRO: O CPF deve ter 11 dígitos numéricos.")

def obter_nome():
    while True:
        nome = input("Digite o nome (somente letras e espaços): ")
        if nome.replace(" ", "").isalpha():
            return nome
        else:
            print("ERRO: O nome deve conter apenas letras e espaços.")

def obter_idade():
    while True:
        idade_str = input("Digite a idade (número inteiro): ")
        if idade_str.isdigit():
            idade = int(idade_str)
            if idade >= 0:
                return idade
            else:
                print("ERRO: A idade não pode ser negativa.")
        else:
            print("ERRO: A idade deve ser um número inteiro.")

def formulario():
    print("Preencha o formulário:")
    
    cpf = obter_cpf()
    nome = obter_nome()
    idade = obter_idade()
    
    print("\nFormulário preenchido com sucesso!")
    print(f"CPF: {cpf}")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

# Executa o formulário
formulario()
