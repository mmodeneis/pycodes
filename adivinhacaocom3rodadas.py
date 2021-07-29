print("*********************************")
print("Bem Vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa:", rodada, "de", total_de_tentativas)


    chute_str = input("Digite o Número: ")

    print("Você Digitou" , chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você Errou! Seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você Errou! Seu chute foi menor que o número secreto.")

    rodada = rodada + 1




    print("*********************************")
    print("Fim do Jogo!")
    print("*********************************")
