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

fps = 6
randon = aleatorio()
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
virus = pygame.image.load('SPRITES/virus.png')
virus_barra = pygame.image.load('SPRITES/virus-barra-pq.png')
#

# Fontes
fonte_default = pygame.font.match_font('FreeSans')  # Encontra caminho absoluto fonte no SO
fonte_dimis = pygame.font.match_font('Dimiss')  # Encontra caminho absoluto fonte no SO
fonte_dimitri = pygame.font.match_font('Dimitri')  # Encontra caminho absoluto fonte no SO
fonte_perguntas = pygame.font.Font('FONTES/Roboto/Roboto-Light.ttf', 28)
fonte_ranking = pygame.font.Font(fonte_dimitri, 45)
#fonte_dimis = pygame.font.Font('FONTES/Dimis/dimis.ttf', 30)
#fonte_dimitri = pygame.font.Font('FONTES/Dimitri/dimitri.ttf', 30)
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

# Variáveis efeitos
selecao = pygame.mixer.Sound('TRILHA/tiro.wav')
certa = pygame.mixer.Sound('TRILHA/certa.wav')
errada = pygame.mixer.Sound('TRILHA/no-no-no.wav')
#

def musicaFundo(trilha):
    pygame.mixer.music.load(trilha)
    pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(1)


def exibeTexto(txt, tam_fonte, cor, fonte):  # função que facilita a rederização de texto na tela é so passar o texto e o tamanho
    fonte_padrao = pygame.font.Font(fonte,tam_fonte)  # criar um objeto Font a partir das fontes do sistema SysFont (nome, tamanho, negrito = Falso, itálico = Falso)
    texto_surface = fonte_padrao.render(txt, False, cor)  # Renderiza o texto passado pelo parametro txt
    return texto_surface

def vitoria(twidth, theight, nomeJogador, pts, tempo):
    global screen, event, fps
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    musicaFundo('TRILHA/redhot.mp3')

    saiGame = True
    while saiGame:
        clock.tick(fps)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            #print(pos)

            if 920 > pos[0] > 420 and 720 > pos[1] > 650:  # Testa se o clique foi no indicado
                saiGame = False
                jogo(1366, 768, nomeJogador)

            if 640 > pos[0] > 240 and 620 > pos[1] > 530:  # Testa se o clique foi no indicado
                saiGame = False
                jogador(1366, 768, )

            if 1120 > pos[0] > 730 and 620 > pos[1] > 530:  # Testa se o clique foi no indicado
                pygame.quit()
                sys.exit()

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(imgvitoria, (0, 0))
        screen.blit(exibeTexto(pts, 55, preto, fonte_dimitri), ((twidth / 2) - 210, 380))
        screen.blit(exibeTexto(tempo, 55, preto, fonte_dimitri), ((twidth / 2) - 210, 430))
        pygame.display.update()  # Atualiza os retangulos defindos

def gameOver(twidth, theight, nomeJogador, pts, tempo):
    global screen, event, fps
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    musicaFundo('TRILHA/sad.wav')

    saiGame = True
    while saiGame:
        clock.tick(fps)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            #print(pos)

            if 920 > pos[0] > 420 and 720 > pos[1] > 650:  # Testa se o clique foi no indicado
                saiGame = False
                jogo(1366, 768, nomeJogador)

            if 640 > pos[0] > 240 and 620 > pos[1] > 530:  # Testa se o clique foi no indicado
                saiGame = False
                jogador(1366, 768, )

            if 1120 > pos[0] > 730 and 620 > pos[1] > 530:  # Testa se o clique foi no indicado
                pygame.quit()
                sys.exit()

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(game_over, (0, 0))
        screen.blit(exibeTexto(pts, 55, preto, fonte_dimitri), ((twidth / 2) - 210, 380))
        screen.blit(exibeTexto(tempo, 55, preto, fonte_dimitri), ((twidth / 2) - 210, 430))
        pygame.display.update()  # Atualiza os retangulos defindos




