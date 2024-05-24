import math


def calcular_raizes(a: float, b: float, c: float) -> str:
    """
    Calcula as raízes de uma equação quadrática do tipo ax^2 + bx + c = 0.

    Args:
        a (float): Coeficiente do termo quadrático.
        b (float): Coeficiente do termo linear.
        c (float): Termo constante.

    Returns:
        str: Uma mensagem indicando o tipo e o número de raízes da equação.

    Raises:
        ValueError: Se os coeficientes a, b e c não forem números reais.
    """
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "A equação não possui raízes reais"
    
    elif delta == 0:
        raiz = -b / (2*a)
        return f"A equação possui uma raiz real: {raiz}"
    
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return f"A equação possui duas raízes reais: {raiz1} e {raiz2}"


def calcular_raiz_linear(a: float, b: float) -> str:
    """
    Calcula a raiz de uma equação linear do tipo ax + b = 0.

    Args:
        a (float): Coeficiente do termo linear.
        b (float): Termo constante.

    Returns:
        str: Uma mensagem indicando o valor da raiz da equação.

    Raises:
        ValueError: Se os coeficientes a e b não forem números reais.
    """
    if a == 0:
        if b == 0:
            return "A equação é uma identidade (0 = 0) e tem infinitas soluções."
        else:
            return "A equação é impossível (0 ≠ 0) e não tem solução."
    else:
        raiz = -b / a
        return f"A raiz da equação é: {raiz}"


def calcular_raizes_quadraticas():
    """
    Interface de linha de comando para calcular as raízes de uma equação quadrática.

    Solicita ao usuário os coeficientes da equação quadrática e exibe o resultado.
    """
    print("\n--- CALCULAR RAÍZES DE UMA EQUAÇÃO QUADRÁTICA ---\n")
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    
    print(calcular_raizes(a, b, c))


def calcular_raiz_linear(a: float, b: float) -> str:
    """
    Calcula a raiz de uma equação linear do tipo ax + b = 0.

    Args:
        a (float): Coeficiente do termo linear.
        b (float): Termo constante.

    Returns:
        str: Uma mensagem indicando o valor da raiz da equação.

    Raises:
        ValueError: Se os coeficientes a e b não forem números reais.
    """
    if a == 0:
        if b == 0:
            return "A equação é uma identidade (0 = 0) e tem infinitas soluções."
        else:
            return "A equação é impossível (0 ≠ 0) e não tem solução."
    else:
        raiz = -b / a
        return f"A raiz da equação é: {raiz}"


def menu():
    """
    Exibe um menu de opções para o usuário e permite escolher entre as funções disponíveis.
    """
    while True:
        print("\nEscolha uma opção:")
        print("1- Calcular raízes de uma equação quadrática")
        print("2- Calcular raiz de uma equação linear")
        print("0- Sair")

        opcao = input("Opção: ")
        
        if opcao == "1":
            calcular_raizes_quadraticas()
        elif opcao == "2":
            calcular_raiz_linear()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
