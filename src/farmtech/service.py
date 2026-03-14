"""
    lógica de manipulação de dados, cadastro, listagem, atualização e remoção
"""

from src.farmtech.storage import talhoes
from src.farmtech.talhao import Talhao

def cadastrar_talhao(nome:str,cultura:str,area) -> None:

    novo_talhao = Talhao(nome, cultura, area)
    talhoes.append(novo_talhao)
def listar_talhoes() -> list:
    return talhoes

def deletar_talhao(indice: int) -> bool:
    if not 0 <= indice < len(talhoes):
        return False
    talhoes.pop(indice)
    return True


def atualizar_talhao(indice: int, novo_nome: str) -> bool:

    if not 0 <= indice < len(talhoes):
        return False

    if not novo_nome:
        return False

    talhoes[indice].nome = novo_nome
    return True