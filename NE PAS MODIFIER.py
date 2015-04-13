import pygame
from pygame.locals import *

pygame.init()

#step_sound = pygame.mixer.Sound("step_sound.wav")
soundtrack = pygame.mixer.Sound("texas.wav")
zombie_sound = pygame.mixer.Sound("zombie_sound.wav")
fenetre = pygame.display.set_mode((1450, 720))


fond = pygame.image.load("SCROLL FINAL.png").convert()
position_fond = fond.get_rect()

zombie = pygame.image.load("MRZBY.png").convert_alpha()
position_zombie = zombie.get_rect()


leroux = pygame.image.load("LEROUX.png").convert_alpha()
position_leroux = leroux.get_rect()


findugame = 0
position_zombie = position_zombie.move(560,525)
position_leroux = position_leroux.move(600,525)


pygame.display.flip()

continuer = 1
while continuer:
        for event in pygame.event.get():        #Attente des événements
                if event.type == QUIT :
                        continuer = 0

                if event.type == KEYDOWN and findugame == 0 :

                         if event.key == K_p:
                                 zombie_sound.play()
                                 soundtrack.play()
                         if event.key == K_o:
                                 zombie_sound.stop()
                                 soundtrack.stop()

                         if position_fond == (-2670, 0, 9197, 720) :
                                findugame+= 1
                                position_fond = position_fond.move(-1850,0)     

                         if position_zombie == position_leroux :
                                findugame+= 1
                                position_fond = position_fond.move(-5750, 0)
                            
                        #Si "flèche droite ": On bouge le zombie et le fond
                         if event.key == K_f:
                                 position_zombie = position_zombie.move(15,0)
                     
                         if event.key == K_RIGHT:
                                 position_zombie = position_zombie.move(-15, 0)
                                 position_fond = position_fond.move(-15, 0)
                                 print(position_fond)
                                 print(position_leroux)


        #Re-collage
        fenetre.blit(fond, position_fond)
        if findugame == 0 :
                fenetre.blit(leroux, position_leroux)
                fenetre.blit(zombie, position_zombie)
        #Rafraichissement
        pygame.display.flip()
