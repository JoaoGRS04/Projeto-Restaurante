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
           editpreco()


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