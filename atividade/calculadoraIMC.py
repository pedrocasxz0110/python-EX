def calcular_imc_interpretar_e_sugerir():
    peso = float(input("Digite o seu peso (em kg): "))
    altura = float(input("Digite a sua altura (em metros): "))

    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser números válidos e positivos.")
        return

    imc = peso / (altura * altura)

    if imc < 18.5:
        classificacao = "Abaixo do Peso"
        peso_ideal = 18.5 * (altura * altura)
        diferenca_peso = peso_ideal - peso
        sugestao = f"Para alcançar um peso saudável, você precisa ganhar aproximadamente {diferenca_peso:.2f} kg."
    elif imc < 25:
        classificacao = "Peso Normal"
        sugestao = "Seu peso está dentro da faixa saudável."
    elif imc < 30:
        classificacao = "Acima do Peso"
        peso_ideal = 24.9 * (altura * altura)
        diferenca_peso = peso - peso_ideal
        sugestao = f"Para alcançar um peso saudável, você precisa perder aproximadamente {diferenca_peso:.2f} kg."
    else:
        classificacao = "Obeso"
        peso_ideal = 24.9 * (altura * altura)
        diferenca_peso = peso - peso_ideal
        sugestao = f"Para alcançar um peso saudável, você precisa perder aproximadamente {diferenca_peso:.2f} kg."

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Você é classificado como: {classificacao}")
    print(sugestao)

calcular_imc_interpretar_e_sugerir()
