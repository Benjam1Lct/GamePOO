import random # pour faire des choses au hasard
import pygame

# créer une classe qui va representer la feuille
class Feuille(pygame.sprite.Sprite):
    """
    Objectif: creer des objet qui tombe du haut de la fenetre, une fois attrape augmente le score
    Arg: le module pygame afin de creer un groupe avec les feuille
    Return: creer trois feuille qui tombe et les font respawn en haut de l'ecran une fois qu'elle entre en colision 
            avec le joueur ou le bord de l'ecran
    """

    # definir la fonction init qui charge les caracteristiques de base de la feuille
    def __init__(self, largeur_ecran, hauteur_ecran, panier):
        super().__init__()

        # on definit la vitesse de chute initiale
        self.vitesse_chute = random.randint(1, 3)

        # on unitialise l'objet panier entre en parametre
        self.panier = panier

        # on creer un groupe panier
        self.panier_group = pygame.sprite.Group()
        # on y ajoute l'objet "panier" cree au lancement du jeu
        self.panier_group.add(self.panier)

        # on defini les dimension de l'ecran
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran

        # on import l'image de la feuille
        self.image = pygame.image.load('assets/feuille.png')
        # on redimensionne cette image
        self.image = pygame.transform.scale(self.image, (30, 30))
        # on creer un rectangle afin d'interagir avec le sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, largeur_ecran - 40)

    # teleporte les feuilles en haut de la fenetre au moment de respawn et appliquer une vitesse aleatoire de descente
    def repositionner(self):
        # reteleporter l'oeuf en haut
        self.rect.x = random.randint(40, self.largeur_ecran - 30)
        self.rect.y = - self.image.get_height()
        self.vitesse_chute = random.randint(2, 5)

    # une methode pour deplacer la feuille vers le bas en fonction du niveau de difficulte
    # la difficulte va varier grace au coefficient qui multiplie la vitesse de chute
    def gravite(self):
        if self.panier.level_setting == 0:
            self.rect.y += (self.vitesse_chute*1.2)
        elif self.panier.level_setting == 1:
            self.rect.y += (self.vitesse_chute*2)
        elif self.panier.level_setting == 2:
            self.rect.y += (self.vitesse_chute*3.5)

        # si la feuille rentre en collision avec le panier alors on reposition la feuille avec la methode "repositionner" et on ajoute un point avec la methode dans la classe "Panier"
        if pygame.sprite.spritecollide(self, self.panier_group, False, pygame.sprite.collide_mask) and self.rect.y >= 500:
            print("Collision", self.rect.y)
            self.repositionner()
            # ajouter des points
            self.panier.ajouter_points()

        # si la position en y de la feuille depasse 646 alors cela signifie que la feuille n'est plus visible donc qu'elle est sortie de l'ecran
        # donc on enlever des points et on repositionne la feuille en haut de la fenetre avec la methode "repositionner"
        if self.rect.y >= 646:
            self.repositionner()
            # enlever les points
            self.panier.enlever_points()