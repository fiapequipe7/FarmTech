"""
    modelo de dados
"""
class Talhao:
    def __init__(self, nome:str, cultura:str, area:float, insumos:list):
        self.nome = nome
        self.cultura = cultura
        self.area = area
        self.insumos = insumos

    def imprimir_insumo(self) -> str:
        texto = ""
        for insumo in self.insumos:
            texto_insumo = f"""nome: {insumo['nome']}\n
                dose_min: {insumo['dose_min']}\n"
                dose_max: {insumo["dose_max"]}\n"
                unidade_dose: {insumo['unidade_dose']}\n"
                dose_media_ha: {insumo['dose_media_ha']}\n"
                quantidade_total: {insumo['quantidade_total']}\n"
                unidade: {insumo['unidade']}\n"
                custo_estimado {insumo['custo_estimado'] } R$\n"""
            texto = texto+texto_insumo
        texto = texto + f"\nCusto_total = {self.insumos[0]["custo_total"]}"
        return texto

    def __str__(self):
        return f"""
    Nome: {self.nome}
    Cultura: {self.cultura}
    Área: {self.area} ha
    Insumos: {self.imprimir_insumo()}
    """