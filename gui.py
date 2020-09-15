import pygame
from pygame.locals import *

pygame.init()#inicializa todos os modulos do pygame

screen = pygame.display.set_mode((600,600))#Define o tamanho da janela
pygame.display.set_caption('SchoolDemic')#Exibe o titulo na janela

fonte = pygame.font.match_font('Arial')#Encontra caminho absoluto fonte no SO

def exibeTexto(txt, tam_fonte): #função que facilita a rederização de texto na tela é so passar o texto e o tamanho
    fonte_padrao = pygame.font.Font(fonte, tam_fonte)#criar um objeto Font a partir das fontes do sistema SysFont (nome, tamanho, negrito = Falso, itálico = Falso)
    texto_surface = fonte_padrao.render(txt, False, (255,255,0))#Renderiza o texto passado pelo parametro txt
    return texto_surface

sangue = [(120, 15), (140, 15), (160,15), (180, 15), (200, 15), (220, 15), (240, 15), (260, 15), (280, 15), (300, 15)]
sangue_skin = pygame.Surface((20,20)) # representa a largura e altura de cada bloco
sangue_skin.fill((255,255,0)) # cor do bloco
pontos_contaminacao = 100
pontos = 0

#ret = pygame.rect(10,80, 25 ,25) #Cria retangulo para clicar

clock = pygame.time.Clock() # Cria um objeto que ajuda a controlar o tempo

while True:
    clock.tick(5)#Método tick() conta o tempo da ultima chamada serve para reduzir fps
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))#apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)

    if event.type == MOUSEBUTTONDOWN:#Pega o evento de clique no botão
            pos = pygame.mouse.get_pos()#Pega a posição onde o mouse clica
            print(pos)

            if 360 > pos[0] > 200 and 220 > pos[1] > 200:#Testa se o clique foi no indicado
                try: #Tenta remover um indice do array sangue
                    sangue.pop()
                    pontos_contaminacao -= 10 #retira 10 pontos a cada erro
                except:
                    print("Perdeu")#Exibe no console que perdeu

            if 360 > pos[0] > 200 and 270 > pos[1] > 240:#Testa se o clique foi no indicado
                try: #Tenta remover um indice do array sangue
                    pontos += 5 #Soma pontos a cada acerto
                except:
                    print("tst")  # Exibe no console

    if pontos_contaminacao > 0:#testa se ainda tem pontos e exibe o jogo
        screen.blit(exibeTexto("Sangue: ", 25), (10, 10))
        screen.blit(exibeTexto("Pontos: ", 25), (380, 10))
        screen.blit(exibeTexto(str(pontos), 25), (480, 10))
        screen.blit(exibeTexto("PERGUNTA", 25), (220, 100))
        screen.blit(exibeTexto("RESPOSTA 01", 25), (200, 200))
        screen.blit(exibeTexto("RESPOSTA 02", 25), (200, 250))
    else:#Apaga tudo e exibe o Game over
        screen.blit(exibeTexto("GAME OVER!", 50), (125, 280))


    for i in sangue: #imprime na tela 10 unidades de sangue
        screen.blit(sangue_skin, i)

    pygame.display.update()#Atualiza os retangulos defindos