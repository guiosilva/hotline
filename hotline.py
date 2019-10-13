import math
import pygame
from pygame.locals import *

# Iniciar o Jogo
pygame.init()
pygame.mixer.init()
width, height = 1080, 720
screen = pygame.display.set_mode((width,height))

# Trilha Sonora
music = False

def shootsnd(): #efeito de tiro
    effect = pygame.mixer.Sound('shoot.wav')
    effect.play()

def soundtrack():
    global music
    if music == False:
        pygame.mixer.music.load('soundtrack.mp3')
        pygame.mixer.music.play(-1)
        music = True

# Listas de variaveis
keys = [False, False, False, False, False]
playerpos = [508, 328]
lifepos = [474, 396]
origempos = [497,260]
bgpos = [0, 0]
shoots = []
shootsctrl = 10


# Esconder o mouse
pygame.mouse.set_visible(False)

# Carregando sprites
#player = pygame.image.load('Sprites/Player.png')
player = [pygame.image.load('Sprites/Player.png'), pygame.image.load('Sprites/Player_01.png'), pygame.image.load('Sprites/Player_02.png'), pygame.image.load('Sprites/Player_03.png'), pygame.image.load('Sprites/Player_04.png'), pygame.image.load('Sprites/Player_03.png'), pygame.image.load('Sprites/Player_02.png'), pygame.image.load('Sprites/Player_01.png'), pygame.image.load('Sprites/Player.png'), pygame.image.load('Sprites/Player_10.png'), pygame.image.load('Sprites/Player_20.png'), pygame.image.load('Sprites/Player_30.png'), pygame.image.load('Sprites/Player_40.png'), pygame.image.load('Sprites/Player_30.png'), pygame.image.load('Sprites/Player_20.png'), pygame.image.load('Sprites/Player_10.png')]
bg = pygame.image.load('Sprites/background.png')
shoot = pygame.image.load('Sprites/Shoot.png')
life = [1,2,3]
life[0] = pygame.image.load('Sprites/Life1.png')
life[1] = pygame.image.load('Sprites/Life2.png')
life[2] = pygame.image.load('Sprites/Life3.png')
enemy = [1,2]
enemy[0] = pygame.image.load('Sprites/Enemy.png')
enemy[1] = pygame.image.load('Sprites/Enemy2.png')
aim = [1,2]
aim[0] = pygame.image.load('Sprites/aim_01.png')
aim[1] = pygame.image.load('Sprites/aim_02.png')
origem = pygame.image.load('Sprites/Origem.png')
I = aim[0]

clock = pygame.time.Clock()

# Animação

# Jogo
aberto = True
while aberto:
    soundtrack()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aberto = False

    # Movimentação
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            keys[4] = True
            position = pygame.mouse.get_pos()
            shootsnd()
            shoots.append([math.atan2 (position[1] - (playerpos1[1]+64), position[0] - (playerpos1[0]+64)), playerpos1[0]*math.sin(32)+289, playerpos1[1]*math.cos(64)+282])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        if event.type == pygame.MOUSEBUTTONUP:
            keys[4] = False
    if keys[0]:
        #playerpos[1] -= 5
        #lifepos[1] -= 5
        bgpos[1] += 5

    elif keys[2]:
        #playerpos[1] += 5
        #lifepos[1] += 5
        bgpos[1] -= 5

    elif keys[1]:
        #playerpos[0] -= 5
        #lifepos[0] -= 5
        bgpos[0] += 5

    elif keys[3]:
        #playerpos[0] += 5
        #lifepos[0] += 5
        bgpos[0] -= 5


    if keys[4]:
        I = aim[1]
    if not keys[4]:
        I = aim[0]


    # Usando sprites
    screen.fill((32, 0, 0)) # Preenchimento do fundo
    screen.blit(bg, (bgpos))
    screen.blit(life[0], (lifepos))
    #screen.blit(origem, (origempos))

    # Mira
    if keys[4]:
        screen.blit(I, (pygame.mouse.get_pos()[0] - 16, pygame.mouse.get_pos()[1] - 16))
    if not keys[4]:
        screen.blit(I, (pygame.mouse.get_pos()[0] - 16, pygame.mouse.get_pos()[1] - 16))

    # Tiros

    for bullet in shoots:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] <-1080 or bullet[1] > 1080 or bullet[2] <-1080 or bullet[2] >1080:
            shoots.pop(index)
        index += 1
        for projectile in shoots:
            shoot1 = pygame.transform.rotate(shoot, 360-projectile[0]*57.29)
            screen.blit(shoot1, (projectile[1]-32 , projectile[2]-64))

    # Rotação do personagem
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1]), position[0] - (playerpos[0]))
    playerrot = pygame.transform.rotate(player[0], 360-angle*57.29)
    playerpos1 = (playerpos[0] -playerrot.get_rect() .width/2, playerpos[1] -playerrot.get_rect() .height/2)
    screen.blit(playerrot, playerpos1)



    # Atualização de frames
    clock.tick(30)
    pygame.display.flip()
    pygame.display.update()


