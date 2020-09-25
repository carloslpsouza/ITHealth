import pygame
from pygame.locals import *

pygame.init()#inicializa todos os modulos do pygame

screen = pygame.display.set_mode((1366,768))#Define o tamanho da janela
pygame.display.set_caption('QuizDemic')#Exibe o titulo na janela

fonte = pygame.font.match_font('Arial')#Encontra caminho absoluto fonte no SO
fundo_mapa = pygame.image.load('SPRITES/fundo-mapa-verde.png')
q_gd_pergunta = pygame.image.load('SPRITES/quadro-grande-pergunta.png')

preto = (0,0,0)
amarelo = (255,255,0)

pergunta1 = "Por mais de 3 mil anos a Varíola atormentou a humanidade, existem relatos..."

def exibeTexto(txt, tam_fonte, cor): #função que facilita a rederização de texto na tela é so passar o texto e o tamanho
    fonte_padrao = pygame.font.Font(fonte, tam_fonte)#criar um objeto Font a partir das fontes do sistema SysFont (nome, tamanho, negrito = Falso, itálico = Falso)
    texto_surface = fonte_padrao.render(txt, False, cor)#Renderiza o texto passado pelo parametro txt
    return texto_surface

sangue = [(120, 15), (140, 15), (160,15), (180, 15), (200, 15), (220, 15), (240, 15), (260, 15), (280, 15), (300, 15)]
sangue_skin = pygame.Surface((1000,20)) # representa a largura e altura de cada bloco
sangue_skin.fill((255,255,0)) # cor do bloco
pontos_contaminacao = 100
pontos = 0

#ret = pygame.rect(10,80, 25 ,25) #Cria retangulo para clicar

clock = pygame.time.Clock() # Cria um objeto que ajuda a controlar o tempo

pygame.mixer.init()
pygame.mixer.music.load('TRILHA/suspense.mp3')
pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(1)

while True:
    clock.tick(5)#Método tick() conta o tempo da ultima chamada serve para reduzir fps
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))#apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)

    if event.type == MOUSEBUTTONDOWN:#Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()#Pega a posição onde o mouse clica
            print(pos)

            if 316 > pos[0] > 150 and 530 > pos[1] > 500:#Testa se o clique foi no indicado
                try: #Tenta remover um indice do array sangue
                    sangue.pop()
                    pontos_contaminacao -= 10 #retira 10 pontos a cada erro
                except:
                    print("Perdeu")#Exibe no console que perdeu

            if 320 > pos[0] > 150 and 630 > pos[1] > 600:#Testa se o clique foi no indicado
                try: #Tenta remover um indice do array sangue
                    pontos += 5 #Soma pontos a cada acerto
                except:
                    print("tst")  # Exibe no console

    if pontos_contaminacao > 0:#testa se ainda tem pontos e exibe o jogo

        screen.blit(fundo_mapa,(0,0))
        screen.blit(q_gd_pergunta, (100, 100))

        screen.blit(exibeTexto("Sangue: ", 25, amarelo), (10, 10))
        screen.blit(exibeTexto("Pontos: ", 25, amarelo), (1000, 50))
        screen.blit(exibeTexto(str(pontos), 25, amarelo), (1200, 50))
        screen.blit(exibeTexto(pergunta1, 25, preto), (200, 120))
        screen.blit(exibeTexto("RESPOSTA 01", 25, amarelo), (150, 500))
        screen.blit(exibeTexto("RESPOSTA 02", 25, amarelo), (150, 600))
    else:#Apaga tudo e exibe o Game over
        screen.blit(exibeTexto("GAME OVER!", 50, amarelo), (125, 280))


    for i in sangue: #imprime na tela 10 unidades de sangue
        screen.blit(sangue_skin, i)

    pygame.display.update()#Atualiza os retangulos defindos

