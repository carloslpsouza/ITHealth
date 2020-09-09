import time

contaminacao = 0
sangue = 1000
resposta = 0
resp = 0

print("="*25)
print("Bem vindo ao Schooldemic!")
print("="*25)

print("-"*110)
print("Tutorial:\n"
      "Toda vez que você executar uma ação que possa te expor ao virus sua contaminação aumenta e sua vida diminui! \n"
      "Você pode recuperar vida tomando decisões certas! Com isso, o nivel de contaminação diminui!")
#time.sleep(4)
print("Se o seu nivel de contaminação chegar ao maximo você perde!")
print("-"*110)
#time.sleep(5)
print("Qual é o seu nome?")
nome = str(input(""))
print("Seja bem-vindo, {}! Vamos começar?".format(nome))
#time.sleep(3)

while contaminacao < 100:

    print("Estamos em 2020, uma grande pandemia se alastrou pelo mundo...")
    #time.sleep(3)
    print("...Isso fez com que o governo declarasse quarentena geral...")
    #time.sleep(3)
    print("...Todos deveriam ficar em casa e só poderiam sair em situações especiais...")
    #time.sleep(3)
    print("...Com as escolar não foi diferente, as aulas foram paralizadas...")
    #time.sleep(3)
    print("...Após meses de tédio e isolamento a pandemia começou a perder força...")
    #time.sleep(3)
    print("...As escolas estavam planejando a volta as aulas, tomando todas as medidas necessarias...")
    #time.sleep(3)
    print("...Todos devem usar mascaras, alcool em gel e evitar contato fisico...")
    #time.sleep(3)
    print("...Sua missão? Simples! Ir a escola sem se contaminar...")
    #time.sleep(3)
    print("Hora de ir a escola!")
    #time.sleep(3)
    #adicionar barulho de despertador
    print("*Você esta sonolento...*")
    #time.sleep(3)
    print("*...mas, precisa levantar...*")
    #time.sleep(3)
    print("*Você escuta sua mãe chamando!*")
    #time.sleep(3)
    print("Mãe: {}! É melhor levantar! Vai acabar se atrasando!".format(nome))
    #time.sleep(4)

    print("Você levantou! Para onde deseja ir?\n"
          "1 - Sala \n"
          "2 - Banheiro \n"
          "3 - Cozinha")

    resposta = int(input("Digite o número da sua resposta: "))
    #sala
    if (resposta == 1):
        resposta = 0
        print("*Noticia na televisão*")
        #time.sleep(3)
        print("...As aulas voltam hoje! Alunos se preparam para retonar o mais seguros possivel!...")
        print("Não há mais nada de interessante aqui! Para onde deseja ir?\n"
              "Você já esta na sala!\n"
              "2 - Banheiro \n"
              "3 - Cozinha \n")
        resposta = int(input("Digite o número da sua resposta: "))
        #banheiro
        if (resposta == 2):
            resposta = 0
            while resp != 2 and resp != 3:
                print("*Gostaria de tomar um banho?*\n"
                      "1 - Sim \n"
                      "2 - Não")
                resp = int(input("Digite o número da sua resposta: "))

                if (resp == 1):
                    resp = 0
                    print("Nada melhor que um bom banho para iniciar bem o dia!")
                    print("*Você encontrou um pote de alcool em gel no banheiro!*")
                    print("Você ganhou 5 pontos de vida!")
                    sangue += 5
                    break
                if (resp == 2):
                    resp = 0
                    print("Nesses tempos de pandemia higiene é muito importante!")
                    break
                else:
                    print('Resposta invalida!')
                    #fim banheiro
                    #cozinha
            if (resposta == 3):
                resposta = 0
                # Essa parte será disparada quando o personagem se aproximar da mãe
                print("Mãe: Olha só quem finalmente levantou!")
                # time.sleep(2)
                print("Mãe: Acabei de vir da feira, comprei frutas fresquinhas para seu café da manhã!")
                # time.sleep(2)
                print("Mãe: É importante se manter muito bem alimentado, pois isso aumenta sua imunidade!")
                # time.sleep(2)
                while resp != 1 and resp != 2:
                    print("Mãe: Você está com fome?")
                    # time.sleep(1)
                    print("1 - Sim, adoraria frutas para o café!")
                    print("2 - Não, prefiro não comer nada!")

                    resp = int(input("Digite sua resposta: "))
                    if (resp == 1):
                        print("Mãe: Ótimo! Aqui estão! Só não tive tempo de lava-las ainda, acabei de chegar!")
                        resp = 0
                        sangue += 10
                        break
                    if (resp == 2):
                        print("Mãe: MAS, VAI COMER MESMO ASSIM!")
                        # time.sleep(2)
                        print("Mãe: Er..digo, você precisa comer. Tem que se manter forte!\n"
                              "Não tive tempo de lavar as frutas ainda pois acabei de chegar!")
                        contaminacao += 20
                        sangue -= contaminacao
                        resp = 0
                        break
                    else:
                        print('Resposta invalida!')
                while resp != 1 and resp != 2:
                    # time.sleep(2)
                    print("1 - Comer a fruta que sua mãe trouxe.")
                    print("2 - Lavar a fruta antes e depois come-la!")

                    resp = int(input("O que vai fazer? "))
                    # tempo para o personagem comer
                    print("*Mastigando...*")
                    # time.sleep(4)
                    if (resp == 1):
                        print("Cuidado ao consumir alimentos que não foram devidamente lavados!")
                        resp = 0
                        contaminacao += 20
                        sangue -= 20
                        break
                        # time.sleep(2)
                    if (resp == 2):
                        resp = 0
                        print(
                            "Bem lembrado, {}! É importante lavar bem os alimentos antes de consumi-los!".format(nome))
                        # time.sleep(2)
                        print("Mesmo se não estivermos em uma pandemia.")
                        break
                    else:
                        print('Resposta invalida!')

                print("Não há mais nada de interessante aqui!\n"
                      "4 - Ir para a escola!")
                #fim cozinha

                resposta = int(input("Digite o número da sua resposta: "))

            print("Não há mais nada de interessante aqui! Para onde deseja ir?\n"
                  "1 - Sala\n"
                  "Você já está no banheiro \n"
                  "3 - Cozinha \n")
            resposta = int(input("Digite o número da sua resposta: "))
            #fim da sala
    if (resposta == 2): #banheiro
        resposta = 0
        while resp != 1 and resp != 2:
            print("*Gostaria de tomar um banho?*\n"
                "1 - Sim \n"
                "2 - Não")
            resp = int(input("Digite o número da sua resposta: "))

            if (resp == 1):
                resp = 0
                print("Nada melhor que um bom banho para iniciar bem o dia!")
                print("*Você encontrou um pote de alcool em gel no banheiro!*")
                print("Você ganhou 5 pontos de vida!")
                sangue += 5
                break
            if (resp == 2):
                resp = 0
                print("Nesses tempos de pandemia higiene é muito importante!")
                break
            else:
                print('Resposta invalida!')

        print("Não há mais nada de interessante aqui! Para onde deseja ir?\n"
                "1 - Sala\n"
                "Você já está no banheiro \n"
                "3 - Cozinha \n")
        resposta = int(input("Digite o número da sua resposta: "))
        #sala
        if (resposta == 1):
            resposta = 0
            print("*Noticia na televisão*")
            # time.sleep(3)
            print("...As aulas voltam hoje! Alunos se preparam para retonar o mais seguros possivel!...")
            print("Não há mais nada de interessante aqui! Para onde deseja ir?\n"
                  "Você já esta na sala!\n"
                  "2 - Banheiro \n"
                  "3 - Cozinha \n")
            resposta = int(input("Digite o número da sua resposta: "))
            if (resposta == 2):
                resposta = 0
                while resp != 2 and resp != 3:
                    print("*Gostaria de tomar um banho?*\n"
                          "1 - Sim \n"
                          "2 - Não")
                    resp = int(input("Digite o número da sua resposta: "))

                    if (resp == 1):
                        resp = 0
                        print("Nada melhor que um bom banho para iniciar bem o dia!")
                        print("*Você encontrou um pote de alcool em gel no banheiro!*")
                        print("Você ganhou 5 pontos de vida!")
                        sangue += 5
                        break
                    if (resp == 2):
                        resp = 0
                        print("Nesses tempos de pandemia higiene é muito importante!")
                        break
                    else:
                        print('Resposta invalida!')
                if (resposta == 3):
                    resposta = 0
                    # Essa parte será disparada quando o personagem se aproximar da mãe
                    print("Mãe: Olha só quem finalmente levantou!")
                    # time.sleep(2)
                    print("Mãe: Acabei de vir da feira, comprei frutas fresquinhas para seu café da manhã!")
                    # time.sleep(2)
                    print("Mãe: É importante se manter muito bem alimentado, pois isso aumenta sua imunidade!")
                    # time.sleep(2)
                    while resp != 1 and resp != 2:
                        print("Mãe: Você está com fome?")
                        # time.sleep(1)
                        print("1 - Sim, adoraria frutas para o café!")
                        print("2 - Não, prefiro não comer nada!")

                        resp = int(input("Digite sua resposta: "))
                        if (resp == 1):
                            print("Mãe: Ótimo! Aqui estão! Só não tive tempo de lava-las ainda, acabei de chegar!")
                            resp = 0
                            sangue += 10
                            break
                        if (resp == 2):
                            print("Mãe: MAS, VAI COMER MESMO ASSIM!")
                            # time.sleep(2)
                            print("Mãe: Er..digo, você precisa comer. Tem que se manter forte!\n"
                                  "Não tive tempo de lavar as frutas ainda pois acabei de chegar!")
                            contaminacao += 20
                            sangue -= contaminacao
                            resp = 0
                            break
                        else:
                            print('Resposta invalida!')
                    while resp != 1 and resp != 2:
                        # time.sleep(2)
                        print("1 - Comer a fruta que sua mãe trouxe.")
                        print("2 - Lavar a fruta antes e depois come-la!")

                        resp = int(input("O que vai fazer? "))
                        # tempo para o personagem comer
                        print("*Mastigando...*")
                        # time.sleep(4)
                        if (resp == 1):
                            print("Cuidado ao consumir alimentos que não foram devidamente lavados!")
                            resp = 0
                            contaminacao += 20
                            sangue -= 20
                            break
                            # time.sleep(2)
                        if (resp == 2):
                            resp = 0
                            print(
                                "Bem lembrado, {}! É importante lavar bem os alimentos antes de consumi-los!".format(
                                    nome))
                            # time.sleep(2)
                            print("Mesmo se não estivermos em uma pandemia.")
                            break
                        else:
                            print('Resposta invalida!')

                    print("Não há mais nada de interessante aqui!\n"
                          "4 - Ir para a escola!")

                    resposta = int(input("Digite o número da sua resposta: "))

                print("Não há mais nada de interessante aqui! Para onde deseja ir?\n"
                      "1 - Sala\n"
                      "Você já está no banheiro \n"
                      "3 - Cozinha \n")
                resposta = int(input("Digite o número da sua resposta: "))
                # fim da sala

                if (resposta == 3):  # inicio cozinha
                    resposta = 0
                    # Essa parte será disparada quando o personagem se aproximar da mãe
                    print("Mãe: Olha só quem finalmente levantou!")
                    # time.sleep(2)
                    print("Mãe: Acabei de vir da feira, comprei frutas fresquinhas para seu café da manhã!")
                    # time.sleep(2)
                    print("Mãe: É importante se manter muito bem alimentado, pois isso aumenta sua imunidade!")
                    # time.sleep(2)
                    while resp != 1 and resp != 2:
                        print("Mãe: Você está com fome?")
                        # time.sleep(1)
                        print("1 - Sim, adoraria frutas para o café!")
                        print("2 - Não, prefiro não comer nada!")

                        resp = int(input("Digite sua resposta: "))
                        if (resp == 1):
                            print("Mãe: Ótimo! Aqui estão! Só não tive tempo de lava-las ainda, acabei de chegar!")
                            resp = 0
                            sangue += 10
                            break
                        if (resp == 2):
                            print("Mãe: MAS, VAI COMER MESMO ASSIM!")
                            # time.sleep(2)
                            print("Mãe: Er..digo, você precisa comer. Tem que se manter forte!\n"
                                  "Não tive tempo de lavar as frutas ainda pois acabei de chegar!")
                            contaminacao += 20
                            sangue -= contaminacao
                            resp = 0
                            break
                        else:
                            print('Resposta invalida!')
                    while resp != 1 and resp != 2:
                        # time.sleep(2)
                        print("1 - Comer a fruta que sua mãe trouxe.")
                        print("2 - Lavar a fruta antes e depois come-la!")

                        resp = int(input("O que vai fazer? "))
                        # tempo para o personagem comer
                        print("*Mastigando...*")
                        # time.sleep(4)
                        if (resp == 1):
                            print("Cuidado ao consumir alimentos que não foram devidamente lavados!")
                            resp = 0
                            contaminacao += 20
                            sangue -= 20
                            break
                            # time.sleep(2)
                        if (resp == 2):
                            resp = 0
                            print("Bem lembrado, {}! É importante lavar bem os alimentos antes de consumi-los!".format(
                                nome))
                            # time.sleep(2)
                            print("Mesmo se não estivermos em uma pandemia.")
                            break
                        else:
                            print('Resposta invalida!')

                    print("Não há mais nada de interessante aqui!\n"
                          "4 - Ir para a escola!")

                    resposta = int(input("Digite o número da sua resposta: "))
                    # fim cozinha

                #fim do banheiro

    if (resposta == 3): #inicio cozinha
        resposta = 0
        # Essa parte será disparada quando o personagem se aproximar da mãe
        print("Mãe: Olha só quem finalmente levantou!")
        # time.sleep(2)
        print("Mãe: Acabei de vir da feira, comprei frutas fresquinhas para seu café da manhã!")
        # time.sleep(2)
        print("Mãe: É importante se manter muito bem alimentado, pois isso aumenta sua imunidade!")
        # time.sleep(2)
        while resp != 1 and resp != 2:
            print("Mãe: Você está com fome?")
            # time.sleep(1)
            print("1 - Sim, adoraria frutas para o café!")
            print("2 - Não, prefiro não comer nada!")

            resp = int(input("Digite sua resposta: "))
            if (resp == 1):
                print("Mãe: Ótimo! Aqui estão! Só não tive tempo de lava-las ainda, acabei de chegar!")
                resp = 0
                sangue += 10
                break
            if (resp == 2):
                print("Mãe: MAS, VAI COMER MESMO ASSIM!")
                # time.sleep(2)
                print("Mãe: Er..digo, você precisa comer. Tem que se manter forte!\n"
                      "Não tive tempo de lavar as frutas ainda pois acabei de chegar!")
                contaminacao += 20
                sangue -= contaminacao
                resp = 0
                break
            else:
                print('Resposta invalida!')
        while resp != 1 and resp != 2:
            # time.sleep(2)
            print("1 - Comer a fruta que sua mãe trouxe.")
            print("2 - Lavar a fruta antes e depois come-la!")

            resp = int(input("O que vai fazer? "))
            #tempo para o personagem comer
            print("*Mastigando...*")
            # time.sleep(4)
            if (resp == 1):
                print("Cuidado ao consumir alimentos que não foram devidamente lavados!")
                resp = 0
                contaminacao += 20
                sangue -= 20
                break
                # time.sleep(2)
            if (resp == 2):
                resp = 0
                print("Bem lembrado, {}! É importante lavar bem os alimentos antes de consumi-los!".format(nome))
                # time.sleep(2)
                print("Mesmo se não estivermos em uma pandemia.")
                break
            else:
                print('Resposta invalida!')

        print("Não há mais nada de interessante aqui!\n"
              "4 - Ir para a escola!")

        resposta = int(input("Digite o número da sua resposta: "))
        #fim cozinha

    # Quando o personagem for abrir a porta

    if (resposta == 4):
        mascara = 0
        estojo = 0
        lanche = 0
        resposta = 0
        # time.sleep(2)
        print("Mãe: Veja se não está esquecendo algo?")
        # time.sleep(2)
        while resp != 1 and resp != 2 and resp != 3:
            print("*Você verifica os bolsos, algo está faltando, o que é?*\n"
                  "1 - Estojo?\n"
                  "2 - Mascara e alcool em gel?\n"
                  "3 - Lanche?\n")

            resp = int(input("Escreva o número da sua resposta: "))

            if (resp == 1):
                resp = 0
                estojo += 1
                #time.sleep(2)
                print("Hm...talvez não seja a melhor opção, mas é hora de ir!")
                contaminacao += 10
                sangue -= 10
                #time.sleep(4)
                break
            if (resp == 2):
                resp = 0
                mascara += 1
                print("É muito importante usar mascara e alcool em gel! Escolha perfeita!")
                print("Você ganhou 10 pontos de vida!")
                contaminacao -= 10
                sangue += 10
                #time.sleep(4)
                break
            if (resp == 3):
                resp = 0
                lanche += 1
                print("É importante se manter alimentado! Mas, talvez esteja esquecendo algo mais importante...")
                #time.sleep(2)
                contaminacao += 10
                sangue -= 10
                #time.sleep(4)
                break
            else:
                print('Resposta invalida!')
    break


#Caso o personagem não escolha nada, repetir.
while contaminacao < 100:

#O personagem tem que retornar para procurar o item


    print("="*20)
    print("Caminho da escola")
    print("="*20)
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
