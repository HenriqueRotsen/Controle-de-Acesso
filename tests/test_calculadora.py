import pytest
from Calculadora import soma, subtracao, multiplicacao, divisao

@pytest.fixture
def numeros_inteiros():
    return 3, 5, -10, 10, 0, 100, -50

@pytest.fixture
def numeros_ponto_flutuante():
    return 3.5, 2.5, -1.5, 1.5, 0.1, 0.2, 2.333, 3.667

# Testes para a função de soma com números inteiros
def test_soma_inteiros(numeros_inteiros):
    inteiros = numeros_inteiros

    # Casos de teste com números inteiros
    assert soma(inteiros[0], inteiros[1]) == 8
    assert soma(inteiros[2], inteiros[3]) == 0
    assert soma(inteiros[4], inteiros[4]) == 0
    assert soma(inteiros[5], inteiros[6]) == 50

# Testes para a função de soma com números de ponto flutuante
def test_soma_float( numeros_ponto_flutuante):
    flutuantes = numeros_ponto_flutuante
    
    # Casos de teste com números de ponto flutuante
    assert soma(flutuantes[0], flutuantes[1]) == 6
    assert soma(flutuantes[2], flutuantes[3]) == 0
    assert soma(flutuantes[4], flutuantes[5]) == pytest.approx(0.3)
    assert soma(flutuantes[6], flutuantes[7]) == pytest.approx(6.0)


# Testes para a função de subtração com números inteiros
def test_subtracao_inteiros(numeros_inteiros):
    inteiros = numeros_inteiros

    # Casos de teste com números inteiros
    assert subtracao(inteiros[0], inteiros[1]) == -2
    assert subtracao(inteiros[2], inteiros[3]) == -20
    assert subtracao(inteiros[4], inteiros[4]) == 0
    assert subtracao(inteiros[6], inteiros[5]) == -150

def test_subtracao_float(numeros_ponto_flutuante):
    flutuantes = numeros_ponto_flutuante
    
    # Casos de teste com números de ponto flutuante
    assert subtracao(flutuantes[0], flutuantes[1]) == 1.0
    assert subtracao(flutuantes[2], flutuantes[3]) == -3.0
    assert subtracao(flutuantes[4], flutuantes[5]) == pytest.approx(-0.1)
    assert subtracao(flutuantes[6], flutuantes[7]) == pytest.approx(-1.334)

# Testes para a função de multiplicação com números inteiros
def test_multiplicacao_inteiros(numeros_inteiros):
    inteiros = numeros_inteiros

    # Casos de teste com números inteiros
    assert multiplicacao(inteiros[0], inteiros[1]) == 15
    assert multiplicacao(inteiros[2], inteiros[3]) == -100
    assert multiplicacao(inteiros[4], inteiros[4]) == 0
    assert multiplicacao(inteiros[6], inteiros[5]) == -5000

def test_multiplicacao_float(numeros_ponto_flutuante):
    flutuantes = numeros_ponto_flutuante
    
    # Casos de teste com números de ponto flutuante
    assert multiplicacao(flutuantes[0], flutuantes[1]) == 8.75
    assert multiplicacao(flutuantes[2], flutuantes[3]) == -2.25
    assert multiplicacao(flutuantes[4], flutuantes[5]) == pytest.approx(0.02, abs=0.001)
    assert multiplicacao(flutuantes[6], flutuantes[7]) == pytest.approx(8.555, abs=0.001)

# Testes para a função de divisão com números inteiros
def test_divisao_inteiros(numeros_inteiros):
    inteiros = numeros_inteiros

    # Casos de teste com números inteiros
    assert divisao(inteiros[0], inteiros[1]) == 0.6
    assert divisao(inteiros[2], inteiros[3]) == -1.0
    with pytest.raises(ZeroDivisionError):
        divisao(inteiros[4], inteiros[4])

def test_divisao_float(numeros_ponto_flutuante):
    flutuantes = numeros_ponto_flutuante
    
    # Casos de teste com números de ponto flutuante
    assert divisao(flutuantes[0], flutuantes[1]) == 1.4
    assert divisao(flutuantes[2], flutuantes[3]) == -1.0
    assert divisao(flutuantes[4], flutuantes[5]) == pytest.approx(0.5)
    assert divisao(flutuantes[6], flutuantes[7]) == pytest.approx(0.636, abs=0.001)

# Teste para divisão por zero
def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)
