import math

def velocidade_media(distancia: float, tempo: float) -> float:
    """
    Calcula a velocidade média de um objeto em movimento.
    Args:
        distancia (float): Distância percorrida pelo objeto.
        tempo (float): Tempo gasto pelo objeto para percorrer a distância.
    Returns:
        float: A velocidade média do objeto.
    """
    return distancia / tempo

def aceleracao_media(variacao_velocidade: float, tempo: float) -> float:
    """
    Calcula a aceleração média de um objeto em movimento.
    Args:
        variacao_velocidade (float): Variação da velocidade do objeto.
        tempo (float): Tempo gasto pelo objeto para mudar de velocidade.
    """
    return variacao_velocidade / tempo

def calcular_forca(massa: float, aceleracao: float) -> float:
    """
    Calcula a força resultante aplicada a um objeto.
    Args:
        massa (float): Massa do objeto.
        aceleracao (float): Aceleração do objeto.
    """
    return massa * aceleracao

def calcular_trabalho(forca: float, distancia: float, angulo: float) -> float:
    """
    Calcula o trabalho realizado por uma força que atua sobre um objeto.
    Args:
        forca (float): Força aplicada ao objeto.
        distancia (float): Distância percorrida pelo objeto.
        angulo (float): Ângulo entre a força e a direção do movimento.
    """
    return forca * distancia * math.cos(math.radians(angulo))

def calcular_energia_potencial_gravitacional(massa: float, altura: float) -> float:
    """
    Calcula a energia potencial gravitacional de um objeto em relação a um ponto de referência.
    Args:
        massa (float): Massa do objeto.
        altura (float): Altura do objeto em relação ao ponto de referência.
    """
    return massa * 9.8 * altura

def calcular_energia_cinetica(massa: float, velocidade: float) -> float:
    """
    Calcula a energia cinética de um objeto em movimento.
    Args:
        massa (float): Massa do objeto.
        velocidade (float): Velocidade do objeto.
    """
    return 0.5 * massa * velocidade ** 2

def calcular_potencia(trabalho: float, tempo: float) -> float:
    """
    Calcula a potência de um objeto que realiza um trabalho em um determinado intervalo de tempo.
    Args:
        trabalho (float): Trabalho realizado pelo objeto.
        tempo (float): Tempo gasto pelo objeto para realizar o trabalho.
    """
    return trabalho / tempo

def calcular_pressao(forca: float, area: float) -> float:
    """
    Calcula a pressão exercida por uma força sobre uma determinada área.
    Args:
        forca (float): Força aplicada sobre a área.
        area (float): Área sobre a qual a força é aplicada.
    """
    return forca / area

def calcular_lei_de_ohm(tensao: float, resistencia: float) -> float:
    """
    Calcula a corrente elétrica em um circuito de acordo com a Lei de Ohm.
    Args:
        tensao (float): Tensão elétrica aplicada ao circuito.
        resistencia (float): Resistência do circuito à passagem de corrente elétrica.
    """
    return tensao / resistencia

def calcular_potencia_eletrica(tensao: float, corrente: float) -> float:
    """
    Calcula a potência elétrica dissipada em um circuito elétrico.
    Args:
        tensao (float): Tensão elétrica aplicada ao circuito.
        corrente (float): Corrente elétrica que circula pelo circuito.
    """
    return tensao * corrente

def calcular_carga_eletrica(corrente: float, tempo: float) -> float:
    """
    Calcula a carga elétrica que passa por um ponto em um determinado intervalo de tempo.
    Args:
        corrente (float): Corrente elétrica que passa pelo ponto.
        tempo (float): Intervalo de tempo no qual a corrente circula.
    """
    return corrente * tempo

def calcular_energia_eletrica(potencia: float, tempo: float) -> float:
    """
    Calcula a energia elétrica consumida em um determinado intervalo de tempo.
    Args:
        potencia (float): Potência elétrica dissipada no circuito.
        tempo (float): Intervalo de tempo no qual a energia é consumida.
    """
    return potencia * tempo

def calcular_energia_elastica(constante_elastica: float, deformacao: float) -> float:
    """
    Calcula a energia potencial elástica armazenada em uma mola.
    Args:
        constante_elastica (float): Constante elástica da mola.
        deformacao (float): Deformação da mola em relação à sua posição de equilíbrio.
    """
    return 0.5 * constante_elastica * deformacao ** 2

def calcular_frequencia(periodo: float) -> float:
    """
    Calcula a frequência de um movimento oscilatório a partir do período.
    Args:
        periodo (float): Período do movimento oscilatório.
    """
    return 1 / periodo

def calcular_energia_mecanica(energia_cinetica: float, energia_potencial: float) -> float:
    """
    Calcula a energia mecânica total de um sistema em movimento.
    Args:
        energia_cinetica (float): Energia cinética do sistema.
        energia_potencial (float): Energia potencial do sistema.
    """
    return energia_cinetica + energia_potencial

def menu():
  """
  Exibe um menu de opções para o usuário e permite escolher entre as funções disponíveis.
  """
  while True:
      print("\nEscolha uma opção:")
      print("1- Calcular velocidade média")
      print("2- Calcular aceleração média")
      print("3- Calcular força")
      print("4- Calcular trabalho")
      print("5- Calcular energia potencial gravitacional")
      print("6- Calcular energia cinética")
      print("7- Calcular potência")
      print("8- Calcular pressão")
      print("9- Calcular Lei de Ohm")
      print("10- Calcular potência elétrica")
      print("11- Calcular carga elétrica")
      print("12- Calcular energia elétrica")
      print("13- Calcular energia elástica")
      print("14- Calcular frequência")
      print("15- Calcular energia mecânica")
      print("0- Sair")
      opcao = input("Opção: ")
      if opcao == "0":
        break

if __name__ == "__main__":
    menu()
