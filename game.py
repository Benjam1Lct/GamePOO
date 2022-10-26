import pygame # importe les composants
from panier import Panier
from panierSecond import PanierSecond
from oeuf import OeufChocolat

class Game(pygame.sprite.Sprite):

    def __init__(self, largeur, hauteur):
        self.is_playing = False
        self.largeur = largeur
        self.hauteur = hauteur
        self.fond = pygame.image.load('assets/fond.jpg') # charger l'image de l'arrière plan
        self.sol = pygame.image.load('assets/sol.png') # charger l'image du sol
        self.solRound = pygame.image.load('assets/solRound.png') # charger l'image du sol

        # charger la barre de chocolat
        self.bar_chocolat = pygame.image.load('assets/chocolate.png')

        # redimentionner
        self.bar_chocolat = pygame.transform.scale(self.bar_chocolat, (50, 50))

        # créer un dictionnaire qui va contenir en temps reel les touches enclenchées par le joueur
        self.touches_active = {}

        # créer le panier du joueur
        self.panier = Panier(largeur, hauteur)
        self.panierSecond = PanierSecond(largeur, hauteur, 'assets/SacDerriere.png')
        self.spriteDevant = PanierSecond(largeur, hauteur, 'assets/SpriteDevant.png')
        self.spriteDerriere = PanierSecond(largeur, hauteur, 'assets/SpriteDerriere.png')


        # créer la couleur
        self.chocolat_couleur = (146, 122, 86)

        # créer un groupe qui va contenir plusieurs oeufs en chocolat
        self.oeufs = pygame.sprite.Group()
        self.oeufs.add(OeufChocolat(largeur, hauteur, self.panier))
        self.oeufs.add(OeufChocolat(largeur, hauteur, self.panier))
        self.oeufs.add(OeufChocolat(largeur, hauteur, self.panier))

    def end_game(self):
        self.is_playing = False
        self.panier.points = self.panier.maximum_points/2

    def update(self, fenetre):
        # actualiser toutes les images qui sont sur le jeu
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(self.spriteDerriere.image, self.panier.rect)
        fenetre.blit(self.panierSecond.image, self.panier.rect)
        self.oeufs.draw(fenetre)
        fenetre.blit(self.panier.image, self.panier.rect)
        fenetre.blit(self.spriteDevant.image, self.panier.rect)
        fenetre.blit(self.sol, (0, 0))
        
        largeur_chocolat = (self.panier.points*1170)/self.panier.maximum_points

        # dessiner l'arriere de la jauge
        pygame.draw.rect(fenetre, (10, 15, 10), [10, self.hauteur - 45, self.largeur - 20, 32] )
        pygame.draw.rect(fenetre, self.chocolat_couleur, [10, self.hauteur - 45, largeur_chocolat, 32] )

        fenetre.blit(self.solRound, (0, 0))

        # on place la bar de chocolat
        fenetre.blit(self.bar_chocolat, (largeur_chocolat - (-5+(5*self.panier.positionLife)), 666))
       
        # recupere tout les oeufs depuis mon groupe de sprite
        for oeuf in self.oeufs:
            oeuf.gravite()

        # detecter quelle est la touche active par le joueur
        if self.touches_active.get(pygame.K_RIGHT): # si la touche droite est active
            self.panier.deplacement_droite()
        elif self.touches_active.get(pygame.K_LEFT): # si la touche gauche est active
            self.panier.deplacement_gauche()

