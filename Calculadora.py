def soma(num1: float, num2: float) -> float:
    """
    Retorna a soma de dois números.

    Args:
        num1 (float): O primeiro número.
        num2 (float): O segundo número.

    Returns:
        float: A soma de num1 e num2.
    """
    return num1 + num2

def subtracao(num1: float, num2: float) -> float:
    """
    Retorna a subtração de dois números.

    Args:
        num1 (float): O primeiro número.
        num2 (float): O segundo número.

    Returns:
        float: A diferença entre num1 e num2.
    """
    return num1 - num2

def multiplicacao(num1: float, num2: float) -> float:
    """
    Retorna a multiplicação de dois números.

    Args:
        num1 (float): O primeiro número.
        num2 (float): O segundo número.

    Returns:
        float: O produto de num1 e num2.
    """
    return num1 * num2

def divisao(num1: float, num2: float) -> float:
    """
    Retorna a divisão de dois números.

    Args:
        num1 (float): O numerador.
        num2 (float): O denominador.

    Returns:
        float: O quociente de num1 dividido por num2.

    Raises:
        ZeroDivisionError: Se num2 for zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Erro: Divisão por zero!")
    return num1 / num2

def calculadora():
    """
    Interface de linha de comando para uma calculadora simples que realiza
    operações básicas: adição, subtração, multiplicação e divisão.

    Solicita ao usuário que escolha uma operação e insira dois números para
    realizar a operação escolhida. O resultado da operação é exibido no console.

    Operações disponíveis:
        1- Adição
        2- Subtração
        3- Multiplicação
        4- Divisão
        0- Sair
    """
    print("\n--- CALCULADORA ---\n")
    print("Escolha a operação:")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("0- Sair")

    operacao = input("Escolha uma operação: ")
    
    if operacao == "0":
        return ""
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "1":
        print(f"Resultado: {soma(num1, num2)}")
    elif operacao == "2":
        print(f"Resultado: {subtracao(num1, num2)}")
    elif operacao == "3":
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif operacao == "4":
        try:
            print(f"Resultado: {divisao(num1, num2)}")
        except ZeroDivisionError as e:
            print(e)
    else:
        print("Operação inválida. Tente novamente.")
