def encontrar_numeros_perfeitos(limite):
    numeros_perfeitos = []
    for numero in range(1, limite + 1):
        soma_divisores = sum([divisor for divisor in range(1, numero) if numero % divisor == 0])
        if soma_divisores == numero:
            numeros_perfeitos.append(numero)
    return numeros_perfeitos

limite_superior = int(input("digite um numero : "))

numeros_perfeitos_encontrados = encontrar_numeros_perfeitos(limite_superior)

if len(numeros_perfeitos_encontrados) == 0:
    print("Não foram encontrados números perfeitos. ")
else:
    print("Números perfeitos encontrados:", numeros_perfeitos_encontrados)
