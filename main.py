import json
import os

ARQUIVO = "cardapio.json"


def carregar_cardapio():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_cardapio(cardapio):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(cardapio, arquivo, indent=4, ensure_ascii=False)


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
           print ("\n-----  MENU  ----")
           # cliente()
           break
        case "2":
            print ("\n---  AREA DO FUNCIONÁRIO  ---")            
            break
        case "3": 
            print ("\nObrigado pela visita!")
            break
        case _: 
            print ("\nOpção inválida!")
            break