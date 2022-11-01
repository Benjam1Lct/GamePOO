import pygame # importe les composants

class Start_Menu(pygame.sprite.Sprite):

    def __init__(self, largeur, hauteur):
        self.end_game_statut = 0
        self.is_playing = True
        self.largeur = largeur
        self.hauteur = hauteur

        #on import le fond floute
        self.fond = pygame.image.load('assets/fond_menu.png') # charger l'image de l'arrière plan
        
        #on ajoute le titre du jeu
        self.title = pygame.image.load('assets/titre_menu.png')
        self.title = pygame.transform.scale(self.title, (500, 500))
        self.titleRect = self.title.get_rect() # on lui definit un rectangle
        self.titleRect.x = (self.largeur / 3) + self.title.get_width() /3
        self.titleRect.y = self.hauteur /6
        
        # on import le titre si la partie precedente est Win
        self.end_game_title_win = pygame.image.load('assets/win_menu.png')
        self.end_game_title_win = pygame.transform.scale(self.end_game_title_win, (525, 667))
        self.end_game_title_win_rect = self.end_game_title_win.get_rect() # on lui definit un rectangle
        self.end_game_title_win_rect.x = (self.largeur - self.end_game_title_win.get_width()) + 12
        self.end_game_title_win_rect.y = 30
        
        # on import le titre si la partie precedente est Lose
        self.end_game_title_lose = pygame.image.load('assets/lose_menu.png')
        self.end_game_title_lose = pygame.transform.scale(self.end_game_title_lose, (525, 667))
        self.end_game_title_lose_rect = self.end_game_title_lose.get_rect() # on lui definit un rectangle
        self.end_game_title_lose_rect.x = (self.largeur - self.end_game_title_win.get_width()) + 13
        self.end_game_title_lose_rect.y = 30
        
        #on ajoute le batton du menu start
        self.buttonPic = pygame.image.load('assets/button_pic.png')
        self.buttonPic = pygame.transform.scale(self.buttonPic, (500, 800))
        self.buttonPicRect = self.buttonPic.get_rect() # on lui definit un rectangle
        self.buttonPicRect.x = 0
        self.buttonPicRect.y = self.hauteur/9
        
        #on le boutton 'jouer'
        self.buttonPlay = pygame.image.load('assets/button/button_start.png')
        self.buttonPlay = pygame.transform.scale(self.buttonPlay, (273, 110))
        self.buttonPlayRect = self.buttonPlay.get_rect() # on lui definit un rectangle
        self.buttonPlayRect.x = (self.largeur / 5.12) - self.buttonPlay.get_width() /3
        self.buttonPlayRect.y = self.hauteur/2.15
        
        #on le boutton 'settings'
        self.buttonSettings = pygame.image.load('assets/button/button_settings.png')
        self.buttonSettings = pygame.transform.scale(self.buttonSettings, (273, 110))
        self.buttonSettingsRect = self.buttonSettings.get_rect() # on lui definit un rectangle
        self.buttonSettingsRect.x = (self.largeur / 7.12) - self.buttonSettings.get_width() /3
        self.buttonSettingsRect.y = self.hauteur/5

    def end_game(self):
        self.is_playing = True
    
    def refresh(self):
        self.end_game_statut = 0

    def update(self, fenetre):
        fenetre.blit(self.fond, (0, 0))
        if self.end_game_statut == 0:
            fenetre.blit(self.title, self.titleRect)
        elif self.end_game_statut == 1:
            fenetre.blit(self.end_game_title_win, self.end_game_title_win_rect)
        elif self.end_game_statut == 2:
            fenetre.blit(self.end_game_title_lose, self.end_game_title_lose_rect)
        fenetre.blit(self.buttonPic, self.buttonPicRect)
        fenetre.blit(self.buttonPlay, self.buttonPlayRect)
        fenetre.blit(self.buttonSettings, self.buttonSettingsRect)