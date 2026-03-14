"""
    modelo de dados
"""


class Talhao:

    def __init__(self, nome, cultura, area):
        self.nome = nome
        self.cultura = cultura
        self.area = area
        if self.cultura == "Cana-de-açúcar":
            self.insumos =[{
            "nome": "Calcario Dolomitico",
            "funcao": "Corretivo de solo (elevar V% a 60%)",
            "dose_min": 2.0,
            "dose_max": 5.0,
            "unidade_dose": "t/ha",
            "metodo": "A lanco, incorporado pre-plantio",
            "custo_por_unidade": 120.00,    # R$/tonelada (media R$100-140)
            "unidade_custo": "R$/t"
        },
        {
            "nome": "Ureia Agricola",
            "dose_min": 270.0,              # kg ureia/ha (124 kg N / 0.46)
            "dose_max": 317.0,              # kg ureia/ha (146 kg N / 0.46)
            "unidade_dose": "kg/ha",
            "custo_por_unidade": 2.219,     # R$/kg (R$ 2.219,00/tonelada)
            "unidade_custo": "R$/kg"
        },
        {
            "nome": "Dual Gold (S-metolachlor)",
            "dose_min": 2.75,               # L produto/ha (2640g / 960g/L)
            "dose_max": 2.75,
            "unidade_dose": "L/ha",
            "custo_por_unidade": 123.00,    # R$/L (ref: R$ 618/5L)
            "unidade_custo": "R$/L"
        },
        {
            "nome": "Opera (Epoxiconazol + Piraclostrobina)",
            "dose_min": 0.8,
            "dose_max": 1.0,
            "unidade_dose": "L/ha",
            "custo_por_unidade": 102.90,    # R$/L
            "unidade_custo": "R$/L"
        }]
        else:
            self.insumos = [{
            "nome": "NPK 04-14-08",
            "dose_min": 400.0,
            "dose_max": 800.0,
            "unidade_dose": "kg/ha",
            "custo_por_unidade": 2.35,      # R$/kg (R$ 2.350,00/tonelada)
            "unidade_custo": "R$/kg"
        },
        {
            "nome": "Verdadero 600 WG (Tiametoxam + Ciproconazol)",
            "dose_min": 1.0,
            "dose_max": 1.0,
            "unidade_dose": "kg/ha",
            "custo_por_unidade": 250.00,    # R$/kg
            "unidade_custo": "R$/kg"
        },
        {
            "nome": "Opera (Epoxiconazol + Piraclostrobina)",
            "dose_min": 0.8,
            "dose_max": 1.5,
            "unidade_dose": "L/ha",
            "custo_por_unidade": 102.90,    # R$/L
            "unidade_custo": "R$/L"
        },
        {
            "nome": "Calcario Agricola",
            "dose_min": 2.0,
            "dose_max": 4.0,
            "unidade_dose": "t/ha",
            "custo_por_unidade": 110.00,    # R$/t (media R$80-140)
            "unidade_custo": "R$/t"
        }]

    def exibir(self):
        print(f"Talhão: {self.nome}")
        print(f"Cultura: {self.cultura}")
        print(f"Área: {self.area}")
        print(f"Insumos: {self.insumos}")

    def __str__(self):
        return f"""
    Nome: {self.nome}
    Cultura: {self.cultura}
    Área: {self.area} ha
    Insumos: {self.insumos}
    """