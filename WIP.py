



import pygame
from pygame.locals import *

pygame.init()


fenetre = pygame.display.set_mode((1600, 720))


fond = pygame.image.load("SCROLL FINAL.png").convert()
position_fond = fond.get_rect()

zombie = pygame.image.load("MRZBY FINAL.png").convert()
position_zombie = zombie.get_rect()


leroux = pygame.image.load("LEROUX FINAL.png").convert()
position_leroux = leroux.get_rect()

zombieWin = pygame.image.load("ZOMBIEWIN.png").convert() #en attente

lerouxWin = pygame.image.load("HUMANWIN.png").convert()  #en attente

position_zombie = position_zombie.move(500,525)
position_leroux = position_leroux.move(600,525)

pygame.display.flip()

continuer = 1
while continuer:
        for event in pygame.event.get():        #Attente des événements
                if event.type == QUIT:
                        continuer = 0
                
                if event.type == KEYDOWN:
                        #Si "flèche droite ": On bouge le zombie
                        if event.key == K_f:
                                position_zombie = position_zombie.move(18,0)
                        if event.key == K_d:
                                position_zombie = position_zombie.move(0,5)
                        if event.key == K_s:
                                position_zombie = position_zombie.move(-15,0)
                        if event.key == K_e:
                                position_zombie = position_zombie.move(0,-5)


                        if event.key == K_RIGHT:
                                position_zombie = position_zombie.move(-15,0)
                                position_fond = position_fond.move(-15,0)
                        if event.key == K_DOWN:
                                position_leroux = position_leroux.move(0,5)
                        if event.key == K_LEFT:
                                position_leroux = position_leroux.move(-15,0)
                        if event.key == K_UP:
                                position_leroux = position_leroux.move(0,-5)


        #Re-collage
        fenetre.blit(fond, position_fond)
        fenetre.blit(leroux, position_leroux)
        fenetre.blit(zombie, position_zombie)
        #Rafraichissement
        pygame.display.flip()

