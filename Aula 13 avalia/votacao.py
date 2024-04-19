total_eleitores = int(input("Digite o número total de eleitores: "))
votos_tiao = 0
votos_shaolin = 0
votos_ze = 0

while total_eleitores > 0:
    print("\nOpções de candidatos:")
    print("2101. Tião")
    print("2403. Shaolin")
    print("1202. Zé")    
    escolha = int(input("Digite o número do candidato escolhido : "))    
    if escolha == 2101:
        votos_tiao += 1
    elif escolha == 2403:
        votos_shaolin += 1
    elif escolha == 1202:
        votos_ze += 1
    else:
        print("Opção inválida. Tente novamente.")

    total_eleitores -=1
    
print(f"Resultados da eleição \n Tião: {votos_tiao} votos \n Shaolin: {votos_shaolin} votos \n Zé: {votos_ze} votos")

