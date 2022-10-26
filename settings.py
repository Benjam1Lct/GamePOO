import pygame # importe les composants

class Settings_Menu(pygame.sprite.Sprite):

    def __init__(self, largeur, hauteur):
        self.is_playing = False
        self.largeur = largeur
        self.hauteur = hauteur
        #on import le fond floute
        self.fond = pygame.image.load('assets/fond_menu.png') # charger l'image de l'arrière plan
        #on import le boutton pour fermer la fenetre des options
        self.buttonClose = pygame.image.load('assets/button_close.png')
        self.buttonClose = pygame.transform.scale(self.buttonClose, (60, 60))
        self.buttonCloseRect = self.buttonClose.get_rect()
        self.buttonCloseRect.x = largeur - (self.buttonClose.get_width()+40)
        self.buttonCloseRect.y = 40

    def update(self, fenetre):
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(self.buttonClose, self.buttonCloseRect)