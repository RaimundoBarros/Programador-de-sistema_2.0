
soma = 0
contador = 0
gibi=0

numero = float(input("Digite a quantidade de gib : "))
while contador < numero:
    gibi = float(input("O valor do gib: "))
    soma += gibi
    contador += 1
media = soma / numero

print(f"A média de valor pago por gib é: {media} e o valor total gasto é R$:{soma}")