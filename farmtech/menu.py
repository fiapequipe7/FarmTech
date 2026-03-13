"""
    interface com usuário
"""


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

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_talhao()

        elif opcao == "2":
            listar_talhoes()

        elif opcao == "3":
            atualizar_talhao()

        elif opcao == "4":
            deletar_talhao()

        elif opcao == "0":
            break

        else:
            print("Opcao invalida")

        input("\nPressione Enter para continuar...")