
import pygame
from pygame.locals import *

pygame.init()


fenetre = pygame.display.set_mode((9197, 720))




fond = pygame.image.load("SCROLL FINAL.png").convert()
fenetre.blit(fond, (0,0))

zombie = pygame.image.load("MRZBY FINAL.png").convert()
position_zombie = zombie.get_rect()             #40,525


leroux = pygame.image.load("LEROUX FINAL.png").convert()
position_leroux = leroux.get_rect()        #170,527

zombieWin = pygame.image.load("ZOMBIEWIN.png").convert() #en attente

lerouxWin = pygame.image.load("HUMANWIN.png").convert()  #en attente

position_zombie = position_zombie.move(40,525)
position_leroux = position_leroux.move(160,525)

pygame.display.flip()

continuer = 1
while continuer:
        for event in pygame.event.get():        #Attente des événements
                if event.type == QUIT:
                        continuer = 0
                
                if event.type == KEYDOWN:
                        #Si "flèche droite ": On bouge le zombie
                        if event.key == K_f:
                                position_zombie = position_zombie.move(15,0)
                        if event.key == K_d:
                                position_zombie = position_zombie.move(0,5)
                        if event.key == K_s:
                                position_zombie = position_zombie.move(-15,0)
                        if event.key == K_e:
                                position_zombie = position_zombie.move(0,-5)


                        if event.key == K_RIGHT:
                                position_leroux = position_leroux.move(15,0)
                        if event.key == K_DOWN:
                                position_leroux = position_leroux.move(0,5)
                        if event.key == K_LEFT:
                                position_leroux = position_leroux.move(-15,0)
                        if event.key == K_UP:
                                position_leroux = position_leroux.move(0,-5)


        #Re-collage
        fenetre.blit(fond,(0,0))
        fenetre.blit(leroux, position_leroux) 
        fenetre.blit(zombie, position_zombie)
        #Rafraichissement
        pygame.display.flip()


