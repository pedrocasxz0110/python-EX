def potencia_de_2(num):
    return num & (num - 1) == 0 and num != 0


numero = int(input("Digite um número: "))

if potencia_de_2(numero):
    print(f"{numero} é uma potência de 2.")
else:
    print(f"{numero} não é uma potência de 2.")
