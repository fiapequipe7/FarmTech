# Função lambda para conversão de metros quadrados para hectares
metro_quadrado_em_hec = lambda x: x / 10000


def calculo_trapezio(base_maior: float, base_menor: float, altura: float) -> float:
    """
    Calcula a área de um terreno em formato de trapézio e converte para hectares.

    Fórmula:
        Área = ((base_maior + base_menor) * altura) / 2

    Args:
        base_maior (float): Comprimento da base maior em metros.
        base_menor (float): Comprimento da base menor em metros.
        altura (float): Altura do trapézio em metros.

    Returns:
        float: Área do terreno em hectares.
    """
    area = (base_maior + base_menor) * altura / 2
    return metro_quadrado_em_hec(area)


def calculo_retangulo(base: float, altura: float) -> float:
    """
    Calcula a área de um terreno retangular e converte para hectares.

    Fórmula:
        Área = base * altura

    Args:
        base (float): Base do terreno em metros.
        altura (float): Altura do terreno em metros.

    Returns:
        float: Área do terreno em hectares.
    """
    area = base * altura
    return metro_quadrado_em_hec(area)


def calculo_insumos(area_ha: float, insumos: list) -> list:
    """
    Calcula a quantidade total de insumos necessários e o custo estimado com base na área.

    Para cada insumo:
    - Calcula a dose média entre dose_min e dose_max
    - Calcula a quantidade total necessária (dose média * área)
    - Calcula o custo estimado (quantidade * custo por unidade)
    - Acumula o custo total

    Estrutura esperada de cada insumo na lista:
        {
            "nome": str,
            "dose_min": float,
            "dose_max": float,
            "unidade_dose": str (ex: "L/ha", "kg/ha"),
            "custo_por_unidade": float
        }

    Args:
        area_ha (float): Área da plantação em hectares.
        insumos (list): Lista de dicionários contendo os dados dos insumos.

    Returns:
        list: Lista de dicionários com os cálculos detalhados de cada insumo, incluindo:
            - nome
            - dose mínima e máxima
            - dose média por hectare
            - quantidade total necessária
            - unidade
            - custo estimado individual
            - custo total acumulado
    """
    custo_total = 0.0
    lista_de_insumos = []

    for insumo in insumos:
        # Cálculo da dose média entre os valores mínimo e máximo
        dose_media = (insumo["dose_min"] + insumo["dose_max"]) / 2

        # Quantidade total baseada na área
        quantidade = dose_media * area_ha

        # Cálculo do custo para o insumo atual
        custo = quantidade * insumo["custo_por_unidade"]
        custo_total += custo

        # Extração da unidade (ex: "L" de "L/ha")
        unidade = insumo["unidade_dose"].split("/")[0]

        lista_de_insumos.append({
            "nome": insumo["nome"],
            "dose_min": insumo["dose_min"],
            "dose_max": insumo["dose_max"],
            "unidade_dose": insumo["unidade_dose"],
            "dose_media_ha": round(dose_media, 2),
            "quantidade_total": round(quantidade, 2),
            "unidade": unidade,
            "custo_estimado": round(custo, 2),
            "custo_total": custo_total
        })

    return lista_de_insumos