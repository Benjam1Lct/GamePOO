import pygame # importe les composants


# créer une classe qui va representer le concept de joueur ou du panier sur notre jeu
class PanierSecond(pygame.sprite.Sprite):

    # le constructeur
    def __init__(self, largeur_ecran, hauteur_ecran):
        super().__init__()
        self.largeur_ecran = largeur_ecran
        self.maximum_points = 200 # nombre maximum de points
        self.points = self.maximum_points/2 # nombre de points qu'aura le joueur
        if self.points == 0:
            self.positionLife = 0
        else:
            self.positionLife = 1 + ((self.points*4.8)/self.maximum_points) #position du logo de vie sur la jauge
        self.image = pygame.image.load('assets/panierfond.png') # charger l'image du panier
        self.image = pygame.transform.scale(self.image, (100, 100)) # redimentionner l'image
        self.rect = self.image.get_rect() # on lui definit un rectangle
        self.rect.x = (largeur_ecran / 2) - self.image.get_width() /2
        self.rect.y = hauteur_ecran - 200
        self.vitesse = 20 # vitesse de deplacement du panier

    # methode pour le deplacement droite
    def deplacement_droite(self):
        if self.rect.x + self.image.get_width() < self.largeur_ecran: 
            self.rect.x += self.vitesse

    # methode pour le deplacement gauche
    def deplacement_gauche(self):
        if self.rect.x > 0:
            self.rect.x -= self.vitesse
