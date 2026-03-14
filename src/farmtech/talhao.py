"""
    modelo de dados
"""
class Talhao:

    def __init__(self, nome: str, cultura: str, area: float, insumos: list):
        self.nome = nome
        self.cultura = cultura
        self.area = area
        self.insumos = insumos

    def imprimir_insumo(self) -> str:

        if not self.insumos:
            return "Nenhum insumo cadastrado."

        texto = ""

        for i, insumo in enumerate(self.insumos, start=1):

            texto_insumo = f"""
  ── Insumo {i} ──
  Nome: {insumo['nome']}
  Dose mínima: {insumo['dose_min']} {insumo['unidade_dose']}
  Dose máxima: {insumo['dose_max']} {insumo['unidade_dose']}
  Dose média/ha: {insumo['dose_media_ha']}
  Quantidade total: {insumo['quantidade_total']} {insumo['unidade']}
  Custo estimado: R$ {insumo['custo_estimado']}
"""

            texto += texto_insumo

        texto += f"\n  Custo total estimado: R$ {round(self.insumos[0]['custo_total'],2)}"

        return texto
    def __str__(self):
        return f"""
══════════════════════════════════
🌱 TALHÃO

Nome: {self.nome}
Cultura: {self.cultura}
Área plantada: {self.area} ha

📦 INSUMOS
{self.imprimir_insumo()}
══════════════════════════════════
"""