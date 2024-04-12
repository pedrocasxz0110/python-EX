def contar_maiusculas(texto):
    count = 0
    for char in texto:
        if char.isupper():
            count += 1
    return count

texto = input("Digite uma string: ")


quantidade_maiusculas = contar_maiusculas(texto)

print(f"A string contém {quantidade_maiusculas} letras maiúsculas.")
