"""
    interface com usuário
"""
from src.farmtech.calculos import *
from src.farmtech.service import *
import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():

    while True:

        limparTela()

        print("""
====== FARMTECH ======

1 - Cadastrar talhao
2 - Listar talhoes
3 - Atualizar talhao
4 - Deletar talhao
0 - Sair

""")

        match input("Escolha: "):
            case  "1":
                while True:
                    limparTela()
                    print("Cadastrando talhão......")
                    nome = input("Nome do talhão: ")
                    print("Escolha uma cultura.....")
                    print("1 - Cana de açúcar\n"
                          "2 - Café Arabica")
                    opcao = input("Escolha: ")
                    if opcao== "1":
                        cultura = "Cana-de-açúcar"
                        print("Calculando a área(retângulo).........")
                        base = float(input("Base: "))
                        altura = float(input("Altura: "))
                        area = calculo_retangulo(base,altura)
                        cadastrar_talhao(nome, cultura, area)
                        break
                    elif opcao == "2":
                        cultura = "Café Arabica"
                        print("Calculando a área(Trapézio).............")
                        base_maior = float(input("Base Maior: "))
                        base_menor = float(input("Base Menor: "))
                        altura = float(input("Altura: "))
                        area = calculo_trapezio(base_maior,base_menor,altura)
                        cadastrar_talhao(nome, cultura, area)
                        break
                    else:
                        print("Opção inválida")
                        continue
                print("Talhão Cadastrado com sucesso!")

            case "2":
                lista_de_talhoes = listar_talhoes()
                if not lista_de_talhoes:
                    print("Nenhum Talhão cadastrado")
                    continue
                for i,talhao in enumerate(lista_de_talhoes):
                    print("======================================")
                    print(f"ID:{i}",talhao)

            case "3":
                if not listar_talhoes():
                    print("Nenhum Talhão cadastrado")
                    continue
                for i,talhao in enumerate(talhoes):
                    print("======================================")
                    print(i,talhao)
                entrada = input("Digite o ID para atualizar: ")

                if not entrada.isdigit():
                    print("ID inválido")
                    continue

                indice = int(entrada)

                novo_nome = input("Novo nome do talhão: ")

                if atualizar_talhao(indice, novo_nome):
                    print("Talhão atualizado")
                else:
                    print("Não foi possível atualizar o talhão")
            case "4":
                deletar_talhao()

            case "0":
                break

            case _:
                print("opçao invalida")

        input("\nPressione Enter para continuar...")
