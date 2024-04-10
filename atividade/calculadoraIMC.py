
x = float(input("Digite um peso: "))
y = float(input("Digite uma altura: "))

calculadora_de_imc = x / (y * y)
print("O IMC é:", calculadora_de_imc)

if calculadora_de_imc < 18.5:
    print("Abaixo do peso")
    peso_saudavel = 18.5 * (y * y)
    peso_a_perder = x - peso_saudavel
    print("Para estar saudável, você precisa perder aproximadamente:", peso_a_perder, "kg")
elif 18.5 <= calculadora_de_imc < 24.9:
    print("Peso normal")
elif 25.0 <= calculadora_de_imc < 29.9:
    print("Sobrepeso")
    peso_saudavel = 24.9 * (y * y)
    peso_a_perder = x - peso_saudavel
    print("Para estar saudável, você precisa perder aproximadamente:", peso_a_perder, "kg")
elif 30.0 <= calculadora_de_imc < 34.9:
    print("Obesidade grau 1")
    peso_saudavel = 24.9 * (y * y)
    peso_a_perder = x - peso_saudavel
    print("Para estar no peso normal, você precisa perder aproximadamente:", peso_a_perder, "kg")
elif 35.0 <= calculadora_de_imc < 39.9:
    print("Obesidade grau 2 (severa)")
    peso_saudavel = 24.9 * (y * y)
    peso_a_perder = x - peso_saudavel
    print("Para estar no peso normal, você precisa perder aproximadamente:", peso_a_perder, "kg")
else:
    print("Obesidade grau 3 (mórbida)")
    peso_saudavel = 24.9 * (y * y)
    peso_a_perder = x - peso_saudavel
    print("Para estar no peso normal, você precisa perder aproximadamente:", peso_a_perder, "kg")
