"""
    lógica de manipulação de dados, cadastro, listagem, atualização e remoção
"""

from src.farmtech.storage import talhoes
from src.farmtech.talhao import Talhao

def cadastrar_talhao(nome:str,cultura:str,area) -> None:

    novo_talhao = Talhao(nome, cultura, area)
    talhoes.append(novo_talhao)


def listar_talhoes() -> list|None:
    return talhoes


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