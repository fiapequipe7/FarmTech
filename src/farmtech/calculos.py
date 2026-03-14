metro_quadrado_em_hec = lambda x:x/10000

def calculo_trapezio(base_maior:float,base_menor:float,altura:float) -> float:
    area = (base_maior+base_menor) * altura / 2
    return metro_quadrado_em_hec(area)


def calculo_retangulo(base:float,altura:float) -> float:
    area = base * altura
    return metro_quadrado_em_hec(area)