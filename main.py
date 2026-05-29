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


def cliente_cardapio():
    os.system('cls')
    print("-----  MENU  ----\n")
    print('Entradas')
    print('-' * 10)
    for i, e in enumerate(entradas, start=1):
        print(
            f'{i} - {e["Nome"]} / Preço: R$ {e["Preco"]:.2f} / Descrição: {e["Descricao"]}\n')
    print('\nPratos principais')
    print('-' * 10)
    for i, p in enumerate(pratos_principais, start=1):
        print(
            f'{i} - {p["Nome"]} / Preço: R$ {p["Preco"]:.2f} / Descrição: {p["Descricao"]}')
    print('\nSobremesas')
    print('-' * 10)
    for i, s in enumerate(sobremesas, start=1):
        print(
            f'{i} - {s["Nome"]} / Preço: R$ {s["Preco"]:.2f} / Descrição: {s["Descricao"]}')


def funcionario():
    os.system('cls')
    print("---  AREA DO FUNCIONÁRIO  ---\n")
    print("1 - Adcionar prato: ")
    print("2 - Remover prato: ")
    print("3 - Editar prato: ")
    escolha = int(input("\nO que voce deseja? "))

    match escolha:
        case 1:
            addprato()
        case 2:
            removeprato()
        case 3:
            editarprato()


def catprato():
    print("\n1 - Entrada")
    print("2 - Prato principal")
    print("3 - Sobremesa")
    cat = int(input("\nEscolha a categoria: "))
    return cat


def addprato():
    match catprato():
        case 1:
            entrada = {}
            entrada["Nome"] = input("Digite o nome da entrada: ")
            entrada["Preco"] = float(input("Digite o preco da entrada: "))
            entrada["Descricao"] = input("Digite a descricao: ")
            entradas.append(entrada)
            salvar_entradas(entradas)

        case 2:
            prato_principal = {}
            prato_principal["Nome"] = input(
                "Digite o nome do prato principal: ")
            prato_principal["Preco"] = float(
                input("Digite o preco do prato principal: "))
            prato_principal["Descricao"] = input(
                "Digite a descricao do prato principal: ")
            pratos_principais.append(prato_principal)
            salvar_pratos_principais(pratos_principais)

        case 2:
            sobremesa = {}
            sobremesa["Nome"] = input("Digite o nome da sobremsa: ")
            sobremesa["Preco"] = float(input("Digite o preco da sobremesa: "))
            sobremesa["Descricao"] = input("Digite a descricao: ")
            sobremesas.append(sobremesa)
            salvar_sobremesas(sobremesas)


def removeprato():
    cliente_cardapio()
    print('\nRemovendo um prato')
    print('-' * 10)
    print('[1] - Entrada')
    print('[2] - Principal')
    print('[3] - Sobremesa\n')
    choicecat = int(input("Digite a categoria do prato: "))
    choice = int(input("Digite o número do prato: "))
    indice = choice - 1

    match choicecat:
        case 1:
            entrada_removida = entradas[indice]["Nome"]
            del entradas[indice]
            salvar_entradas(entradas)
            print(f"\n{entrada_removida} removida com sucesso!\n")
            input('Pressione ENTER para continuar...')

        case 2:
            principal_removido = pratos_principais[indice]["Nome"]
            del pratos_principais[indice]
            salvar_pratos_principais(pratos_principais)
            print(f"\n{principal_removido} removido com sucesso!\n")
            input('Pressione ENTER para continuar...')


while True:
    os.system('cls')
    print("\n ---------------------------")
    print("|        BEM-VINDO AO       |")
    print("|      Bandeijão da PUC     |")
    print(" ---------------------------\n")

    print("[1] - Sou cliente")
    print("[2] - Sou funcionário")
    print("[3] - Sair")

    opcao = int(input("Escolha uma das opções acima: "))

    match opcao:
        case 1:
            cliente_cardapio()
            input('Pressione ENTER para continuar...')
        case 2:
            funcionario()
        case 3:
            print("\nObrigado pela visita!")
            break
        case _:
            print("\nOpção inválida!")
