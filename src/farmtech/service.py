"""
    lógica de manipulação de dados, cadastro, listagem, atualização e remoção
"""

from src.farmtech.storage import talhoes
from src.farmtech.talhao import Talhao

def cadastrar_talhao(nome:str,cultura:str,area) -> None:

    novo_talhao = Talhao(nome, cultura, area)
    talhoes.append(novo_talhao)


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


def atualizar_talhao(indice: int, novo_nome: str) -> bool:

    if not 0 <= indice < len(talhoes):
        return False

    if not novo_nome:
        return False

    talhoes[indice].nome = novo_nome
    return True