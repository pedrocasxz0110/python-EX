def inverter_string(texto):
    return texto[::-1]
  
entrada = input("Digite uma string: ")
inverso = inverter_string(entrada)

print(f"A string invertida é: {inverso}")
