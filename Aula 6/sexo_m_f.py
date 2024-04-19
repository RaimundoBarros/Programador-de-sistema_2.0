sexo = input('Digite seu sexo (M => Masculino, F => Feminino): ')

if sexo() == 'm':
    print('Seu sexo é MASCULINO')
elif sexo() == 'f':
    print('Seu sexo é FEMININO')
else:
    print(sexo, 'não corresponde a um comando válido (M ou F)')
