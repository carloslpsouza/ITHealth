import pygame, sys
import quebraLinha
import ranking
import threading
from pygame.locals import *
from perguntas import *
import webbrowser

global screen
global event
global mus_menu
global mus_jogo
global fps
global pts
global s_tam
global sangue_skin

pygame.init()  # inicializa todos os modulos do pygame
pygame.mixer.init() # inicia métodos de som

fps = 10 # Frames do jogo
randon = aleatorio() # Cria uma sequencia aletaoria para as perguntas seguirem em ordem aleatória
s_tam = 0
sangue_skin = pygame.Surface((0, 32))

print(randon)

# Variáveis Sprites
fundo_mapa = pygame.image.load('SPRITES/fundo-menu.png')
abertura = pygame.image.load('SPRITES/logo-inicial.png')
menu = pygame.image.load('SPRITES/tela-inicial.png')
tela_nome = pygame.image.load('SPRITES/tela-nome.png')
q_gd_pergunta = pygame.image.load('SPRITES/quadro-grande-pergunta.png')
game_over = pygame.image.load('SPRITES/game-over.png')
imgvitoria = pygame.image.load('SPRITES/tela-vitoria.png')
op_a = pygame.image.load('SPRITES/a.png')
op_b = pygame.image.load('SPRITES/b.png')
op_c = pygame.image.load('SPRITES/c.png')
op_d = pygame.image.load('SPRITES/d.png')
virus = pygame.image.load('SPRITES/virus-contorno-branco.png')
virus_barra = pygame.image.load('SPRITES/barra-sangue-contorno-branco.png')
resposta_errada = pygame.image.load('SPRITES/resposta_errada.png')
resposta_certa = pygame.image.load('SPRITES/resposta_certa.png')
qdjogador = pygame.image.load('SPRITES/jogador-pontos.png')
qdtimer = pygame.image.load('SPRITES/timer.png')
logo = pygame.image.load('SPRITES/logo.png')
ambulancia = pygame.image.load('SPRITES/ambulancia.png')
#

# Fontes
fonte_default = pygame.font.match_font('FreeSans')  # Encontra caminho absoluto fonte no SO
fonte_dimis = pygame.font.match_font('Dimiss')  # Encontra caminho absoluto fonte no SO
fonte_dimitri = pygame.font.match_font('Dimitri')  # Encontra caminho absoluto fonte no SO
fonte_perguntas = pygame.font.Font('FONTES/Roboto/Roboto-Bold.ttf', 28)
fonte_ranking = pygame.font.Font(fonte_dimitri, 45)
#

# Variaveis de cores
preto = (50, 64, 50)
amarelo = (255, 255, 0)
branco = (255, 255, 255)
#

# Variáveis de tela
twidth = 1366
theight = 768
#

clock = pygame.time.Clock()  # Cria um objeto que ajuda a controlar o tempo

# Variáveis efeitos musica
intro = pygame.mixer.Sound('TRILHA/efeitointro.wav')
selecao = pygame.mixer.Sound('TRILHA/tiro.wav')
certa = pygame.mixer.Sound('TRILHA/certa.wav')
errada = pygame.mixer.Sound('TRILHA/errada.wav')
#

def musicaFundo(trilha):
    pygame.mixer.music.load(trilha)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)


def exibeTexto(txt, tam_fonte, cor, fonte):  # função que facilita a rederização de texto na tela é so passar o texto e o tamanho
    fonte_padrao = pygame.font.Font(fonte,tam_fonte)  # criar um objeto Font a partir das fontes do sistema SysFont (nome, tamanho, negrito = Falso, itálico = Falso)
    texto_surface = fonte_padrao.render(txt, False, cor)  # Renderiza o texto passado pelo parametro txt
    return texto_surface

