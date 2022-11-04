import math
import pygame # importe les composants
from panier import Panier
from panierSecond import PanierSecond
from feuille import Feuille
from settings import Settings_Menu

class Game(pygame.sprite.Sprite):
    """
    Objectif: lorsque le bouton "jouer" est cliquer, permet de creer une page de jeu active
    Args: le module pygame afin de creer le jeu
    Return: renvoie une page avec un sprite que l'on peut deplacer sur un arriere plan, affiche egalement un score qui s'actualise
            et des objet son generer et tombre de l'ecran, l'objectif etant de les attraper afin de gagner des points
    """

    def __init__(self, largeur, hauteur):
        self.is_playing = False # variable qui indique si une partie est en cour
        self.largeur = largeur
        self.hauteur = hauteur

        # on import les differents fonds du plateau de jeu
        self.fond = pygame.image.load('assets/fond.jpg') # charger l'image de l'arrière plan
        self.sol = pygame.image.load('assets/sol.png') # charger l'image du sol arriere plan
        self.solRound = pygame.image.load('assets/solRound.png') # charger l'image du sol premier plan

        # charger la lanterne qui sera placer sur la bar de progression
        self.lanterne = pygame.image.load('assets/lanterne.png')
        
        # charger le bouton "retour" en haut a gauche de l'ecran de jeu qui permet de revenir a l'ecran titre
        self.back = pygame.image.load('assets/button/button_back.png')
        self.back = pygame.transform.scale(self.back, (112, 54.58))
        # on lui definie un rectangle pour pouvoir interagir avec et cliquer dessus
        self.back_rect = self.back.get_rect()
        self.back_rect.x = 0
        self.back_rect.y = 0

        # on redimentionne la lanterne qui se trouve sur la bar de progression 
        self.lanterne = pygame.transform.scale(self.lanterne, (36, 50))

        # créer un dictionnaire qui va contenir en temps reel les touches enclenchées par le joueur
        self.touches_active = {}

        # on créer le sprite du joueur avec different element afin d'avoir des profondeurs differentes
        # on creer un objet principale qui se chargera de la colision avec la classe Panier
        # on creer des objet secondaire qui serve uniquement au design du sprite a partir de la classs PanierSecond
        self.panier = Panier(largeur, hauteur)
        self.panierSecond = PanierSecond(largeur, hauteur, 'assets/SacDerriere.png')
        self.spriteDevant = PanierSecond(largeur, hauteur, 'assets/SpriteDevant.png')
        self.spriteDerriere = PanierSecond(largeur, hauteur, 'assets/SpriteDerriere.png')

        # on creer les menu des options en utilisant la classe Settings_Menu
        self.settings = Settings_Menu(largeur, hauteur, self.panier)


        # on definie la couleur de la bar de progression
        self.couleur_progress_bar = (146, 122, 86)

        # on import l'encoche du score en haut a droite de l'ecran
        self.score = pygame.image.load('assets/score.png')
        self.score = pygame.transform.scale(self.score, (200, 90))

        # créer un groupe qui va contenir plusieurs feuilles
        self.feuille = pygame.sprite.Group()
    
    # methode executer lorsqu'on clique sur le bouton "Jouer", elle vient lancer le jeu et ajoute des feuille au groupe creer precedement
    def start(self):
        self.is_playing = True
        self.feuille.add(Feuille(self.largeur, self.hauteur, self.panier))
        self.feuille.add(Feuille(self.largeur, self.hauteur, self.panier))
        self.feuille.add(Feuille(self.largeur, self.hauteur, self.panier))

    # methode lancer a la fin d'une partie, elle stop la partie, reinitialise les points et definit a nouveau un groupe de feuille vide
    def end_game(self):
        self.is_playing = False
        self.panier.points = self.panier.maximum_points/2
        self.feuille = pygame.sprite.Group()

    # methode executer lorsqu'une partie est en cour
    def update(self, fenetre):
        # actualiser toutes les images qui sont sur le jeu
        # on place le font du jeu
        fenetre.blit(self.fond, (0, 0))
        # on place le bouton "retour" en haut a gauche qui permet de revenir a l'ecran d'acceuil
        fenetre.blit(self.back, self.back_rect)
        
        # on creer une variable "police" qui correspond a une police d'ecriture custome
        police = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 26)
        # on creer une variable scoreNum qui recupere les points du jour et arrondi le nombre a l'unite afin de supprimer la virgule
        scoreNum = math.floor(self.panier.points)
        # on creer une derniere variable qui vient ecrire le score stocke dans la varible "scoreNum" en utilisant la police d'ecriture personalise
        text_score = police.render(str(scoreNum), True ,(255,255,255))

        # afficher le score en haut de l'ecran qui correspond au nombre de points
        # on place le rectangle
        fenetre.blit(self.score, (1003, 0))
        # on place le text qui correspond au score, le texte est reecrit a chac tic ce qui permet de le modifier en temps reel sur la fenetre du jeu
        fenetre.blit(text_score, (1070,45))

        # on place le sprite du jour
        # on place l'image de l'epouvantail qui sera en arriere plan
        fenetre.blit(self.spriteDerriere.image, self.panier.rect)
        # on place l'image du panier qui sera en arriere plan
        fenetre.blit(self.panierSecond.image, self.panier.rect)
        # on fait apparaitre les feuilles dans la fenetre, elle sont positioner automatiquement en haut de l'ecran
        self.feuille.draw(fenetre)
        # on place l'image du panier en premiere plan
        fenetre.blit(self.panier.image, self.panier.rect)
        # on place l'image de l'epouvantail en premier plan
        fenetre.blit(self.spriteDevant.image, self.panier.rect)
        # on place le sol du decor en dernier, apres les feuilles afin qu'elle passe derriere pour disparaitre
        fenetre.blit(self.sol, (0, 0))
        
        # on creer une varible qui vient calculer la largeur de l'ecran en fonction du nombre de points maximum a atteindre, permet d'adapter automatiquement la bar de progression
        largeur_lanterne = (self.panier.points*(self.largeur-112))/self.panier.maximum_points

        # dessiner l'arriere de la jauge de progression
        pygame.draw.rect(fenetre, (0, 0, 0), [57, self.hauteur - 50, self.largeur - 112, 36] ) # dimension dans la fenetre

        # dessiner l'avant de la jauge de progression, il s'agit de la partie qui sera en mouvement grace a la variable precedant "largeur_lanterne"
        pygame.draw.rect(fenetre, self.couleur_progress_bar, [57, self.hauteur - 50, largeur_lanterne, 36] )

        # on place le decore du sol qui vient entourer la bar de progression
        fenetre.blit(self.solRound, (0, 0))
        # on place la lanterne au bout de la jauge de progrssion qui est en mouvement afin de rendre la lecture plus evidente
        fenetre.blit(self.lanterne, (largeur_lanterne + 35, 666))

        # on recupere tout les oeufs depuis le groupe de sprite
        for petales in self.feuille:
            # on utilise la methode de la class Feuille pour deplacer vers le bas les feuilles et verifier si 
            # elle entre en colision avec le joueur ou si elle sort de l'ecran pour la faire respawn
            petales.gravite()

        # detecter quelle est la touche active par le joueur
        # si la touche droite est active
        if self.touches_active.get(pygame.K_RIGHT):
            # dans la classe Panier, on active la methode "deplacement_droite" afin de deplacer le sprite du joueur vers la droite et cela du moment que la touche est enfonce
            self.panier.deplacement_droite()
            self.panierSecond.deplacement_droite()
        # si la touche gauche est active
        elif self.touches_active.get(pygame.K_LEFT):
            # dans la classe Panier, on active la methode "deplacement_gauche" afin de deplacer le sprite du joueur vers la gauche et cela du moment que la touche est enfonce
            self.panier.deplacement_gauche()
            self.panierSecond.deplacement_gauche()