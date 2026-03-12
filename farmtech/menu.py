from farmtech.talhao import (
    cadastrar_talhao,
    listar_talhoes,
    deletar_talhao,
    atualizar_talhao
)


def menu():

    while True:

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