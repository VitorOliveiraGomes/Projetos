def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a/b
    else:
        return "Erro! Divisão por Zero."

def calculadora():
    print("Selecione a operação")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = (input("Digite sua escolha (1/2/3/4): "))
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    if escolha == '1':
        print(f"{num1} + {num2} = {adicao(num1, num2)}")
    if escolha == '2':
        print(f"{num1} - {num2} = {subtracao(num1 , num2)}")
    if escolha == '3':
        print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
    if escolha == '4':
        print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Opção Invalida!")

calculadora()
          
    