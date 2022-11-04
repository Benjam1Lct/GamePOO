import pygame # importe les composants

class Settings_Menu(pygame.sprite.Sprite):
    """
    Objectif: lorsque le bouton "options" est clique, permet d'afficher une fenetre avec des bouton de parametrage
    Args: le module pygame
    Return: renvoie une page avec des element (arriere plan, titre) et trois bouton cliquable pour choisir une difficulte
    """

    def __init__(self, largeur, hauteur, panier):
        self.is_playing = False # variable qui indique si le menu des options est ouvert ou non

        # on creer un parametre dans le constructeur qui renvoie a l'objet panier creer dans la classe Game
        self.panier = panier

        # on recupere les dimension de la fenetre
        self.largeur = largeur
        self.hauteur = hauteur

        #on import l'arriere plan flou
        self.fond = pygame.image.load('assets/fond_menu.png') # charger l'image de l'arrière plan

        # on import le boutton pour fermer la fenetre des options
        self.buttonClose = pygame.image.load('assets/button/button_close.png')
        self.buttonClose = pygame.transform.scale(self.buttonClose, (60, 60))
        # on lui definie un rectangle pour pouvoir interagir avec et cliquer dessus
        self.buttonCloseRect = self.buttonClose.get_rect()
        self.buttonCloseRect.x = largeur - (self.buttonClose.get_width()+40)
        self.buttonCloseRect.y = 40

        # on import la police d'ecriture custom
        police = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 48)
        # on ecrit le titre "difficulté"
        self.title = police.render('Difficulté', True ,(255,255,255))


        # importer le sprite du bouton easy lorsqu'il n'est pas selectionne
        self.button_easy_unselect = pygame.image.load('assets/button/easy_unselect.png')
        self.button_easy_unselect = pygame.transform.scale(self.button_easy_unselect, (230, 207.25))
        # on lui definie un rectangle pour pouvoir interagir avec et cliquer dessus
        self.button_easy_unselect_rect = self.button_easy_unselect.get_rect()
        self.button_easy_unselect_rect.x = 180
        self.button_easy_unselect_rect.y = 339

        # les bouton de non-selection sont sombre
        # importer le sprite du bouton normal lorsqu'il n'est pas selectionne
        self.button_normal_unselect = pygame.image.load('assets/button/normal_unselect.png')
        self.button_normal_unselect = pygame.transform.scale(self.button_normal_unselect, (230, 207.25))
        self.button_normal_unselect_rect = self.button_normal_unselect.get_rect()
        # on lui definie un rectangle pour pouvoir interagir avec et cliquer dessus
        self.button_normal_unselect_rect.x = 501
        self.button_normal_unselect_rect.y = 339

        # importer le sprite du bouton hard lorsqu'il n'est pas selectionne
        self.button_hard_unselect = pygame.image.load('assets/button/hard_unselect.png')
        self.button_hard_unselect = pygame.transform.scale(self.button_hard_unselect, (230, 207.25))
        self.button_hard_unselect_rect = self.button_hard_unselect.get_rect()
        # on lui definie un rectangle pour pouvoir interagir avec et cliquer dessus
        self.button_hard_unselect_rect.x = 814
        self.button_hard_unselect_rect.y = 339
        

        # les bouton de selection son clair
        # importer le sprite du bouton easy lorsqu'il est selectionne
        self.button_easy_select = pygame.image.load('assets/button/easy_select.png')
        self.button_easy_select = pygame.transform.scale(self.button_easy_select, (230, 207.25))
        self.button_easy_select_rect = self.button_easy_select.get_rect()
        self.button_easy_select_rect.x = 180
        self.button_easy_select_rect.y = 339
        # importer le sprite du bouton normal lorsqu'il est selectionne
        self.button_normal_select = pygame.image.load('assets/button/normal_select.png')
        self.button_normal_select = pygame.transform.scale(self.button_normal_select, (230, 207.25))
        self.button_normal_select_rect = self.button_normal_select.get_rect()
        self.button_normal_select_rect.x = 501
        self.button_normal_select_rect.y = 339
        # importer le sprite du bouton hard lorsqu'il est selectionne
        self.button_hard_select = pygame.image.load('assets/button/hard_select.png')
        self.button_hard_select = pygame.transform.scale(self.button_hard_select, (230, 207.25))
        self.button_hard_select_rect = self.button_hard_select.get_rect()
        self.button_hard_select_rect.x = 814
        self.button_hard_select_rect.y = 339

    # methode lancer lorsque la page des parametre est 
    def update(self, fenetre):
        # on affiche l'arriere plan flou
        fenetre.blit(self.fond, (0, 0))
        # on affiche la croix en haut a droite qui permet de revenir a l'ecran d'acceuil 
        fenetre.blit(self.buttonClose, self.buttonCloseRect)
        # on affiche le titre des options
        fenetre.blit(self.title, (400,200))
        # on affiche les differents bouton des selection de difficulte
        # si le level_setting est egal a 0 alors on affiche le bouton easy en clair et les autres en sombre
        if self.panier.level_setting == 0:
            fenetre.blit(self.button_easy_select, self.button_easy_select_rect)
            fenetre.blit(self.button_normal_unselect, self.button_normal_unselect_rect)
            fenetre.blit(self.button_hard_unselect, self.button_hard_unselect_rect)
        # si le level_setting est egal a 1 alors on affiche le bouton normal en clair et les autres en sombre
        elif self.panier.level_setting == 1:
            fenetre.blit(self.button_easy_unselect, self.button_easy_unselect_rect)
            fenetre.blit(self.button_normal_select, self.button_normal_select_rect)
            fenetre.blit(self.button_hard_unselect, self.button_hard_unselect_rect)
        # si le level_setting est egal a 2 alors on affiche le bouton hard en clair et les autres en sombre
        elif self.panier.level_setting == 2:
            fenetre.blit(self.button_easy_unselect, self.button_easy_unselect_rect)
            fenetre.blit(self.button_normal_unselect, self.button_normal_unselect_rect)
            fenetre.blit(self.button_hard_select, self.button_hard_select_rect)