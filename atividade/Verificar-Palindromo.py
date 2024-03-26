palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
