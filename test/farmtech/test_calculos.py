import pytest
from src.farmtech.calculos import calculo_trapezio,calculo_retangulo

def test_calculo_trapezio():
    assert calculo_trapezio(15,10,10) == 125.0

def test_calculo_retangulo():
    assert calculo_retangulo(15,10) == 150.0
def test_calculo_insumo():
    assert()