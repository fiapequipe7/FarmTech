"""
    interface com usuário
"""
from farmtech.calculos import *
from farmtech.service import *
import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')
def pausar():
    input("\nPressione ENTER para continuar...")

def menu():

    while True:

        limparTela()

        print("""
╔══════════════════════════════╗
║        FARMTECH SYSTEM       ║
╚══════════════════════════════╝

[1] Cadastrar Talhão
[2] Listar Talhões
[3] Atualizar Talhão
[4] Remover Talhão
[0] Sair

--------------------------------
""")

        match input("Escolha: "):
            case  "1":
                adicionar_talhao()
            case "2":
                mostrar_talhoes()
            case "3":
                alterar_talhao()
            case "4":
                apagar_talhao()

            case "0":
                break

            case _:
                print("opçao invalida")

        pausar()

def mostrar_talhoes() -> bool:
    limparTela()
    lista_de_talhoes = listar_talhoes()

    if not lista_de_talhoes:
        print("⚠ Nenhum talhão cadastrado no sistema.")
        return False

    for i, talhao in enumerate(lista_de_talhoes):
        print("────────────────────────────────")
        print(f"ID:{i}")
        print(talhao)

    return True

def adicionar_talhao():
    while True:
        limparTela()
        print("=== Cadastro de Talhão ===")
        nome = input("Nome do talhão: ")
        print("Selecione o tipo de cultura:")
        print("[1] Cana de açúcar\n"
              "[2] Café Arabica")
        opcao = input("Escolha: ")
        if opcao == "1":
            cultura = "Cana-de-açúcar"
            print("Cálculo da área (retângulo)\n"
                  "Informe as dimensões do terreno:")
            while True:
                try:
                    base = float(input("Base: "))
                    altura = float(input("Altura: "))
                    area = calculo_retangulo(base, altura)
                    cadastrar_talhao(nome, cultura, area)
                    print("Talhão cadastrado!")
                    return
                except ValueError:
                    print("Por favor insira somente números")
                    continue


            break
        elif opcao == "2":
            cultura = "Café Arabica"
            print("Cálculo da área (trapézio) \n"
                  "Informe as dimensões do terreno:")
            while True:
                try:
                    base_maior = float(input("Base Maior: "))
                    base_menor = float(input("Base Menor: "))
                    while base_menor>base_maior:
                        print("A base menor deve ser menor que a base maior")
                        base_menor = float(input("Base Menor: "))
                    altura = float(input("Altura: "))
                    area = calculo_trapezio(base_maior, base_menor, altura)
                    cadastrar_talhao(nome, cultura, area)
                    print("✅ Talhão cadastrado com sucesso!")
                    return
                except ValueError:
                    print("❌ Valor inválido. Digite apenas números.")
                    continue
        else:
            print("Opção inválida")
            continue
    print("Talhão Cadastrado com sucesso!")
