metro_quadrado_em_hec = lambda x:x/10000

def calculo_trapezio(base_maior:float,base_menor:float,altura:float) -> float:
    area = (base_maior+base_menor) * altura / 2
    return metro_quadrado_em_hec(area)


def calculo_retangulo(base:float,altura:float) -> float:
    area = base * altura
    return metro_quadrado_em_hec(area)

def calculo_insumos(area_ha:float,insumos:list) -> list:
    custo_total = 0.0
    lista_de_insumos = []
    for insumo in insumos:
        dose_media = (insumo["dose_min"] + insumo["dose_max"])/2
        quantidade = dose_media * area_ha
        custo = quantidade * insumo["custo_por_unidade"]
        custo_total+= custo
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
            "custo_total" : custo_total
        })
    return lista_de_insumos