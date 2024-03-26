string = input("Digite uma palavra para verificar: ")


vogais = 'aeiouAEIOU'
contagem = 0
for char in string:
    if char in vogais:
        contagem += 1

print("Número de vogais na palavra:", contagem)
