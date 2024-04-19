nota_1= float(input('Digite a primeira nota: '))
nota_2= float(input('Digite a segunda nota: '))
nota_3= float(input('Digite a terceira nota: '))
nota_4= float(input('Digite a quarta nota: '))

media= (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7:
    print('Parabéns sua média é ',media,' você esta aprovado')
else :
    print('Parabéns sua média é ',media,' Infelisme você não esta aprovado')