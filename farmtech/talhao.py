"""
    modelo de dados
"""

from farmtech.storage import talhoes

class Talhao:

    def __init__(self, nome, cultura, area=0, insumos=0):
        self.nome = nome
        self.cultura = cultura
        self.area = area
        self.insumos = insumos

    def exibir(self):
        print(f"Talhão: {self.nome}")
        print(f"Cultura: {self.cultura}")
        print(f"Área: {self.area}")
        print(f"Insumos: {self.insumos}")