def vitoria(twidth, theight, nomeJogador, pts, tempo):
    global screen, event, fps
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    mus_jogo = threading.Thread(target=musicaFundo, args=('TRILHA/vitoria.wav',))
    mus_jogo.start()

    saiGame = True
    while saiGame:
        clock.tick(fps)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            print(pos)

            if 920 > pos[0] > 420 and 720 > pos[1] > 650:  # Testa se o clique foi no indicado (JOGAR NOVAMENTE)
                mus_jogo._stop()
                saiGame = False
                jogo(twidth, theight, nomeJogador, 0, 0, 0, 0)

            if 640 > pos[0] > 240 and 620 > pos[1] > 530:  # Testa se o clique foi no indicado (VOLTA TELA NOME)
                mus_jogo._stop()
                saiGame = False
                jogador(twidth, theight)

            if 1120 > pos[0] > 730 and 620 > pos[1] > 530:  # Testa se o clique foi no indicado (SAI DO JOGO)
                pygame.quit()
                sys.exit()

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(imgvitoria, (0, 0)) # tela do fundo
        screen.blit(exibeTexto(pts, 55, preto, fonte_dimitri), ((twidth / 2) - 210, 380))
        screen.blit(exibeTexto(tempo, 55, preto, fonte_dimitri), ((twidth / 2) - 210, 430))
        pygame.display.update()  # Atualiza os retangulos defindos

def gameOver(twidth, theight, nomeJogador, pts, tempo):
    global screen, event, fps
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    mus_jogo = threading.Thread(target=musicaFundo, args=('TRILHA/derrota.wav',))
    mus_jogo.start()

    saiGame = True
    while saiGame:
        clock.tick(fps)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            print(pos)

            if 920 > pos[0] > 420 and 720 > pos[1] > 650:  # Testa se o clique foi no indicado (JOGAR NOVAMENTE)
                saiGame = False
                mus_jogo._stop()
                jogo(twidth, theight, nomeJogador, 0, 0, 0, 0)

            if 640 > pos[0] > 240 and 620 > pos[1] > 530:  # Testa se o clique foi no indicado (VOLTA TELA NOME)
                saiGame = False
                mus_jogo._stop()
                jogador(twidth, theight)

            if 1120 > pos[0] > 730 and 620 > pos[1] > 530:  # Testa se o clique foi no indicado (SAI DO JOGO)
                pygame.quit()
                sys.exit()

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(game_over, (0, 0))
        screen.blit(exibeTexto(pts, 55, preto, fonte_dimitri), ((twidth / 2) - 210, 380))
        screen.blit(exibeTexto(tempo, 55, preto, fonte_dimitri), ((twidth / 2) - 210, 430))
        pygame.display.update()  # Atualiza os retangulos defindos




