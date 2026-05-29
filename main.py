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


entradas = carregar_entradas()
pratos_principais = carregar_pratos_principais()
sobremesas = carregar_sobremesas()


def funcionario():
    os.system('cls')
    print("---  AREA DO FUNCIONÁRIO  ---\n")
    print("1 - Adcionar prato: ")
    print("2 - Remover prato: ")
    print("3 - Editar preco: ")
    escolha = int(input("\nO que voce deseja? "))

    match escolha:
        case 1:
            addprato()
        case 2:
            removeprato()
        case 3:
            editpreco()


def catprato():
    print("\n1 - Entrada")
    print("2 - Prato principal")
    print("3 - Sobremesa")
    cat = input("\nEscolha a categoria: ")
    return cat


def addprato():
    match catprato():
        case "1":
            entrada = {}
            entrada["Nome"] = input("Digite o nome da entrada: ")
            entrada["Preco"] = float(input("Digite o preco da entrada: "))
            entrada["Descricao"] = input("Digite a descricao: ")
            entradas.append(entrada)
            salvar_entradas(entradas)

        case "2":
            prato_principal = {}
            prato_principal["Nome"] = input(
                "Digite o nome do prato principal: ")
            prato_principal["Preco"] = float(
                input("Digite o preco do prato principal: "))
            prato_principal["Descricao"] = input(
                "Digite a descricao do prato principal: ")
            pratos_principais.append(prato_principal)
            salvar_pratos_principais(pratos_principais)

        case "3":
            sobremesa = {}
            sobremesa["Nome"] = input("Digite o nome da sobremsa: ")
            sobremesa["Preco"] = float(input("Digite o preco da sobremesa: "))
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
    print("[4] - Reclamação/sugestão")
    print("[3] - Sair")

    opcao = int(input("Escolha uma das opções acima: "))

    match opcao:
        case "1":
            print("\n-----  MENU  ----")
            # cliente()
        case "2":
            print("\n---  AREA DO FUNCIONÁRIO  ---")
            # funcionario()
        case "3":
            print("\nObrigado pela visita!")
            break
        case _:
            print("\nOpção inválida!")
