import pygame, sys
import quebraLinha
import Counter
from pygame.locals import *

global screen

pygame.init()#inicializa todos os modulos do pygame


#Variáveis Sprites
fundo_mapa = pygame.image.load('SPRITES/fundo-mapa-verde.png')
abertura = pygame.image.load('SPRITES/logo-com-fundo.png')
menu = pygame.image.load('SPRITES/tela-inicial.png')
tela_nome = pygame.image.load('SPRITES/tela-nome.png')
q_gd_pergunta = pygame.image.load('SPRITES/quadro-grande-pergunta.png')
game_over = pygame.image.load('SPRITES/game-over.png')
op_a = pygame.image.load('SPRITES/a.png')
op_b = pygame.image.load('SPRITES/b.png')
op_c = pygame.image.load('SPRITES/c.png')
op_d = pygame.image.load('SPRITES/d.png')
#

#Fontes
fonte = pygame.font.match_font('FreeSans')#Encontra caminho absoluto fonte no SO
fonte_padrao = pygame.font.Font(fonte, 30)  # criar um objeto Font a partir das fontes do sistema SysFont (nome, tamanho, negrito = Falso, itálico = Falso)
fonte_perguntas = pygame.font.Font('FONTES/Roboto/Roboto-Light.ttf', 30)
#

#Variaveis de cores
preto = (0,0,0)
amarelo = (255,255,0)
branco = (255,255,255)
#

#Variáveis de tela
twidth = 1366
theight = 768
#

clock = pygame.time.Clock() # Cria um objeto que ajuda a controlar o tempo

def gameOver(twidth, theight, nomeJogador, pts, tempo):
    global screen
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    saiGame = True
    while saiGame:
        clock.tick(5)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            print(pos)

            if 1200 > pos[0] > 800 and 450 > pos[1] > 380:  # Testa se o clique foi no indicado
                saiGame = False
                jogo(1366, 768, nomeJogador)

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(game_over, (0, 0))
        #screen.blit(exibeTexto(nomeJogador, 25, preto), ((twidth/2), 400))
        screen.blit(exibeTexto(pts, 50, preto), ((twidth/2)-200, 370))
        screen.blit(exibeTexto(tempo, 50, preto), ((twidth/2)-200, 430))
        pygame.display.update()  # Atualiza os retangulos defindos



def musicaFundo():
    pygame.mixer.init()
    pygame.mixer.music.load('TRILHA/suspense.mp3')
    pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(1)

def exibeTexto(txt, tam_fonte, cor): #função que facilita a rederização de texto na tela é so passar o texto e o tamanho
    fonte_padrao = pygame.font.Font(fonte, tam_fonte)#criar um objeto Font a partir das fontes do sistema SysFont (nome, tamanho, negrito = Falso, itálico = Falso)
    texto_surface = fonte_padrao.render(txt, False, cor)#Renderiza o texto passado pelo parametro txt
    return texto_surface

