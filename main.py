from game import Game
from settings import Settings_Menu # on import la classe oeuf chocolat
from start import Start_Menu
import pygame
pygame.init() # charger les composants
# definir les dimentions
largeur = 1200
hauteur = 720

#def des fps
clock = pygame.time.Clock()

# creer la fenetre avec pygame
fenetre = pygame.display.set_mode((largeur, hauteur)) # on definit la taille
pygame.display.set_caption("Drop & Collect") # on definit un titre
pygame.display.set_icon(pygame.image.load('assets/oeuf.png'))

#on charge
game = Game(largeur, hauteur)
start = Start_Menu(largeur, hauteur)
settings = Settings_Menu(largeur, hauteur)

# maintenir la fenetre du jeu en eveil pour pas qu'elle se ferme
running = True

# tant que la fenetre est active, on boucle des instructions à chaque fois
while running:

    # partie gagner
    if game.panier.points >= game.panier.maximum_points:
        game.end_game()
        start.end_game()
    # partie perdue
    elif game.panier.points <= 0:
        pass
    elif game.is_playing:
        game.update(fenetre)
    elif start.is_playing:
        start.update(fenetre)
    elif settings.is_playing:
        settings.update(fenetre)
    

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
        # verification si la souris est en collision avec le bouton 'Jouer'
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            if start.buttonPlayRect.collidepoint(evenement.pos):
                # mettre le jeu en mode "is_playing" = True
                start.is_playing = False
                game.is_playing = True
            elif start.buttonSettingsRect.collidepoint(evenement.pos):
                start.is_playing = False
                settings.is_playing = True
            elif settings.buttonCloseRect.collidepoint(evenement.pos):
                settings.is_playing = True
                start.is_playing = True


    # mettre à jour l'ecran du jeu
    clock.tick(400)
    pygame.display.flip()