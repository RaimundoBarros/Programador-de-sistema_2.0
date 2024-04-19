escala = input('Digite C para converter de CELSISUS / FAHRENHEIT:  \n Digite F para converter de FAHRENHEIT / CELSISUS: ')
temperatura = float(input('Digite a temperatura: '))

if escala == 'c':
    print('A temperatatura em CELSISUS É', (temperatura*9/5)+32)
elif escala == "f":
    print('A temperatatura em FAHRENHEIT É', (temperatura - 32)*5/9)
else:
    print(' Não corresponde a um comando valido C - CELSISUS ou F - FAHRENHEIT.')