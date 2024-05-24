import math

def velocidade_media(distancia: float, tempo: float) -> float:
    return distancia / tempo

def aceleracao_media(variacao_velocidade: float, tempo: float) -> float:
    return variacao_velocidade / tempo

def calcular_forca(massa: float, aceleracao: float) -> float:
    return massa * aceleracao

def calcular_trabalho(forca: float, distancia: float, angulo: float) -> float:
    return forca * distancia * math.cos(math.radians(angulo))

def calcular_energia_potencial_gravitacional(massa: float, altura: float) -> float:
    return massa * 9.8 * altura

def calcular_energia_cinetica(massa: float, velocidade: float) -> float:
    return 0.5 * massa * velocidade ** 2

def calcular_potencia(trabalho: float, tempo: float) -> float:
    return trabalho / tempo

def calcular_pressao(forca: float, area: float) -> float:
    return forca / area

def calcular_lei_de_ohm(tensao: float, resistencia: float) -> float:
    return tensao / resistencia

def calcular_potencia_eletrica(tensao: float, corrente: float) -> float:
    return tensao * corrente

def calcular_carga_eletrica(corrente: float, tempo: float) -> float:
    return corrente * tempo

def calcular_energia_eletrica(potencia: float, tempo: float) -> float:
    return potencia * tempo

def calcular_energia_elastica(constante_elastica: float, deformacao: float) -> float:
    return 0.5 * constante_elastica * deformacao ** 2

def calcular_frequencia(periodo: float) -> float:
    return 1 / periodo

def calcular_energia_mecanica(energia_cinetica: float, energia_potencial: float) -> float:
    return energia_cinetica + energia_potencial

def menu():
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
        elif opcao == "1":
            distancia = float(input("Digite a distância (m): "))
            tempo = float(input("Digite o tempo (s): "))
            print("Velocidade média:", velocidade_media(distancia, tempo))
        elif opcao == "2":
            variacao_velocidade = float(input("Digite a variação da velocidade (m/s): "))
            tempo = float(input("Digite o tempo (s): "))
            print("Aceleração média:", aceleracao_media(variacao_velocidade, tempo))
        elif opcao == "3":
            massa = float(input("Digite a massa (kg): "))
            aceleracao = float(input("Digite a aceleração (m/s²): "))
            print("Força:", calcular_forca(massa, aceleracao))
        elif opcao == "4":
            forca = float(input("Digite a força (N): "))
            distancia = float(input("Digite a distância (m): "))
            angulo = float(input("Digite o ângulo (graus): "))
            print("Trabalho:", calcular_trabalho(forca, distancia, angulo))
        elif opcao == "5":
            massa = float(input("Digite a massa (kg): "))
            altura = float(input("Digite a altura (m): "))
            print("Energia potencial gravitacional:", calcular_energia_potencial_gravitacional(massa, altura))
        elif opcao == "6":
            massa = float(input("Digite a massa (kg): "))
            velocidade = float(input("Digite a velocidade (m/s): "))
            print("Energia cinética:", calcular_energia_cinetica(massa, velocidade))
        elif opcao == "7":
            trabalho = float(input("Digite o trabalho (J): "))
            tempo = float(input("Digite o tempo (s): "))
            print("Potência:", calcular_potencia(trabalho, tempo))
        elif opcao == "8":
            forca = float(input("Digite a força (N): "))
            area = float(input("Digite a área (m²): "))
            print("Pressão:", calcular_pressao(forca, area))
        elif opcao == "9":
            tensao = float(input("Digite a tensão (V): "))
            resistencia = float(input("Digite a resistência (Ω): "))
            print("Corrente elétrica:", calcular_lei_de_ohm(tensao, resistencia))
        elif opcao == "10":
            tensao = float(input("Digite a tensão (V): "))
            corrente = float(input("Digite a corrente (A): "))
            print("Potência elétrica:", calcular_potencia_eletrica(tensao, corrente))
        elif opcao == "11":
            corrente = float(input("Digite a corrente (A): "))
            tempo = float(input("Digite o tempo (s): "))
            print("Carga elétrica:", calcular_carga_eletrica(corrente, tempo))
        elif opcao == "12":
            potencia = float(input("Digite a potência (W): "))
            tempo = float(input("Digite o tempo (s): "))
            print("Energia elétrica:", calcular_energia_eletrica(potencia, tempo))
        elif opcao == "13":
            constante_elastica = float(input("Digite a constante elástica (N/m): "))
            deformacao = float(input("Digite a deformação (m): "))
            print("Energia elástica:", calcular_energia_elastica(constante_elastica, deformacao))
        elif opcao == "14":
            periodo = float(input("Digite o período (s): "))
            print("Frequência:", calcular_frequencia(periodo))
        elif opcao == "15":
            energia_cinetica = float(input("Digite a energia cinética (J): "))
            energia_potencial = float(input("Digite a energia potencial (J): "))
            print("Energia mecânica:", calcular_energia_mecanica(energia_cinetica, energia_potencial))
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
