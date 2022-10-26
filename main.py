from game import Game
from panier import Panier # on importe le composant panier
from oeuf import OeufChocolat # on import la classe oeuf chocolat
import pygame

from panierSecond import PanierSecond # utiliser le module pygame pour faire des jeux avec python
pygame.init() # charger les composants

# definir les dimentions
largeur = 1200
hauteur = 720

#def des fps
clock = pygame.time.Clock()

# creer la fenetre avec pygame
fenetre = pygame.display.set_mode((largeur, hauteur)) # on definit la taille
pygame.display.set_caption("Chasse aux oeufs") # on definit un titre
pygame.display.set_icon(pygame.image.load('assets/panier.png'))

#on charge
game = Game(largeur, hauteur)

# maintenir la fenetre du jeu en eveil pour pas qu'elle se ferme
running = True

# tant que la fenetre est active, on boucle des instructions à chaque fois
while running:

    if game.is_playing:
        game.update(fenetre)
    
    

    # boucler sur les evenements actif du joueur
    for evenement in pygame.event.get():
        # si l'evenement c'est la fermeture de fenetre
        if evenement.type == pygame.QUIT:
            running = False # on arrete la boucle pour que la fenetre se ferme
            quit() # on quitte le jeu
        # si l'evenement est une interaction au clavier
        elif evenement.type == pygame.KEYDOWN:
            game.touches_active[evenement.key] = True # la touche est active
        elif evenement.type == pygame.KEYUP:
            game.touches_active[evenement.key] = False # la touche est desactive

    # mettre à jour l'ecran du jeu
    clock.tick(400)
    pygame.display.flip()