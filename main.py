from game import Game
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
pygame.display.set_icon(pygame.image.load('assets/feuille.png'))

#on charge
game = Game(largeur, hauteur)
start = Start_Menu(largeur, hauteur)


# maintenir la fenetre du jeu en eveil pour pas qu'elle se ferme
running = True

# tant que la fenetre est active, on boucle des instructions à chaque fois
while running:

    # partie gagner
    if game.panier.points >= game.panier.maximum_points:
        start.end_game_statut = 1
        game.end_game()
        start.end_game()
    # partie perdue
    elif game.panier.points <= 0:
        start.end_game_statut = 2
        game.end_game()
        start.end_game()
    elif game.is_playing:
        game.update(fenetre)
    elif start.is_playing:
        start.update(fenetre)
    elif game.settings.is_playing:
        game.settings.update(fenetre)
    

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
            if start.buttonPlayRect.collidepoint(evenement.pos) and start.is_playing:
                # mettre le jeu en mode "is_playing" = True
                start.is_playing = False
                game.start()
            elif start.buttonSettingsRect.collidepoint(evenement.pos) and start.is_playing:
                start.is_playing = False
                game.settings.is_playing = True
            elif game.settings.buttonCloseRect.collidepoint(evenement.pos) and game.settings.is_playing:
                game.settings.is_playing = False
                start.is_playing = True
                start.refresh()
            elif game.settings.button_easy_unselect_rect.collidepoint(evenement.pos) and game.settings.is_playing == True:
                game.panier.level_setting = 0
                game.settings.update(fenetre)
                game.panier.update_level()
                print(game.panier.level_setting)
                print(game.panier.maximum_points)
                print(game.panier.points)
            elif game.settings.button_normal_unselect_rect.collidepoint(evenement.pos) and game.settings.is_playing == True:
                game.panier.level_setting = 1
                game.settings.update(fenetre)
                game.panier.update_level()
                print(game.panier.level_setting)
                print(game.panier.maximum_points)
                print(game.panier.points)
            elif game.settings.button_hard_unselect_rect.collidepoint(evenement.pos) and game.settings.is_playing == True:
                game.panier.level_setting = 2
                game.settings.update(fenetre)
                game.panier.update_level()
                print(game.panier.level_setting)
                print(game.panier.maximum_points)
                print(game.panier.points)
            elif game.back_rect.collidepoint(evenement.pos) and game.is_playing:
                game.end_game()
                start.end_game()
                
                

    # mettre à jour l'ecran du jeu
    clock.tick(400)
    pygame.display.flip()