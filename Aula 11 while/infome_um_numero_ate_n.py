acumulador = 0
numero = int(input("Digite um numero: "))
n = 10
while acumulador < n:
    acumulador += numero
    numero = int(input("Digite um numero: "))
print(acumulador)