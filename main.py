import pygame
from pygame.locals import *

pygame.init()


def menu():
        fenetre = pygame.display.set_mode((800, 600))
        fond_menu = pygame.image.load("Menu.png")
        fenetre.blit(fond_menu, (0, 0))
        pygame.display.flip()
        #son_menu = pygame.mixer.Sound("intro.wav")

        continuer = 1
        while continuer:
                for event in pygame.event.get():        #Attente des événements
                        if event.type == QUIT :
                                continuer = 0

                        #if event.type == KEYDOWN:
                                #if event.key == K_p:
                                        #son_menu.play()
                                #if event.key == K_o:
                                        #son_menu.stop()

                        if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 264 and event.pos[0] < 511 and event.pos[1] > 332 and event.pos[1] < 446:
                                #son_menu.stop()
                                main()
                        
        
        
def refresh(fenetre, fond, position_fond, zombie, zombie2, position_zombie, leroux,  position_leroux, anim, findugame):
        #Re-collage
        fenetre.blit(fond, position_fond)
        if findugame == 0 :
                fenetre.blit(leroux, position_leroux)
                if anim % 2 == 0 :
                    fenetre.blit(zombie, position_zombie)
                else :
                    fenetre.blit(zombie2, position_zombie)
        #Rafraichissement
        pygame.display.flip()
        

def main():
        soundtrack = pygame.mixer.Sound("texas.wav")
        zombie_sound = pygame.mixer.Sound("zombie_sound.wav")
        #zombiewin_sound = pygame.mixer.Sound("zombiewin.wav")
        #humanwin_sound = pygame.mixer.Sound(".wav")
        
        fenetre = pygame.display.set_mode((1450, 720))


        fond = pygame.image.load("SCROLL FINAL.png").convert()
        position_fond = fond.get_rect()

        zombie = pygame.image.load("MRZBY.png").convert_alpha()
        position_zombie = zombie.get_rect()
        zombie2 = pygame.image.load("MRZBY2.png").convert_alpha()
        


        leroux = pygame.image.load("LEROUX.png").convert_alpha()
        position_leroux = leroux.get_rect()


        findugame = 0
        position_zombie = position_zombie.move(550,525)
        position_leroux = position_leroux.move(600,525)
        d_parcourue = 0
        anim = 0


        pygame.display.flip()

        continuer = 1
        while continuer:
                for event in pygame.event.get():        #Attente des événements
                        if event.type == QUIT :
                                continuer = 0

                        if event.type == KEYDOWN and findugame == 0 :

                                # Musiques de fond
                                 if event.key == K_p:
                                         zombie_sound.play()
                                         soundtrack.play()
                                 if event.key == K_o:
                                         zombie_sound.stop()
                                         soundtrack.stop()
                                #Si "flèche droite ": On bouge le zombie et le fond

                                 if event.key == K_f:
                                                 position_zombie = position_zombie.move(30,0)
                                                 anim += 1

                                 if event.key == K_RIGHT:
                                                 position_zombie = position_zombie.move(-20,0)
                                                 position_fond = position_fond.move(-20,0)
                                                 d_parcourue += 20
                                                 #print(position_fond)
                                                 #print(position_leroux)

                                # Gestion de Fin
                                 if position_fond == (-2660, 0, 9197, 720) :
                                        findugame+= 1
                                        position_fond = position_fond.move(-1850,0)
                                        zombie_sound.stop()
                                        soundtrack.stop()
                                        #humanwin_sound.play()


                                 if position_zombie == position_leroux  :
                                        findugame+= 1
                                        position_fond = position_fond.move(-5800 + d_parcourue, 0)
                                        zombie_sound.stop()
                                        soundtrack.stop()
                                        #zombiewin_sound.play()


                                 if event.key == K_f:
                                                 position_zombie = position_zombie.move(-10,0)
                                
                refresh(fenetre, fond, position_fond, zombie, zombie2, position_zombie, leroux,  position_leroux, anim, findugame)

menu()

