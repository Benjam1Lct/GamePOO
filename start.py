import pygame # importe les composants

class Start_Menu(pygame.sprite.Sprite):

    def __init__(self, largeur, hauteur):
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
        #on ajoute le batton du menu start
        self.buttonPic = pygame.image.load('assets/button_pic.png')
        self.buttonPic = pygame.transform.scale(self.buttonPic, (500, 800))
        self.buttonPicRect = self.buttonPic.get_rect() # on lui definit un rectangle
        self.buttonPicRect.x = 0
        self.buttonPicRect.y = self.hauteur/9
        #on le boutton 'jouer'
        self.buttonPlay = pygame.image.load('assets/button_start.png')
        self.buttonPlay = pygame.transform.scale(self.buttonPlay, (273, 110))
        self.buttonPlayRect = self.buttonPlay.get_rect() # on lui definit un rectangle
        self.buttonPlayRect.x = (self.largeur / 5.12) - self.buttonPlay.get_width() /3
        self.buttonPlayRect.y = self.hauteur/2.15
        #on le boutton 'settings'
        self.buttonSettings = pygame.image.load('assets/button_settings.png')
        self.buttonSettings = pygame.transform.scale(self.buttonSettings, (273, 110))
        self.buttonSettingsRect = self.buttonSettings.get_rect() # on lui definit un rectangle
        self.buttonSettingsRect.x = (self.largeur / 7.12) - self.buttonSettings.get_width() /3
        self.buttonSettingsRect.y = self.hauteur/5

    def end_game(self):
        self.is_playing = True

    def update(self, fenetre):
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(self.title, self.titleRect)
        fenetre.blit(self.buttonPic, self.buttonPicRect)
        fenetre.blit(self.buttonPlay, self.buttonPlayRect)
        fenetre.blit(self.buttonSettings, self.buttonSettingsRect)