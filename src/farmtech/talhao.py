"""
Módulo de modelo de dados.

Define a estrutura da entidade Talhão, que representa uma área de plantio
com sua respectiva cultura, área e insumos associados.
"""


class Talhao:
    """
    Classe que representa um talhão agrícola.

    Um talhão contém:
    - Nome identificador
    - Tipo de cultura plantada
    - Área em hectares
    - Lista de insumos calculados para a plantação
    """

    def __init__(self, nome: str, cultura: str, area: float, insumos: list):
        """
        Inicializa um novo objeto Talhao.

        Args:
            nome (str): Nome do talhão.
            cultura (str): Tipo de cultura (ex: "Café Arabica").
            area (float): Área do talhão em hectares.
            insumos (list): Lista de insumos calculados para o talhão.
        """
        self.nome = nome
        self.cultura = cultura
        self.area = area
        self.insumos = insumos

    def imprimir_insumo(self) -> str:
        """
        Gera uma representação textual formatada dos insumos do talhão.

        Para cada insumo, exibe:
        - Nome
        - Dose mínima e máxima
        - Dose média por hectare
        - Quantidade total necessária
        - Custo estimado

        Returns:
            str: Texto formatado contendo as informações dos insumos.
        """

        if not self.insumos:
            return "Nenhum insumo cadastrado."

        texto = ""

        for i, insumo in enumerate(self.insumos, start=1):

            # Montagem do texto individual de cada insumo
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

        # Custo total acumulado (armazenado no primeiro insumo)
        texto += f"\n  Custo total estimado: R$ {round(self.insumos[0]['custo_total'], 2)}"

        return texto

    def __str__(self) -> str:
        """
        Retorna a representação textual completa do talhão.

        Inclui:
        - Nome
        - Cultura
        - Área
        - Lista detalhada de insumos

        Returns:
            str: Texto formatado para exibição no terminal.
        """
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