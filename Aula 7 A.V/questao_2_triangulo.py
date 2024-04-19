lado_1 = float(input('Digite o primeiro lado do triângulo: '))
lado_2 = float(input('Digite o segundo lado do triângulo: '))
lado_3 = float(input('Digite o terceiro lado do triângulo: '))

if lado_1 == lado_2 and lado_1 == lado_3:
    print('Este triângulo é EQUILÁTERO (todos os lados são iguais).')
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print('Este triângulo é ISÓSCELES (dois lados são iguais).')
else:
    print('Este triângulo é ESCALENO (todos os lados são diferentes).')
