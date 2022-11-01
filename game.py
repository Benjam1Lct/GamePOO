import math
import pygame # importe les composants
from panier import Panier
from panierSecond import PanierSecond
from feuille import Feuille
from settings import Settings_Menu

class Game(pygame.sprite.Sprite):

    def __init__(self, largeur, hauteur):
        self.is_playing = False
        self.largeur = largeur
        self.hauteur = hauteur
        self.fond = pygame.image.load('assets/fond.jpg') # charger l'image de l'arrière plan
        self.sol = pygame.image.load('assets/sol.png') # charger l'image du sol
        self.solRound = pygame.image.load('assets/solRound.png') # charger l'image du sol

        # charger la lampe
        self.lanterne = pygame.image.load('assets/lanterne.png')
        
        # charger le bouton retour a l'ecran titre
        self.back = pygame.image.load('assets/button/button_back.png')
        self.back = pygame.transform.scale(self.back, (112, 54.58))
        self.back_rect = self.back.get_rect()
        self.back_rect.x = 0
        self.back_rect.y = 0

        # redimentionner
        self.lanterne = pygame.transform.scale(self.lanterne, (36, 50))

        # créer un dictionnaire qui va contenir en temps reel les touches enclenchées par le joueur
        self.touches_active = {}

        # créer le panier du joueur
        self.panier = Panier(largeur, hauteur)
        self.panierSecond = PanierSecond(largeur, hauteur, 'assets/SacDerriere.png')
        self.spriteDevant = PanierSecond(largeur, hauteur, 'assets/SpriteDevant.png')
        self.spriteDerriere = PanierSecond(largeur, hauteur, 'assets/SpriteDerriere.png')

        # on creer les settings
        self.settings = Settings_Menu(largeur, hauteur, self.panier)


        # créer la couleur
        self.chocolat_couleur = (146, 122, 86)

        # on import l'encoche du score
        self.score = pygame.image.load('assets/score.png')
        self.score = pygame.transform.scale(self.score, (200, 90))

        # on ecrit le score a l'ecran
          # type: ignore

        # créer un groupe qui va contenir plusieurs oeufs en chocolat
        self.feuille = pygame.sprite.Group()
    
    def start(self):
        self.is_playing = True
        self.feuille.add(Feuille(self.largeur, self.hauteur, self.panier))
        self.feuille.add(Feuille(self.largeur, self.hauteur, self.panier))
        self.feuille.add(Feuille(self.largeur, self.hauteur, self.panier))

    def end_game(self):
        self.is_playing = False
        self.panier.points = self.panier.maximum_points/2
        self.feuille = pygame.sprite.Group()

    def update(self, fenetre):
        # actualiser toutes les images qui sont sur le jeu
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(self.back, self.back_rect)

        police = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 26)
        scoreNum = math.floor(self.panier.points)
        text_score = police.render(str(scoreNum), True ,(255,255,255))

        # afficher le score en haut de l'ecran qui correspond au nombre de points
        fenetre.blit(self.score, (1003, 0))
        fenetre.blit(text_score, (1070,45))

        fenetre.blit(self.spriteDerriere.image, self.panier.rect)
        fenetre.blit(self.panierSecond.image, self.panier.rect)
        self.feuille.draw(fenetre)
        fenetre.blit(self.panier.image, self.panier.rect)
        fenetre.blit(self.spriteDevant.image, self.panier.rect)
        fenetre.blit(self.sol, (0, 0))
        
        largeur_lanterne = (self.panier.points*(self.largeur-112))/self.panier.maximum_points

        # dessiner l'arriere de la jauge
        pygame.draw.rect(fenetre, (0, 0, 0), [57, self.hauteur - 50, self.largeur - 112, 36] ) # dimension dans la fenetre

        pygame.draw.rect(fenetre, self.chocolat_couleur, [57, self.hauteur - 50, largeur_lanterne, 36] )

        # afficher le designer de la jauge de progression
        fenetre.blit(self.solRound, (0, 0))
        # afficher icon sur la jauge de progression
        fenetre.blit(self.lanterne, (largeur_lanterne + 35, 666))

        

        # recupere tout les oeufs depuis mon groupe de sprite
        for petales in self.feuille:
            petales.gravite()  # type: ignore

        # detecter quelle est la touche active par le joueur
        if self.touches_active.get(pygame.K_RIGHT): # si la touche droite est active
            self.panier.deplacement_droite()
        elif self.touches_active.get(pygame.K_LEFT): # si la touche gauche est active
            self.panier.deplacement_gauche()

