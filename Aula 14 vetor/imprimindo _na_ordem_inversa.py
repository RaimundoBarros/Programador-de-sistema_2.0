#a = []
#for _ in range(6):
    #numero = float(input("Digite um número: "))
    #a.append(numero)


#for i in reversed(a):
    #print(i)

a = []
for i in range(6):
    numero = float(input("Digite um número: "))
    a.append(numero)

for i in a:
    print(i)

for i in range(len(a) - 1, -1, -1):
    print(a[i])

