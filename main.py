import json
import os

ARQUIVO_ENTRADAS = "entradas.json"
ARQUIVO_PRATOS = "pratos_principais.json"
ARQUIVO_SOBREMESAS = "sobremesas.json"


def carregar_entradas():
    if os.path.exists(ARQUIVO_ENTRADAS):
        with open(ARQUIVO_ENTRADAS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_entradas(entradas):
    with open(ARQUIVO_ENTRADAS, "w", encoding="utf-8") as arquivo:
        json.dump(entradas, arquivo, indent=4, ensure_ascii=False)


def carregar_pratos_principais():
    if os.path.exists(ARQUIVO_PRATOS):
        with open(ARQUIVO_PRATOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_pratos_principais(pratos_principais):
    with open(ARQUIVO_PRATOS, "w", encoding="utf-8") as arquivo:
        json.dump(pratos_principais, arquivo, indent=4, ensure_ascii=False)


def carregar_sobremesas():
    if os.path.exists(ARQUIVO_SOBREMESAS):
        with open(ARQUIVO_SOBREMESAS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_sobremesas(sobremesas):
    with open(ARQUIVO_SOBREMESAS, "w", encoding="utf-8") as arquivo:
        json.dump(sobremesas, arquivo, indent=4, ensure_ascii=False)

def funcionario():
   print("1 - adcionar prato: ")
   print("2 - remover prato: ")
   print("3 - editar preco: ")
   escolha = print("o que voce deseja? ")

   match escolha:
       case "1":
           addprato()
       case "2":
           removeprato()
       case "3":
           editarprato()


def catprato():
    print("1 -  entrada")
    print("2 - prato principal")
    print("3 -  sobremesa")
    cat = input("Escolha a categoria")
    return cat

def addprato():
    match cat:
        case "1":
            entrada = {}
            entrada["Nome"] = input("Digite o nome da entrada: ")
            entrada["Preco"] = input("Digite o preco da entrada: ")
            entrada["Descricao"] = input("Digite a descricao: ")
            entradas.append(entrada)
            salvar_entradas(entradas)

        case "2":
            prato_principal = {}
            prato_principal["Nome"] = input("Digite o nome do prato_principal: ")
            prato_principal["Preco"] = input("Digite o preco do prato principal: ")
            prato_principal["Descricao"] = input("Digite a descricao do prato principal: ")
            pratos_principais.append(prato_principal)
            salvar_pratos_principais(pratos_principais)


        case "3":
            sobremesa = {}
            sobremesa["Nome"] = input("Digite o nome da sobremsa: ")
            sobremesa["Preco"] = input("Digite o preco da sobremesa: ")
            sobremesa["Descricao"] = input("Digite a descricao: ")
            sobremesas.append(entrada)
            salvar_entradas(sobremesas)

def removeprato():
    choicecat = input ("Digite a categoria do prato: ")
    choice = input("Digite o índice do prato: ")
    indice = int(choice)

    match choicecat:
        case "1":
            del entradas[indice]
            salvar_entradas(entradas)
            print("Entrada removida com sucesso!")
            
        case "2":
            del pratos_principais[indice]
            salvar_pratos_principais(pratos_principais)
            print("Prato principal removido com sucesso!")
            
        case "3":
            del sobremesas[indice]
            salvar_sobremesas(sobremesas)
            print("Sobremesa removida com sucesso!")
            
def editarprato():
    choicecat = input("Digite a categoria do prato (1-Entrada, 2-Principal, 3-Sobremesa): ")
    choice = input("Digite o índice do prato que deseja editar: ")
    
    indice = int(choice)

    match choicecat:
        case "1":
            # Busca o prato atual para mostrar ao usuário
            prato_atual = entradas[indice]
            print(f"\nEditando: {prato_atual['Nome']}")
            
            # Pede os novos dados
            prato_atual["Nome"] = input("Digite o NOVO nome da entrada: ")
            prato_atual["Preco"] = input("Digite o NOVO preco da entrada: ")
            prato_atual["Descricao"] = input("Digite a NOVA descricao: ")
            
            salvar_entradas(entradas)
            print("Entrada atualizada com sucesso!")
            
        case "2":
            prato_atual = pratos_principais[indice]
            print(f"\nEditando: {prato_atual['Nome']}")
            
            prato_atual["Nome"] = input("Digite o NOVO nome do prato principal: ")
            prato_atual["Preco"] = input("Digite o NOVO preco do prato principal: ")
            prato_atual["Descricao"] = input("Digite a NOVA descricao do prato principal: ")
            
            salvar_pratos_principais(pratos_principais)
            print("Prato principal atualizado com sucesso!")
            
        case "3":
            prato_atual = sobremesas[indice]
            print(f"\nEditando: {prato_atual['Nome']}")
            
            prato_atual["Nome"] = input("Digite o NOVO nome da sobremesa: ")
            prato_atual["Preco"] = input("Digite o NOVO preco da sobremesa: ")
            prato_atual["Descricao"] = input("Digite a NOVA descricao: ")
            
            salvar_sobremesas(sobremesas)
            print("Sobremesa atualizada com sucesso!")


while True:
    print("\n ---------------------------")
    print("|        BEM-VINDO AO       |")
    print("|      Bandeijão da PUC     |")
    print(" ---------------------------\n")

    print("[1] - Sou cliente")
    print("[2] - Sou funcionário")
    print("[3] - Sair")

    opcao = input("Escolha uma das opções acima: ")

    match opcao:
        case "1":
            print("\n-----  MENU  ----")
            # cliente()
        case "2":
            print("\n---  AREA DO FUNCIONÁRIO  ---")
            # funcionario()
        case "3":
            print("\nObrigado pela visita!")
        case _:
            print("\nOpção inválida!")
