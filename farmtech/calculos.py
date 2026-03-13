"""
    cálculos agrícolas 
"""

def calculo_area(cultura:str) -> float:
    match cultura:
        case "Café Arabica":
            print("Área do Terreno(Trapézio")
            base_maior = float(input("Digite a base maior: "))
            base_menor = float(input("Digite a base menor: "))
            altura = float(input("Digite a altura: "))
            area = (base_maior + base_menor) * altura / 2
            return area
        case "Cana-de-açúcar":
            print("Area do terreno(Retângulo")
            base = float(input("Digite a base: "))
            altura = float(input("Digite a altura: "))
            area = base * altura
            return area
