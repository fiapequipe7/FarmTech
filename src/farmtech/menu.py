"""
    interface com usuário
"""
from farmtech.calculos import *
from farmtech.service import *
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

        input("\nPressione Enter para continuar...")

def mostrar_talhoes() -> bool:
    limparTela()
    lista_de_talhoes = listar_talhoes()

    if not lista_de_talhoes:
        print("Nenhum talhão foi cadastrado")
        return False

    for i, talhao in enumerate(lista_de_talhoes):
        print("======================================")
        print(f"ID:{i}")
        print(talhao)

    return True

def adicionar_talhao():
    while True:
        limparTela()
        print("Cadastrando talhão......")
        nome = input("Nome do talhão: ")
        print("Escolha uma cultura.....")
        print("1 - Cana de açúcar\n"
              "2 - Café Arabica")
        opcao = input("Escolha: ")
        if opcao == "1":
            cultura = "Cana-de-açúcar"
            print("Calculando a área(retângulo).........")
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            area = calculo_retangulo(base, altura)
            cadastrar_talhao(nome, cultura, area)
            break
        elif opcao == "2":
            cultura = "Café Arabica"
            print("Calculando a área(Trapézio).............")
            base_maior = float(input("Base Maior: "))
            base_menor = float(input("Base Menor: "))
            altura = float(input("Altura: "))
            area = calculo_trapezio(base_maior, base_menor, altura)
            cadastrar_talhao(nome, cultura, area)
            break
        else:
            print("Opção inválida")
            continue
    print("Talhão Cadastrado com sucesso!")
def alterar_talhao():
    if mostrar_talhoes():
        while True:
            entrada = input("Digite o ID para atualizar: ")

            if not entrada.isdigit():
                print("ID inválido")
                continue

            indice = int(entrada)
            if indice not in [x for x in range(len(listar_talhoes()))]:
                print("ID invalido")
                continue
            novo_nome = input("Novo nome do talhão: ")

            if atualizar_talhao(indice, novo_nome):
                print("Talhão atualizado")
                return
            else:
                print("Não foi possível atualizar o talhão")
                return

def apagar_talhao():
    if mostrar_talhoes():
        while True:
            entrada = input("Digite o ID do talhão para deletar: ")

            # Validação para garantir que a entrada seja um número e não uma string vazia ou um valor não numérico
            if entrada == "" or not entrada.isdigit():
                print("ID inválido")
                continue
            indice = int(entrada)
            if indice not in [x for x in listar_talhoes()]:
                print("ID invalido")
                continue
            if deletar_talhao(indice):
                print("Talhão removido")
            else:
                print("ID inválido")
            return