def jogo(twidth, theight, nomeJogador):
    # Sangue
    s_ini = 180
    s_tam = 30
    sangue = [(s_ini, 15), (s_ini + s_tam, 15), (s_ini + (2 * s_tam), 15), (s_ini + (3 * s_tam), 15),
              (s_ini + (4 * s_tam), 15), (s_ini + (5 * s_tam), 15), (s_ini + (6 * s_tam), 15),
              (s_ini + (7 * s_tam), 15), (s_ini + (8 * s_tam), 15), (s_ini + (9 * s_tam), 15)]
    sangue_skin = pygame.Surface((s_tam, 20))  # representa a largura e altura de cada bloco
    sangue_skin.fill((255, 255, 0))  # cor do bloco
    #

    pontos_contaminacao = 100
    pontos = 0
    pergunta1 = "Por mais de 3 mil anos a Varíola atormentou a humanidade, existem relatos históricos que apontam vestígios do vírus no Faraó Ramsés V (Falecido em 1145 AC). Qual foi o primeiro método eficaz na imunização do Vírus?"

    musicaFundo()

    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela
    # tratamento quebra de linha
    quadro_pergunta = pygame.Surface((900, 290), pygame.SRCALPHA, 32)  # cria um quadro onde serão exibidas as perguntas
    quadro_pergunta = quadro_pergunta.convert_alpha()  # Converte a superficie quadro branco para transparente
    bloco = pygame.Rect(5, 5, 900, 290)  # Função textWrap pede como paramentro
    #

    while True:
        clock.tick(5)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            print(pos)

            if 320 > pos[0] > 150 and 600 > pos[1] > 500:  # Testa se o clique foi no indicado
                sangue.pop()
                pontos_contaminacao -= 10  # retira 10 pontos a cada erro
                print(pontos_contaminacao)

            if 640 > pos[0] > 540 and 600 > pos[1] > 500:  # Testa se o clique foi no indicado
                pontos += 5  # Soma pontos a cada acerto

        if pontos_contaminacao > 0:  # testa se ainda tem pontos e exibe o jogo
            screen.fill(
                preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
            screen.blit(fundo_mapa, (0, 0))
            screen.blit(q_gd_pergunta, ((twidth / 2) - 563, 130))
            screen.blit(quadro_pergunta, ((twidth / 2) - 510, 150))

            screen.blit(exibeTexto("Contaminação: ", 25, amarelo), (10, 10))

            for i in sangue:  # imprime na tela 10 unidades de sangue
                screen.blit(sangue_skin, i)

            screen.blit(exibeTexto(Counter.tempoCorrido(), 25, amarelo), ((twidth / 2) - 100, 10))

            screen.blit(exibeTexto("Jogador: ", 25, amarelo), (twidth - 200, 10))
            screen.blit(exibeTexto(nomeJogador, 25, amarelo), (twidth - 100, 10))

            pts = ("Pontos: " + str(pontos))
            screen.blit(exibeTexto(pts, 25, amarelo), (twidth - 200, 50))

            quebraLinha.drawText(quadro_pergunta, pergunta1, preto, bloco, fonte_perguntas)

            screen.blit(op_a, (120, 500))
            screen.blit(op_b, (440, 500))
            screen.blit(op_c, (740, 500))
            screen.blit(op_d, (1040, 500))
        else:  # Apaga tudo e exibe o Game over
            gameOver(1366,768, nomeJogador, pts, Counter.tempoCorrido())

        pygame.display.update()  # Atualiza os retangulos defindos


def planMenu(twidth, theight, nomeJogador):
    global screen
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    saiMenu = True
    while saiMenu:
        clock.tick(5)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()  # Pega a posição onde o mouse clica
            #print(pos)

            if 1200 > pos[0] > 800 and 450 > pos[1] > 380:  # Testa se o clique foi no indicado
                saiMenu = False


        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(menu, (0, 0))

        print(nomeJogador)

        pygame.display.update()  # Atualiza os retangulos defindos

    jogo(1366, 768, nomeJogador)


def jogador(twidth, theight):
    global screen
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela

    userName = ""
    saiNome = True
    while saiNome:
        clock.tick(5)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                userName += event.unicode
                nomeJogador = userName[:-1]
                if event.key == pygame.K_RETURN:
                    saiNome = False


        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(tela_nome, (0, 0))

        screen.blit(exibeTexto(userName, 50, preto), ((twidth/2)-400,(theight/2)-70))


        pygame.display.update()  # Atualiza os retangulos defindos

    planMenu(1366, 768, nomeJogador)


def entrada(twidth, theight):
    global screen
    screen = pygame.display.set_mode((twidth, theight))  # Define o tamanho da janela
    pygame.display.set_caption('QuizDemic')  # Exibe o titulo na janela
    saiEntrada = True
    while saiEntrada:
        clock.tick(5)  # Método tick() conta o tempo da ultima chamada serve para reduzir fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(preto)  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(abertura, (0, 0))
        pygame.display.update()  # Atualiza os retangulos defindos
        pygame.time.wait(1500)
        saiEntrada = False
    jogador(1366, 768)

entrada(600,600)
