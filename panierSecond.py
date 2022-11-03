import pygame # importe les composants

# créer une classe qui va representer le concept de joueur ou du panier sur notre jeu
class PanierSecond(pygame.sprite.Sprite):

    # le constructeur
    def __init__(self, largeur_ecran, hauteur_ecran, image):
        super().__init__()

        # on definie la taille de l'ecran
        self.largeur_ecran = largeur_ecran
        
        # on initialise l'image de l'objet en fonction du parametre
        self.image = pygame.image.load(image) # charger l'image du panier
        self.image = pygame.transform.scale(self.image, (250, 250)) # redimentionner l'image
        # on lui definit un rectangle afin de le placer facilement
        self.rect = self.image.get_rect() 
        self.rect.x = (largeur_ecran / 2) - self.image.get_width() /2
        self.rect.y = hauteur_ecran - 335

        # vitesse de deplacement du panier
        self.vitesse = 12 

    # methode pour le deplacement droite
    def deplacement_droite(self):
        if self.rect.x + self.image.get_width() < self.largeur_ecran: 
            self.rect.x += self.vitesse

    # methode pour le deplacement gauche
    def deplacement_gauche(self):
        if self.rect.x > 0:
            self.rect.x -= self.vitesse