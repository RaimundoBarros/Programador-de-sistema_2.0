sexo = input('Digite seu sexo (M => Masculino, F => Feminino): ')
altura = float(input('Digite sua altura em metros: '))

if sexo == 'm': 
    if altura >= 1.7:
     print('Seu sexo é MASCULINO. Você pode servir ao exército.')
    else:
        print('Seu sexo é Masculino, mas você não pode servir ao exército.')

elif sexo == 'f':
    if altura >= 1.6:
        print('Seu sexo é FEMININO. Você pode servir ao exército.')
    else:
        print('Seu sexo é FEMININO, mas você não pode servir ao exército.')

else:
    print(' Não corresponde a um comando valido M ou F.')