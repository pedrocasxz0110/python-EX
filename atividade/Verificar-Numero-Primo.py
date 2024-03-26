num = int(input("Digite um número inteiro: "))


primo = True
if num <= 1:
    primo = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break

if primo:
    print(num, "é um número primo.")
else:
    print(num, "não é um número primo.")