def jogo(twidth, theight, nomeJogador, contador = 0, pontos = 0, pontos_contaminacao = 0):
    import Counter
    global screen, event, fps, pts, s_tam, sangue_skin, mus_jogo

    opcoes = ['A', 'B', 'C', 'D']

    # Sangue
    yp = 34
    s_ini = 110
    #

    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    # tratamento quebra de linha
    quadro_pergunta = pygame.Surface((900, 290), pygame.SRCALPHA, 32)
    quadro_pergunta = quadro_pergunta.convert_alpha()
    bloco = pygame.Rect(5, 5, 900, 290)

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

        if contador == len(randon):
            print("Vc ganhou")
            s_tam = 0
            tempo = Counter.tempoCorrido()
            ranking.atualizaRanking(nomeJogador, tempo[8:], pontos)
            mus_jogo._stop()
            vitoria(1366, 768, nomeJogador, pts, Counter.tempoCorrido())

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            pygame.time.wait(500)
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

        if pontos_contaminacao < 101:  # testa se ainda tem pontos e exibe o jogo
            screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
            screen.blit(fundo_mapa, (0, 0))

            screen.blit(q_gd_pergunta, ((twidth / 2) - 563, 130))
            screen.blit(quadro_pergunta, ((twidth / 2) - 510, 150))

            screen.blit(quadro_a, (200, 300))
            screen.blit(quadro_b, (700, 300))
            screen.blit(quadro_c, (200, 350))
            screen.blit(quadro_d, (700, 350))

            screen.blit(virus, (10, 10))
            screen.blit(virus_barra, (106, 30))

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


            screen.blit(exibeTexto(Counter.tempoCorrido(), 25, amarelo, fonte_dimitri), ((twidth / 2) - 100, 10))

            screen.blit(exibeTexto("Jogador   ", 25, amarelo, fonte_dimitri), (twidth - 200, 10))
            screen.blit(exibeTexto(nomeJogador, 25, amarelo, fonte_dimitri), (twidth - 100, 10))

            pts = ("Pontos " + str(pontos))
            screen.blit(exibeTexto(pts, 25, amarelo, fonte_dimitri), (twidth - 200, 50))

            screen.blit(op_a, (120, 500))
            screen.blit(op_b, (440, 500))
            screen.blit(op_c, (740, 500))
            screen.blit(op_d, (1040, 500))

            pergunta = selecionaQuestao(randon[contador] * 7)

            #print("Memoria", int(s_tam),"Contaminação", int(pontos_contaminacao))
            quebraLinha.drawText(quadro_pergunta, pergunta[0], preto, bloco, fonte_perguntas)
            quebraLinha.drawText(quadro_a, pergunta[1], preto, bloco_a, fonte_perguntas)
            quebraLinha.drawText(quadro_b, pergunta[2], preto, bloco_b, fonte_perguntas)
            quebraLinha.drawText(quadro_c, pergunta[3], preto, bloco_c, fonte_perguntas)
            quebraLinha.drawText(quadro_d, pergunta[4], preto, bloco_d, fonte_perguntas)

            if pergunta[6] in opcoes:
                opcoes.remove(str(pergunta[6]))
            if resposta == pergunta[6]:
                certa.play()
                pygame.time.wait(500)
                print("certa resposta")
                contador += 1
                pontos += int(pergunta[5])
                jogo(1366, 768, nomeJogador, contador, pontos, pontos_contaminacao)

            if resposta in opcoes:
                errada.play()
                pygame.time.wait(500)
                print('Errada')
                contador += 1
                s_tam += 43
                pontos_contaminacao += 10

                pygame.display.update()
                jogo(1366, 768, nomeJogador, contador, pontos, pontos_contaminacao)

            resposta = ""
            #print(pontos_contaminacao)

        else:  # Apaga tudo e exibe o Game over
            s_tam = 0
            tempo = Counter.tempoCorrido()
            ranking.atualizaRanking(nomeJogador, tempo[8:], pontos)
            mus_jogo._stop()
            gameOver(1366, 768, nomeJogador, pts, Counter.tempoCorrido())

        pygame.display.update()  # Atualiza os retangulos defindos


def planMenu(twidth, theight, nomeJogador):
    global screen, event, mus_menu, fps, mus_jogo
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    #quadro ranking
    quadro_ranking = pygame.Surface((200, 290), pygame.SRCALPHA, 32)
    quadro_ranking = quadro_ranking.convert_alpha()
    bloco_ranking = pygame.Rect(5, 5, 200, 290)
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

            if 1200 > pos[0] > 800 and 450 > pos[1] > 380:  # Testa se o clique foi no indicado
                selecao.play()
                pygame.time.wait(500)
                saiMenu = False

            if 1200 > pos[0] > 800 and 560 > pos[1] > 480:  # Testa se o clique foi no indicado
                selecao.play()
                webbrowser.open('https://github.com/carloslpsouza/ITHealth')

            if 1200 > pos[0] > 800 and 680 > pos[1] > 600:  # Testa se o clique foi no indicado
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
            ranksai = str(ranknome[:-1] + "   " + rankpts[:-1] + "   " + ranktempo[:-1])
            screen.blit(exibeTexto(ranksai, 45, preto, fonte_dimitri), ((twidth / 2) - 530, 300 + mem))
            mem += 100

        pygame.display.update()  # Atualiza os retangulos defindos
    mus_menu._stop()
    mus_jogo = threading.Thread(target=musicaFundo, args=('TRILHA/suspense.mp3',))
    mus_jogo.start()
    jogo(1366, 768, nomeJogador, 0, 0, 0)


def jogador(twidth, theight):
    global screen, event, mus_menu, fps
    mus_menu = threading.Thread(target=musicaFundo, args=('TRILHA/awesomeness.wav', ))
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

    planMenu(1366, 768, nomeJogador)


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
    jogador(1366, 768)


entrada(1366,768)