def jogo(twidth, theight, nomeJogador, contador = 0, pontos = 0, pontos_contaminacao = 0, tempo = 0):
    import Counter
    global screen, event, fps, pts, s_tam, sangue_skin, mus_jogo

    opcoes = ['A', 'B', 'C', 'D'] # Quando busca a pergunta no banco, retira a resposta certa do array para testar a errada

    # Sangue
    yp = 34
    s_ini = 80
    #

    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    # tratamento quebra de linha
    quadro_pergunta = pygame.Surface((1000, 290), pygame.SRCALPHA, 32)
    quadro_pergunta = quadro_pergunta.convert_alpha()
    bloco = pygame.Rect(5, 5, 940, 290)

    quadro_a = pygame.Surface((440, 100), pygame.SRCALPHA, 32)
    quadro_a  = quadro_a.convert_alpha()
    bloco_a = pygame.Rect(5, 5, 440, 100)

    quadro_b = pygame.Surface((440, 100), pygame.SRCALPHA, 32)
    quadro_b = quadro_b.convert_alpha()
    bloco_b = pygame.Rect(5, 5, 440, 100)

    quadro_c = pygame.Surface((440, 100), pygame.SRCALPHA, 32)
    quadro_c = quadro_c.convert_alpha()
    bloco_c = pygame.Rect(5, 5, 440, 100)

    quadro_d = pygame.Surface((440, 100), pygame.SRCALPHA, 32)
    quadro_d = quadro_d.convert_alpha()
    bloco_d = pygame.Rect(5, 5, 440, 100)
    #

    resposta = ""
    while True:
        clock.tick(fps)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps

        if contador == (len(randon)): # testa se o jogo acabou
            if pontos <= 50 : # se o jogo acabou menor que 50 pontos, gameOver
                gameOver(twidth, theight, nomeJogador, pts, Counter.tempoCorrido())
            print("Vc ganhou")
            s_tam = 0
            tempo = Counter.tempoCorrido() # Inicia cronometro do jogo
            ranking.atualizaRanking(nomeJogador, tempo[8:], pontos)
            mus_jogo._stop()
            vitoria(1366, 768, nomeJogador, pts, Counter.tempoCorrido())

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            #pygame.time.wait(500)
            #print(pos)
            opc_a = 320 > pos[0] > 120 and 600 > pos[1] > 500
            opc_b = 640 > pos[0] > 440 and 600 > pos[1] > 500
            opc_c = 940 > pos[0] > 740 and 600 > pos[1] > 500
            opc_d = 1240 > pos[0] > 1040 and 600 > pos[1] > 500
            if opc_a:  # Testa se o clique foi no indicado
                resposta = 'A'
            if opc_b:  # Testa se o clique foi no indicado
                resposta = 'B'
            if opc_c:  # Testa se o clique foi no indicado
                resposta = 'C'
            if opc_d:  # Testa se o clique foi no indicado
                resposta = 'D'

        if pontos_contaminacao < 100:  # testa se ainda tem pontos e exibe o jogo
            screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
            screen.blit(fundo_mapa, (0, 0))

            #screen.blit(q_gd_pergunta, ((twidth / 2) - 613, 130))
            #screen.blit(quadro_pergunta, ((twidth / 2) - 560, 150))
            screen.blit(q_gd_pergunta, ((twidth / 2) - 563, 130))
            screen.blit(quadro_pergunta, ((twidth / 2) - 540, 150))

            screen.blit(quadro_a, (200, 300))
            screen.blit(quadro_b, (700, 300))
            screen.blit(quadro_c, (200, 350))
            screen.blit(quadro_d, (700, 350))

            screen.blit(virus_barra, (s_ini - 4, 30))
            sangue_skin = pygame.Surface((s_tam, 32))

            if pontos_contaminacao <= 20:
                sangue_skin.fill((26,140,0))  # cor do bloco
            elif 20 < pontos_contaminacao <= 30:
                sangue_skin.fill((140, 140, 0))  # cor do bloco
            elif 30 < pontos_contaminacao <= 40:
                sangue_skin.fill((190, 190, 0))  # cor do bloco
            elif 40 < pontos_contaminacao <= 50:
                sangue_skin.fill((255, 255, 0))  # cor do bloco
            elif 50 < pontos_contaminacao <= 60:
                sangue_skin.fill((255, 145, 0))  # cor do bloco
            elif 60 < pontos_contaminacao <= 70:
                sangue_skin.fill((255, 90, 0))  # cor do bloco
            elif 70 < pontos_contaminacao <= 80:
                sangue_skin.fill((255, 130, 0))  # cor do bloco
            elif 80 < pontos_contaminacao:
                sangue_skin.fill((255, 0, 0))  # cor do bloco

            screen.blit(sangue_skin, (s_ini, yp))
            screen.blit(virus, (10, 10))

            screen.blit(qdtimer, ((twidth / 2) - 150, 10))
            tempo = Counter.tempoCorrido()
            screen.blit(exibeTexto(tempo[6:], 60, preto, fonte_dimitri), ((twidth / 2) - 150, 20))

            screen.blit(qdjogador, (twidth - 260, 10))
            #screen.blit(exibeTexto("Jogador   ", 25, amarelo, fonte_dimitri), (twidth - 200, 10))
            screen.blit(exibeTexto(nomeJogador, 40, preto, fonte_dimitri), (twidth - 230, 15))
            pts = ("Pontos " + str(pontos))
            screen.blit(exibeTexto(pts, 40, preto, fonte_dimitri), (twidth - 230, 50))

            screen.blit(op_a, (120, 500))
            screen.blit(op_b, (440, 500))
            screen.blit(op_c, (740, 500))
            screen.blit(op_d, (1040, 500))

            pergunta = selecionaQuestao(randon[contador] * 7)

            quebraLinha.drawText(quadro_pergunta, pergunta[0], preto, bloco, fonte_perguntas)
            quebraLinha.drawText(quadro_a, pergunta[1], preto, bloco_a, fonte_perguntas)
            quebraLinha.drawText(quadro_b, pergunta[2], preto, bloco_b, fonte_perguntas)
            quebraLinha.drawText(quadro_c, pergunta[3], preto, bloco_c, fonte_perguntas)
            quebraLinha.drawText(quadro_d, pergunta[4], preto, bloco_d, fonte_perguntas)

            if pergunta[6] in opcoes: # Verifica se a resposta certa esta no array opções
                opcoes.remove(str(pergunta[6])) # Remove a opção certa do arrat
            if resposta == pergunta[6]: # Testa se a resposta escolhida é a certa
                certa.play()
                fecha_janela = 1
                while fecha_janela:
                    screen.blit(resposta_certa, ((twidth / 2) - 482, (theight/2) - 261))
                    pygame.display.update()
                    pygame.time.wait(1000)
                    fecha_janela = 0

                print("certa resposta")
                contador += 1
                pontos += int(pergunta[5])
                jogo(twidth, theight, nomeJogador, contador, pontos, pontos_contaminacao)

            if resposta in opcoes: # Testa se a opção escolhida esta nas opções após remover a resposta certa
                errada.play()
                fecha_janela = 1
                while fecha_janela:
                    screen.blit(resposta_errada, ((twidth / 2) - 482, (theight / 2) - 261))
                    #screen.blit(exibeTexto(pergunta[6], 200, preto, fonte_dimitri), ((twidth / 2)-30, (theight / 2)))
                    if pergunta[6] == 'A':
                        screen.blit(exibeTexto(pergunta[1], 50, preto, fonte_default),((twidth / 2) - (len(pergunta[1])//2)*20, (theight / 2)))
                    if pergunta[6] == 'B':
                        screen.blit(exibeTexto(pergunta[2], 50, preto, fonte_default),((twidth / 2) - (len(pergunta[2])//2)*20, (theight / 2)))
                    if pergunta[6] == 'C':
                        screen.blit(exibeTexto(pergunta[3], 50, preto, fonte_default),((twidth / 2) - (len(pergunta[3])//2)*20, (theight / 2)))
                    if pergunta[6] == 'D':
                        screen.blit(exibeTexto(pergunta[4], 50, preto, fonte_default),((twidth / 2) - (len(pergunta[4])//2)*20, (theight / 2)))
                    pygame.display.update()
                    pygame.time.wait(1000)
                    fecha_janela = 0

                print('Errada')
                contador += 1
                s_tam += 43
                pontos_contaminacao += 10

                pygame.display.update()
                jogo(twidth, theight, nomeJogador, contador, pontos, pontos_contaminacao)

            resposta = ""

            #print("pontos: ", pontos, "Contam: ", pontos_contaminacao, "Contador: ", contador, "Tam rand: ", len(randon), "Random: ", randon, pergunta[6])

        else:  # Apaga tudo e exibe o Game over
            s_tam = 0
            tempo = Counter.tempoCorrido()
            ranking.atualizaRanking(nomeJogador, tempo[8:], pontos)
            mus_jogo._stop()
            gameOver(twidth, theight, nomeJogador, pts, Counter.tempoCorrido())

        pygame.display.update()  # Atualiza os retangulos defindos


def planMenu(twidth, theight, nomeJogador):
    global screen, event, mus_menu, fps, mus_jogo
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    #quadro ranking
    quadro_ranking = pygame.Surface((200, 290), pygame.SRCALPHA, 32)
    #quadro_ranking = quadro_ranking.convert_alpha()
    #bloco_ranking = pygame.Rect(5, 5, 200, 290)
    #

    saiMenu = True
    while saiMenu:
        clock.tick(fps)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            #print(pos)

            if 1200 > pos[0] > 800 and 450 > pos[1] > 380:  # Testa se o clique foi no indicado (JOGAR)
                selecao.play()
                pygame.time.wait(500)
                saiMenu = False

            if 1200 > pos[0] > 800 and 560 > pos[1] > 480:  # Testa se o clique foi no indicado (COMO JOGAR)
                selecao.play()
                webbrowser.open('https://github.com/carloslpsouza/ITHealth')

            if 1200 > pos[0] > 800 and 680 > pos[1] > 600:  # Testa se o clique foi no indicado (SOBRE O JOGO)
                selecao.play()
                webbrowser.open('https://github.com/carloslpsouza/ITHealth')

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(menu, (0, 0))
        rankingArray = ranking.leRanking()
        mem = 0
        for i in range(3):
            indice = (i * 3)
            rankpts = rankingArray[indice]
            ranknome = rankingArray[indice + 1]
            ranktempo = rankingArray[indice + 2]
            ranksai = str(rankpts[:-1] + "   " + ranktempo[:-1])
            screen.blit(exibeTexto(ranknome[:-1], 45, preto, fonte_dimitri), ((twidth / 2) - 530, 300 + mem))
            screen.blit(exibeTexto(ranksai, 45, preto, fonte_dimitri), ((twidth / 2) - 330, 300 + mem))
            mem += 100

        pygame.display.update()  # Atualiza os retangulos defindos
    mus_menu._stop()
    mus_jogo = threading.Thread(target=musicaFundo, args=('TRILHA/fundo-jogo.wav',))
    mus_jogo.start()
    jogo(twidth, theight, nomeJogador, 0, 0, 0)


def jogador(twidth, theight):
    global screen, event, mus_menu, fps
    mus_menu = threading.Thread(target=musicaFundo, args=('TRILHA/menu.wav', ))
    mus_menu.start()
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    userName = ""
    saiNome = True
    while saiNome:
        clock.tick(fps)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    userName = userName[:-1]
                else:
                    userName += event.unicode
                    nomeJogador = userName[:-1]
                if event.key == pygame.K_RETURN:
                    selecao.play()
                    pygame.time.wait(1000)
                    saiNome = False

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(tela_nome, (0, 0))

        screen.blit(exibeTexto(userName, 50, preto, fonte_dimitri), ((twidth / 2) - 400, (theight / 2) - 60))

        pygame.display.update()  # Atualiza os retangulos defindos

    planMenu(twidth, theight, nomeJogador)


def entrada(twidth, theight):
    global screen, event, fps
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela
    saiEntrada = True
    while saiEntrada:
        clock.tick(fps)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(abertura, (0, 0))
        pygame.display.update()  # Atualiza os retangulos defindos
        pygame.time.wait(2000)
        saiEntrada = False
    jogador(twidth, theight)



def introducao(twidth, theight):
    global screen, event, fps
    screen = pygame.display.set_mode((twidth, theight))
    pygame.display.set_caption('QuizDemic')
    saiEntrada = True
    while saiEntrada:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == quit:
                pygame.quit()
                sys.exit()

        screen.fill(preto)
        toca = 0
        for i in range(14):
            screen.fill(branco)
            if i >= 7:
                screen.blit(logo, ((twidth / 2) - 210, (theight / 2) - 200))
                if (toca == 0):
                    intro.play()
                    toca = 1
            if i == 0:
                screen.blit(ambulancia, (-100, (theight / 2) - 200))
            screen.blit(ambulancia, ((100 * (i)), (theight / 2) - 200))
            pygame.time.wait(45)
            pygame.display.update()
        pygame.time.wait(750)
        saiEntrada = False
        entrada(twidth, theight)

introducao(twidth, theight)