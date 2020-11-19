import pygame, sys;


pygame.init()
# Variáveis de tela
twidth = 1366
theight = 768
#
preto = (0,0,0)
logo = pygame.image.load('SPRITES/logo.png')
ambulancia = pygame.image.load('SPRITES/ambulancia.png')
fps = 25

clock = pygame.time.Clock()


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
        for i in range(14):
            screen.fill(preto)
            if i >= 7:
                screen.blit(logo, ((twidth / 2) - 150, (theight / 2) - 200))
            if i == 0:
                screen.blit(ambulancia, (-100, (theight / 2) - 200))
            screen.blit(ambulancia, ((100 * (i)), (theight / 2) - 200))
            pygame.time.wait(45)
            pygame.display.update()

        #saiEntrada = False
    #jogador(twidth, theight)

entrada(1366, 768)