def alterar_talhao():
    if mostrar_talhoes():
        while True:
            entrada = input("Informe o ID do talhão que deseja atualizar: ")
            if entrada == "":
                match input("Deseja sair desta operação? (S/N): ").lower().strip():
                    case "s":
                        return
                    case "n":
                        continue
                    case _:
                        continue
            if not entrada.isdigit():
                print("❌ ID inválido. Tente novamente.")
                continue
            indice = int(entrada)
            if indice not in [x for x in range(len(listar_talhoes()))]:
                print("❌ ID inválido. Tente novamente.")
                continue
            while True:
                limparTela()
                print("Selecione o que deseja alterar:")
                print("[1] Nome \n"
                      "[2] Cultura\n"
                      "[3] Area\n"
                      "[0] Sair\n")

                match input("Escolha: "):
                    case "1":
                        novo_nome = input("Digite o novo nome do talhão: ")
                        if atualizar_talhao(indice,novo_nome=novo_nome):
                            print("✅ Talhão atualizado com sucesso!")
                            match input("Deseja Continuar atualizando os dados?(S/N)").lower().strip():
                                case "s":
                                    pausar()
                                case "n":
                                    return
                                case _:
                                    continue

                        else:
                            print("❌ Não foi possível atualizar o talhão.")
                            pausar()

                    case "2":
                        area = 0
                        while True:
                            print("Selecione o tipo de cultura:")
                            print("[1] Cana de açúcar\n"
                                  "[2] Café Arabica")
                            escolha = input("Escolha: ")
                            if escolha not in ["1","2"]:
                                print("Opção inválida")
                                continue
                            break

                        if escolha == "1":
                            print("Cálculo da área (retângulo)\n"
                                  "Informe as dimensões do terreno:")
                            while True:
                                try:
                                    base = float(input("Base: "))
                                    altura = float(input("Altura: "))
                                    area = calculo_retangulo(base, altura)
                                    break
                                except ValueError:
                                    print("Por favor insira somente números")
                                    continue
                        else:
                            print("Cálculo da área (trapézio) \n"
                                  "Informe as dimensões do terreno:")
                            while True:
                                try:
                                    base_maior = float(input("Base Maior: "))
                                    base_menor = float(input("Base Menor: "))
                                    while base_menor > base_maior:
                                        print("A base menor deve ser menor que a base maior")
                                        base_menor = float(input("Base Menor: "))
                                    altura = float(input("Altura: "))
                                    area = calculo_trapezio(base_maior, base_menor, altura)
                                    break
                                except ValueError:
                                    print("❌ Valor inválido. Digite apenas números.")
                                    continue
                        if atualizar_talhao(indice,nova_cultura=escolha,nova_area=area):
                            print("✅ Talhão atualizado com sucesso!")
                            match input("Deseja Continuar atualizando os dados?(S/N)").lower().strip():
                                case "s":
                                    pausar()
                                case "n":
                                    return
                                case _:
                                    continue

                        else:
                            print("❌ Não foi possível atualizar o talhão.")
                            pausar()

                    case "3":
                        nova_area = 0
                        if talhoes[indice].cultura == "Cana-de-açúcar":
                            print("Cálculo da área (retângulo)\n"
                                  "Informe as dimensões do terreno:")
                            while True:
                                try:
                                    base = float(input("Base: "))
                                    altura = float(input("Altura: "))
                                    nova_area = calculo_retangulo(base, altura)
                                    break
                                except ValueError:
                                    print("Por favor insira somente números")
                                    continue

                        else:
                            print("Cálculo da área (trapézio) \n"
                                  "Informe as dimensões do terreno:")
                            while True:
                                try:
                                    base_maior = float(input("Base Maior: "))
                                    base_menor = float(input("Base Menor: "))
                                    while base_menor > base_maior:
                                        print("A base menor deve ser menor que a base maior")
                                        base_menor = float(input("Base Menor: "))
                                    altura = float(input("Altura: "))
                                    nova_area = calculo_trapezio(base_maior, base_menor, altura)
                                    break
                                except ValueError:
                                    print("❌ Valor inválido. Digite apenas números.")
                                    continue
                        if atualizar_talhao(indice, nova_area=nova_area):
                            print("✅ Talhão atualizado com sucesso!")
                            match input("Deseja Continuar atualizando os dados?(S/N)").lower().strip():
                                case "s":
                                    pausar()
                                case "n":
                                    return
                                case _:
                                    continue

                        else:
                            print("❌ Não foi possível atualizar o talhão.")
                            pausar()
                    case "0":
                        return
                    case _:
                       print("opçao invalida")
                       pausar()

def apagar_talhao():
    if mostrar_talhoes():
        while True:
            entrada = input("Digite o ID do talhão para deletar: ")
            if entrada == "":
                sair = input("Deseja sair desta operação? (S/N): ")
                if sair.lower() == "n":
                    continue
                elif sair.lower() == "s":
                    return
                else:
                    continue
            if not entrada.isdigit():
                print("❌ ID inválido.")
                continue
            indice = int(entrada)
            if indice not in [x for x in range(len(listar_talhoes()))]:
                print("❌ ID inválido.")
                continue
            if deletar_talhao(indice):
                print("🗑 Talhão removido com sucesso!")
            else:
                print("❌ ID inválido.")
            return