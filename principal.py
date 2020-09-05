import time
contaminacao = 0
sangue = 1000
resposta = 0

mascara = 0
estojo = 0
lanche = 0
time.sleep(2)
print("Mãe: Veja se não está esquecendo algo!")
time.sleep(2)

while (mascara <= 0) or (estojo <= 0) or (lanche <= 0):
    print("*Você verifica os bolsos, algo está faltando, o que é?*\n"
          "1 - Estojo?\n"
          "2 - Mascara e alcool em gel?\n"
          "3 - Lanche?\n"
          "4 - Nada?")

    resposta = int(input("Escreva o número da sua resposta: "))

    if (resposta == 1):
        resposta = 0
        estojo += 1
        time.sleep(2)
        print("Hm...talvez não seja a melhor opção, mas é hora de ir!")
        contaminacao += 10
        sangue -= 10
        time.sleep(4)
    elif (resposta == 2):
        resposta = 0
        mascara +=1
        print("É muito importante usar mascara e alcool em gel! Escolha perfeita!")
        print("Você ganhou 10 pontos de vida!")
        contaminacao -= 10
        sangue += 10
        time.sleep(4)
    elif (resposta == 3):
        resposta = 0
        lanche += 1
        print("É importante se manter alimentado! Mas, talvez esteja esquecendo algo mais importante...")
        time.sleep(2)
        contaminacao += 10
        sangue -= 10
        time.sleep(4)
    elif (resposta == 4):
        resposta = 0
        print("Você tem certeza? Melhor pensar direito!")
        time.sleep(2)
