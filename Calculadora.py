def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Erro: Divisão por zero!")
    return num1 / num2

def calculadora():
    print("\n--- CALCULADORA ---\n")
    print("Escolha a operação:")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("0- Sair")

    operacao = input("Escolha uma operação: ")
    
    if operacao == "0":
        return
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "1":
        soma(num1, num2)
    elif operacao == "2":
        subtracao(num1, num2)
    elif operacao == "3":
        multiplicacao(num1, num2)
    elif operacao == "4":
        divisao(num1, num2)
    else:
        print("Operação inválida. Tente novamente.")
