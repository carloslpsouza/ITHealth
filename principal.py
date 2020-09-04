contaminacao = 0
sangue = 1000
resposta = 0

print("Bem vindo ao Schooldemic!\nVamos começar?")

while contaminacao < 100:

    print("Você está em casa")
    print("Sua mãe acabou de chegar em casa com diversas frutas para o seu café da manhã. O que você deve fazer com as frutas?")
    print("1 - Lavar a fruta antes de comer?")
    print("2 - Comer a fruta sem lavar?")

    resposta = int(input("Digite sua resposta: "))

    if (resposta == 1):
        print("Parabens voce acertou")
        resposta = 0
        sangue += 2
    elif (resposta == 2):
        print("Cuidado você perdeu 20 pontos\nComer frutas sem lavar pode ser um risco")
        contaminacao += 20
        sangue -= contaminacao
        resposta = 0

    print(contaminacao, " contaminação")
    print(sangue, " sangue\n")

    print("Caminho da escola")
    print("Chegou a hora de você ir para a escola. Nesse momento de pandemia, como você deve sair?")
    print("1 - Com mascara")
    print("2 - Sem mascara")


    resposta = int(input("Digite sua resposta: "))

    if (resposta == 1):
        print("Parabens voce acertou")
        resposta = 0
        sangue += 2
    elif (resposta == 2):
        print("Cuidado você perdeu 20 pontos\nComer frutas sem lavar pode ser um risco")
        contaminacao += 20
        sangue -= contaminacao
        resposta = 0

    print(contaminacao, " contaminação")
    print(sangue, " sangue\n")
    if (sangue > 1005):
        print("Parabéns você venceu")
        break


if (contaminacao >= 100):
    print("Ah você desse jeito você ficou doente!")
