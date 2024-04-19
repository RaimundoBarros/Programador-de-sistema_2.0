
nota = int(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print(" A nota não esta entre 0 e 10", nota )
    
    nota = float(input("Digite um numero: "))
print("A nota incerida foi : ", nota)