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