numeros = []
for i in range(5):
    entrada = float(input("Digite um número: "))
    numeros.append(entrada)

maior_numero = numeros  
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print("O maior número digitado é:", maior_numero)

