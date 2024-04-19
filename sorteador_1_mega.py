import random

# Gera uma lista com números de 1 a 60
numeros_possiveis = list(range(1, 61))

# Sorteia seis números únicos
numeros_sorteados = random.sample(numeros_possiveis, 6)

# Imprime os números sorteados
print("Números sorteados:")
for numero in numeros_sorteados:
    print(numero)