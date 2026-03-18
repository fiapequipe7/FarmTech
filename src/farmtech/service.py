"""
Módulo responsável pela manipulação de dados dos talhões.

Contém funções para:
- Cadastro
- Listagem
- Atualização
- Remoção
- Exportação para CSV
"""

from pathlib import Path
import csv
from farmtech.storage import *
from farmtech.talhao import *
from farmtech.calculos import *


def export_csv() -> None:
    """
    Exporta os dados dos talhões para um arquivo CSV.

    O arquivo será salvo no diretório:
        data/talhoes.csv

    Estrutura do CSV:
        Talhao, Cultura, Area

    Cada linha representa um talhão cadastrado no sistema.
    """
    caminho = Path(__file__).resolve().parents[2] / "data" / "talhoes.csv"

    with open(caminho, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Cabeçalho do arquivo CSV
        writer.writerow(["Talhao", "Cultura", "Area"])

        # Escrita dos dados dos talhões
        for talhao in talhoes:
            writer.writerow([talhao.nome, talhao.cultura, talhao.area])


def cadastrar_talhao(nome: str, cultura: str, area) -> None:
    """
    Cadastra um novo talhão no sistema.

    Com base na cultura informada, seleciona automaticamente
    o conjunto de insumos correspondente e realiza o cálculo.

    Args:
        nome (str): Nome do talhão.
        cultura (str): Tipo de cultura (ex: "Café Arabica").
        area (float): Área do talhão em hectares.

    Returns:
        None
    """
    lista_insumos = []

    # Seleção de insumos com base na cultura
    if cultura == "Café Arabica":
        lista_insumos = calculo_insumos(area, insumos[0])
    else:
        lista_insumos = calculo_insumos(area, insumos[1])

    # Criação do objeto Talhao
    novo_talhao = Talhao(nome, cultura, area, lista_insumos)

    # Armazenamento na lista global
    talhoes.append(novo_talhao)


def listar_talhoes() -> list:
    """
    Retorna a lista de talhões cadastrados.

    Returns:
        list: Lista de objetos Talhao.
    """
    return talhoes


def deletar_talhao(indice: int) -> bool:
    """
    Remove um talhão da lista com base no índice.

    Args:
        indice (int): Posição do talhão na lista.

    Returns:
        bool:
            True se o talhão foi removido com sucesso.
            False se o índice for inválido.
    """
    if not 0 <= indice < len(talhoes):
        return False

    talhoes.pop(indice)
    return True


def atualizar_talhao(indice: int, novo_nome=None, nova_cultura=None, nova_area=None):
    """
    Atualiza os dados de um talhão existente.

    Permite atualizar:
    - Nome
    - Cultura (com recálculo de insumos)
    - Área (com recálculo de insumos)

    Apenas um tipo de atualização é realizado por chamada.

    Args:
        indice (int): Índice do talhão na lista.
        novo_nome (str, opcional): Novo nome do talhão.
        nova_cultura (str, opcional): Código da nova cultura ("1" ou "2").
        nova_area (float, opcional): Nova área do talhão.

    Returns:
        bool:
            True se a atualização foi realizada com sucesso.
            False se houver erro (índice inválido ou dados incorretos).
    """

    # Validação do índice
    if not 0 <= indice < len(talhoes):
        return False

    talhao = talhoes[indice]

    # Atualização do nome
    if novo_nome is not None:
        if not novo_nome:
            return False

        talhao.nome = novo_nome
        return True

    # Atualização da cultura (com recálculo de insumos)
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

    # Atualização da área (com recálculo de insumos)
    if nova_area is not None:

        talhao.area = nova_area

        if talhao.cultura == "Cana-de-açúcar":
            talhao.insumos = calculo_insumos(nova_area, insumos[1])
        else:
            talhao.insumos = calculo_insumos(nova_area, insumos[0])

        return True

    return False