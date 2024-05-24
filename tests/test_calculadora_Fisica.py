import pytest
from Calculadora_fisica import velocidade_media, aceleracao_media, calcular_forca, calcular_trabalho, calcular_energia_potencial_gravitacional, calcular_energia_cinetica, calcular_potencia, calcular_pressao, calcular_lei_de_ohm, calcular_potencia_eletrica, calcular_carga_eletrica, calcular_energia_eletrica, calcular_energia_elastica, calcular_frequencia, calcular_energia_mecanica

def test_velocidade_media():
    assert velocidade_media(10, 2) == 5.0

def test_aceleracao_media():
    assert aceleracao_media(10, 2) == 5.0

def test_calcular_forca():
    assert calcular_forca(10, 2) == 20.0

def test_calcular_trabalho():
    assert calcular_trabalho(50, 10, 60) == 250.00000000000006

def test_calcular_energia_potencial_gravitacional():
    assert calcular_energia_potencial_gravitacional(10, 2) == 196.0

def test_calcular_energia_cinetica():
    assert calcular_energia_cinetica(10, 2) == 20.0

def test_calcular_potencia():
    assert calcular_potencia(10, 2) == 5.0

def test_calcular_pressao():
    assert calcular_pressao(10, 2) == 5.0

def test_calcular_lei_de_ohm():
    assert calcular_lei_de_ohm(10, 2) == 5.0

def test_calcular_potencia_eletrica():
    assert calcular_potencia_eletrica(10, 2) == 20.0

def test_calcular_carga_eletrica():
    assert calcular_carga_eletrica(10, 2) == 20.0

def test_calcular_energia_eletrica():
    assert calcular_energia_eletrica(10, 2) == 20.0

def test_calcular_energia_elastica():
    assert calcular_energia_elastica(10, 2) == 20.0

def test_calcular_frequencia():
    assert calcular_frequencia(10) == 0.1

def test_calcular_energia_mecanica():
    assert calcular_energia_mecanica(10, 2) == 12.0