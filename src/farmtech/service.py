"""
    lógica de manipulação de dados, cadastro, listagem, atualização e remoção
"""

from farmtech.storage import talhoes,insumos
from farmtech.talhao import Talhao

from farmtech.calculos import calculo_insumos


def cadastrar_talhao(nome:str,cultura:str,area) -> None:
    lista_insumos = []
    if cultura == "Café Arabica":
        lista_insumos = calculo_insumos(area,insumos[0])
    else:
        lista_insumos = calculo_insumos(area,insumos[1])
    novo_talhao = Talhao(nome, cultura, area,lista_insumos)
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