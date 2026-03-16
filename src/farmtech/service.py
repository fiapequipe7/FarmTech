"""
    lógica de manipulação de dados, cadastro, listagem, atualização e remoção
"""
from pathlib import Path
import csv
from farmtech.storage import *
from farmtech.talhao import *
from farmtech.calculos import *

def export_csv():
    caminho = Path(__file__).resolve().parents[2] / "data" / "talhoes.csv"
    with open(caminho,"w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Talhao","Cultura","Area"])
        for talhao in talhoes:
            writer.writerow([talhao.nome,talhao.cultura,talhao.area])


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


def atualizar_talhao(indice:int, novo_nome=None, nova_cultura=None, nova_area=None):

    if not 0 <= indice < len(talhoes):
        return False

    talhao = talhoes[indice]

    if novo_nome is not None:
        if not novo_nome:
            return False
        talhao.nome = novo_nome
        return True

    if nova_cultura is not None:

        if nova_cultura == "1":
            talhao.cultura = "Cana-de-açúcar"
            insumo_cultura = insumos[1]

        elif nova_cultura == "2":
            talhao.cultura = "Café Arabica"
            insumo_cultura = insumos[0]

        else:
            return False

        talhao.area = nova_area
        talhao.insumos = calculo_insumos(nova_area, insumo_cultura)

        return True

    if nova_area is not None:

        talhao.area = nova_area

        if talhao.cultura == "Cana-de-açúcar":
            talhao.insumos = calculo_insumos(nova_area, insumos[1])
        else:
            talhao.insumos = calculo_insumos(nova_area, insumos[0])

        return True

    return False