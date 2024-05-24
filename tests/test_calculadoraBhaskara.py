import pytest
from Calculadora_Bhaskara import calcular_raizes, calcular_raiz_linear

def test_calcular_raizes_imaginarias():
    assert calcular_raizes(1, 1, 1) == "A equação não possui raízes reais"

def test_calcular_raiz_unica():
    assert calcular_raizes(1, -2, 1) == "A equação possui uma raiz real: 1.0"
    
def test_calcula_duas_raizes():
    assert calcular_raizes(1, -3, 2) == "A equação possui duas raízes reais: 2.0 e 1.0"

def test_calcular_raiz_linear():
    assert calcular_raiz_linear(2, -4) == "A raiz da equação é: 2.0"

def test_equacao_impossivel():
    assert calcular_raiz_linear(0, 4) == "A equação é impossível (0 ≠ 0) e não tem solução."

def test_identidade():
    assert calcular_raiz_linear(0, 0) == "A equação é uma identidade (0 = 0) e tem infinitas soluções."

