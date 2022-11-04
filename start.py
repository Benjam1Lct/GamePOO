import pygame # importe les composants

class Start_Menu(pygame.sprite.Sprite):
    """
    Objectif: au demarrage du jeu affiche un ecran d'accueil avec le titre du jeu et des boutons afin de lancer une partie ou de parametrer la difficulte
    Args: le module pygame
    Return: renvoie une une fenetre avec des element (arriere plan, bouton) dont l'interaction est possible
    """

    def __init__(self, largeur, hauteur):
        self.end_game_statut = 0 # variable permetant de savoir quel ecran de fin afficher en fonction du resultat
        self.is_playing = True # variable qui definit si l'ecran de titre est affiche
        self.largeur = largeur
        self.hauteur = hauteur

        #on import le fond flou
        self.fond = pygame.image.load('assets/fond_menu.png') # charger l'image de l'arrière plan
        
        #on ajoute le titre du jeu
        self.title = pygame.image.load('assets/titre_menu.png')
        self.title = pygame.transform.scale(self.title, (500, 500))
        # on lui definit un rectangle
        self.titleRect = self.title.get_rect() 
        self.titleRect.x = (self.largeur / 3) + self.title.get_width() /3
        self.titleRect.y = self.hauteur /6
        
        # on import le titre pour l'ecran d'acceuil si la partie precedente est Gagne
        self.end_game_title_win = pygame.image.load('assets/win_menu.png')
        self.end_game_title_win = pygame.transform.scale(self.end_game_title_win, (525, 667))
        self.end_game_title_win_rect = self.end_game_title_win.get_rect() # on lui definit un rectangle
        self.end_game_title_win_rect.x = (self.largeur - self.end_game_title_win.get_width()) + 12
        self.end_game_title_win_rect.y = 30
        
        # on import le titre pour l'ecran d'acceuil si la partie precedente est Perdu
        self.end_game_title_lose = pygame.image.load('assets/lose_menu.png')
        self.end_game_title_lose = pygame.transform.scale(self.end_game_title_lose, (525, 667))
        self.end_game_title_lose_rect = self.end_game_title_lose.get_rect() # on lui definit un rectangle
        self.end_game_title_lose_rect.x = (self.largeur - self.end_game_title_win.get_width()) + 13
        self.end_game_title_lose_rect.y = 30
        
        #on affiche le sprite pour fixer les boutons de l'ecran d'acceuil
        self.buttonPic = pygame.image.load('assets/button_pic.png')
        self.buttonPic = pygame.transform.scale(self.buttonPic, (500, 800))
        # on lui definit un rectangle
        self.buttonPicRect = self.buttonPic.get_rect() 
        self.buttonPicRect.x = 0
        self.buttonPicRect.y = self.hauteur/9
        
        #on ajoute le boutton 'jouer' qui permet de lancer une partie
        self.buttonPlay = pygame.image.load('assets/button/button_start.png')
        self.buttonPlay = pygame.transform.scale(self.buttonPlay, (273, 110))
        # on lui definit un rectangle, il permettra d'interagir avec pour cliquer dessus
        self.buttonPlayRect = self.buttonPlay.get_rect()
        self.buttonPlayRect.x = (self.largeur / 5.12) - self.buttonPlay.get_width() /3
        self.buttonPlayRect.y = self.hauteur/2.15
        
        #on ajoute le bouton qui permet d'ouvrir le menu des options ou son les differentes difficulte
        self.buttonSettings = pygame.image.load('assets/button/button_settings.png')
        self.buttonSettings = pygame.transform.scale(self.buttonSettings, (273, 110))
        # on lui definit un rectangle, il permettra d'interagir avec pour cliquer dessus
        self.buttonSettingsRect = self.buttonSettings.get_rect()
        self.buttonSettingsRect.x = (self.largeur / 7.12) - self.buttonSettings.get_width() /3
        self.buttonSettingsRect.y = self.hauteur/5

    # methode executer a la fin d'une partie qui permet d'afficher l'ecran titre
    def end_game(self):
        self.is_playing = True
    
    # methode qui une fois executer permet de re-afficher le titre du jeu sur l'ecran d'acceuil
    def refresh(self):
        self.end_game_statut = 0

    def update(self, fenetre):
        # afficher le fond flou de l'ecran d'acceuil
        fenetre.blit(self.fond, (0, 0))
        # afficher un titre en fonction du statut de la variable: "self.end_game_statut"
        # si la variable est a 0 (jeu pas encore lancer ou variable refresh avec la methode correspondante) on affiche le nom du jeu
        if self.end_game_statut == 0:
            fenetre.blit(self.title, self.titleRect)
        # sinon si la variable est egale a 1 la partie precedente a etait gagne donc on affiche le titre qui indique au joueur qu'il a remporte la partie
        elif self.end_game_statut == 1:
            fenetre.blit(self.end_game_title_win, self.end_game_title_win_rect)
        # sinon si la variable est egale a 2 la partie precedente a etait perdue on affiche le titre qui indique au jouer qu'il a perdu la partie  
        elif self.end_game_statut == 2:
            fenetre.blit(self.end_game_title_lose, self.end_game_title_lose_rect)
        # on affiche les sprite de design de l'ecran d'acceuil
        # sprite correspondant au batton du panneau avec les bouton 
        fenetre.blit(self.buttonPic, self.buttonPicRect)
        # sprite du bouton "jouer" permetant de lancer une partie
        fenetre.blit(self.buttonPlay, self.buttonPlayRect)
        # sprite du bouton "options" permetant d'ouvrir le menu des options
        fenetre.blit(self.buttonSettings, self.buttonSettingsRect)