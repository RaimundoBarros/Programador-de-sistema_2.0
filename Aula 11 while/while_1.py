acumulador = 0
numero = int(input("Digite um numero: "))

while numero != 0:
    acumulador += numero
    numero = int(input("Digite um numero: "))
print(acumulador)