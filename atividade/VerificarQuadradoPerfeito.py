def quadrado_perfeito(num):
    raiz_quadrada = math.isqrt(num)
    return raiz_quadrada ** 2 == num
import math

def quadrado_perfeito(num):
    raiz_quadrada = math.isqrt(num)
    return raiz_quadrada ** 2 == num


numero = int(input("Digite um número: "))


if quadrado_perfeito(numero):
    print(f"{numero} é um quadrado perfeito.")
else:
    print(f"{numero} não é um quadrado perfeito.")


print(quadrado_perfeito(25))  
