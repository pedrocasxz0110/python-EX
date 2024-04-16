import math

def calcular_logaritmo(numero, base=None):
    if base is None:
      
        if numero <= 0:
            return "O logaritmo natural de um número negativo ou zero não é definido."
        else:
            return math.log(numero)
    else:
     
        if base <= 0 or base == 1:
            return "A base do logaritmo deve ser um número positivo diferente de 1."
        elif numero <= 0:
            return "O logaritmo de um número negativo ou zero não é definido."
        else:
            return math.log(numero, base)

numero = float(input("Digite o número: "))
base = float(input("Digite a base (ou pressione Enter para logaritmo natural): "))

if base:
    resultado = calcular_logaritmo(numero, base)
    print(f"O logaritmo de {numero} na base {base} é: {resultado}")
else:
    resultado = calcular_logaritmo(numero)
    print(f"O logaritmo natural de {numero} é: {resultado}")
