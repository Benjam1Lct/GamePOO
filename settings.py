import pygame # importe les composants

class Settings_Menu(pygame.sprite.Sprite):

    def __init__(self, largeur, hauteur, panier):
        self.is_playing = False
        self.panier = panier
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

        # titre "difficulty"
        police = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 48)
        self.title = police.render('Difficulty', True ,(255,255,255))

        #importer le bouton easy unselect
        self.button_easy_unselect = pygame.image.load('assets/button/easy_unselect.png')
        self.button_easy_unselect = pygame.transform.scale(self.button_easy_unselect, (230, 207.25))
        self.button_easy_unselect_rect = self.button_easy_unselect.get_rect()
        self.button_easy_unselect_rect.x = 180
        self.button_easy_unselect_rect.y = 339
        #importer le bouton normal unselect
        self.button_normal_unselect = pygame.image.load('assets/button/normal_unselect.png')
        self.button_normal_unselect = pygame.transform.scale(self.button_normal_unselect, (230, 207.25))
        self.button_normal_unselect_rect = self.button_normal_unselect.get_rect()
        self.button_normal_unselect_rect.x = 501
        self.button_normal_unselect_rect.y = 339
        #importer le bouton hard unselect
        self.button_hard_unselect = pygame.image.load('assets/button/hard_unselect.png')
        self.button_hard_unselect = pygame.transform.scale(self.button_hard_unselect, (230, 207.25))
        self.button_hard_unselect_rect = self.button_hard_unselect.get_rect()
        self.button_hard_unselect_rect.x = 814
        self.button_hard_unselect_rect.y = 339
        
        #importer le bouton easy select
        self.button_easy_select = pygame.image.load('assets/button/easy_select.png')
        self.button_easy_select = pygame.transform.scale(self.button_easy_select, (230, 207.25))
        self.button_easy_select_rect = self.button_easy_select.get_rect()
        self.button_easy_select_rect.x = 180
        self.button_easy_select_rect.y = 339
        #importer le bouton normal select
        self.button_normal_select = pygame.image.load('assets/button/normal_select.png')
        self.button_normal_select = pygame.transform.scale(self.button_normal_select, (230, 207.25))
        self.button_normal_select_rect = self.button_normal_select.get_rect()
        self.button_normal_select_rect.x = 501
        self.button_normal_select_rect.y = 339
        #importer le bouton hard select
        self.button_hard_select = pygame.image.load('assets/button/hard_select.png')
        self.button_hard_select = pygame.transform.scale(self.button_hard_select, (230, 207.25))
        self.button_hard_select_rect = self.button_hard_select.get_rect()
        self.button_hard_select_rect.x = 814
        self.button_hard_select_rect.y = 339


    def update(self, fenetre):
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(self.buttonClose, self.buttonCloseRect)
        fenetre.blit(self.title, (400,200))
        if self.panier.level_setting == 0:
            fenetre.blit(self.button_easy_select, self.button_easy_select_rect)
            fenetre.blit(self.button_normal_unselect, self.button_normal_unselect_rect)
            fenetre.blit(self.button_hard_unselect, self.button_hard_unselect_rect)
        elif self.panier.level_setting == 1:
            fenetre.blit(self.button_easy_unselect, self.button_easy_unselect_rect)
            fenetre.blit(self.button_normal_select, self.button_normal_select_rect)
            fenetre.blit(self.button_hard_unselect, self.button_hard_unselect_rect)
        elif self.panier.level_setting == 2:
            fenetre.blit(self.button_easy_unselect, self.button_easy_unselect_rect)
            fenetre.blit(self.button_normal_unselect, self.button_normal_unselect_rect)
            fenetre.blit(self.button_hard_select, self.button_hard_select_rect)

        