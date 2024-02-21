limite_superior = int(input("Digite o Numero : "))

numeros_perfeitos = []

for numero in range(1, limite_superior + 1):
    soma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma_divisores += divisor
    if soma_divisores == numero:
        numeros_perfeitos.append(numero)

if len(numeros_perfeitos) == 0:
    print("Não foram encontrados números perfeitos .")
else:
    print("Números perfeitos encontrados:", numeros_perfeitos)
