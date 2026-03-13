"""
    lógica de manipulação de dados, cadastro, listagem, atualização e remoção
"""

from farmtech.storage import talhoes
from farmtech.talhao import Talhao

def cadastrar_talhao():
    nome = input("Nome do talhão: ")

    if nome == "":
        print("Atualização cancelada")
        return

    print("Escolha a cultura")
    print("1 - Cana de açúcar")
    print("2 - Café Arabica")

    opcao = input("Opção: ")

    if opcao == "1":
        cultura = "Cana-de-açúcar"
    elif opcao == "2":
        cultura = "Café Arabica"
    else:
        print("Opção inválida")
        return

    # Área à ser calculada 
    area = 0

    # Custo também
    insumos = 0

    novo_talhao = Talhao(nome, cultura, area, insumos)
    talhoes.append(novo_talhao)

    print("Talhão cadastrado com sucesso!")


def listar_talhoes():
    if len(talhoes) == 0:
        print("Nenhum talhão cadastrado")
        return

    for i, talhao in enumerate(talhoes):
        print(f"""ID: {i}
        Nome: {talhao.nome}
        Cultura: {talhao.cultura}
        Área: {talhao.area}
        Insumos: {talhao.insumos}
        """)


def deletar_talhao():
    if len(talhoes) == 0:
        print("Nenhum talhão cadastrado")
        return
    else:
        listar_talhoes()
        entrada = input("Digite o ID do talhão para deletar: ")

        # Validação para garantir que a entrada seja um número e não uma string vazia ou um valor não numérico
        if entrada == "" or not entrada.isdigit():
            print("ID inválido")
            return

        indice = int(entrada)

        if 0 <= indice < len(talhoes):
            talhoes.pop(indice)
            print("Talhão removido")
        else:
            print("ID inválido")


def atualizar_talhao():
    if len(talhoes) == 0:
        print("Nenhum talhão cadastrado")
        return
    else:
        listar_talhoes()
        entrada = input("Digite o ID para atualizar: ")

        # Validação para garantir que a entrada seja um número e não uma string vazia ou um valor não numérico
        if entrada == "" or not entrada.isdigit():
            print("ID inválido")
            return

        indice = int(entrada)

        if 0 <= indice < len(talhoes):
            novo_nome = input("Novo nome do talhão: ")

            if novo_nome == "":
                print("Atualização cancelada")
                return
            talhoes[indice].nome = novo_nome
            print("Talhão atualizado")
        else:
            print("ID inválido")