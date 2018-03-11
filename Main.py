#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((700, 700))

Couverture = pygame.image.load("/Users/TLM/Documents/Projet ISN/fond_noir.jpg").convert()
fenetre.blit(Couverture, (0,0))

Personnage1 = pygame.image.load("/Users/TLM/Documents/Projet ISN/Serpent2.png").convert_alpha()
#Chargement et collage du personnage
fenetre.blit(Personnage1, (250,250))
position_perso1 = Personnage1.get_rect()

#Rafraîchissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_UP:
                position_perso1 = position_perso1.move(0,10)

    Couverture.blit(Couverture, (0,0))	
    Couverture.blit(Personnage1, position_perso1)
    pygame.display.flip()
