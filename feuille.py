import random # pour faire des choses au hasard
import pygame
from panier import Panier

# créer une classe qui va representer l'oeuf en chocolat
class Feuille(pygame.sprite.Sprite):

    # definir la fonction init qui charge les caracteristiques de base de notre oeuf
    def __init__(self, largeur_ecran, hauteur_ecran, panier):
        super().__init__()
        self.vitesse_chute = random.randint(1, 3)
        self.panier = panier
        self.panier_group = pygame.sprite.Group()
        self.panier_group.add(self.panier)
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran
        self.image = pygame.image.load('assets/feuille.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, largeur_ecran - 40)

    def restart(self):
        self.rect.y = 0

    # teleporter respawn
    def repositionner(self):
        # reteleporter l'oeuf en haut
        self.rect.x = random.randint(40, self.largeur_ecran - 30)
        self.rect.y = - self.image.get_height()
        self.vitesse_chute = random.randint(2, 5)

    # une methode pour deplacer vers le bas l'oeuf, chuter
    def gravite(self):
        if self.panier.level_setting == 0:
            self.rect.y += (self.vitesse_chute*1.5)
        elif self.panier.level_setting == 1:
            self.rect.y += (self.vitesse_chute*2)
        elif self.panier.level_setting == 2:
            self.rect.y += (self.vitesse_chute*3)


        # si il touche le panier
        if pygame.sprite.spritecollide(self, self.panier_group, False, pygame.sprite.collide_mask) and self.rect.y >= 500:
            print("Collision", self.rect.y)
            self.repositionner()
            # ajouter des points
            self.panier.ajouter_points()


        # si il sort de l'ecran
        if self.rect.y >= 646:
            self.repositionner()
            # enlever les points
            self.panier.enlever_points()
