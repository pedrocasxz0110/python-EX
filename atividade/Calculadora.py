
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."


print("Operações disponíveis:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Escolha a operação (1/2/3/4): "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


if opcao == 1:
    print("Resultado da soma:", soma(num1, num2))
elif opcao == 2:
    print("Resultado da subtração:", subtracao(num1, num2))
elif opcao == 3:
    print("Resultado da multiplicação:", multiplicacao(num1, num2))
elif opcao == 4:
    print("Resultado da divisão:", divisao(num1, num2))
else:
    print("Opção inválida.")
