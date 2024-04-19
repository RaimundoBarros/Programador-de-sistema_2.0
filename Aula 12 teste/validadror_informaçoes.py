nome = input("Digite seu nome: ")
while len(nome) < 3:
    nome = input("Seu nome deve ter mais de 3 caracteres. Digite novamente: ")

idade = int(input("Digite sua idade: "))
while idade < 1 or idade > 150:
    idade = int(input("Sua idade deve estar entre 18 e 150 anos. Digite novamente: "))

salario = float(input("Digite o valor do seu salário: "))
while salario < 1:
    salario = float(input("Digite um salário válido (maior que 1420): "))

sexo = input("Digite seu sexo (M ou F): ")
while sexo != "m" and sexo != "f":
    sexo = input("Digite um sexo válido (M ou F): ")

estado = input("Estado Civil (S - C - V - D): ")
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
    estado = input("Digite um estado civil válido (S - C - V - D): ")

print(f"Olá {nome}, seus dados foram cadastrados com sucesso! \n Idade: {idade} \n Salario: {salario} \n Sexo: {sexo} \n Estado: {estado}")
