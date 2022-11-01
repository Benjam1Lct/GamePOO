import pygame # importe les composants

# créer une classe qui va representer le concept de joueur ou du panier sur notre jeu
class Panier(pygame.sprite.Sprite):

    # le constructeur
    def __init__(self, largeur_ecran, hauteur_ecran):
        super().__init__()
        # level 0 = easy
        # level 1 = normal
        # level 2 = hard
        self.level_setting = 1
        self.largeur_ecran = largeur_ecran
        # nombre maximum de points
        self.maximum_points = 100
        # nombre de points qu'aura le joueur
        self.points = self.maximum_points/2 
        self.image = pygame.image.load('assets/SacDevant.png') # charger l'image du panier
        self.image = pygame.transform.scale(self.image, (250, 250)) # redimentionner l'image
        self.rect = self.image.get_rect() # on lui definit un rectangle
        self.rect.x = (largeur_ecran / 2) - self.image.get_width() /2
        self.rect.y = hauteur_ecran - 335
        self.vitesse = 12 # vitesse de deplacement du panier


    def update_level(self):
        if self.level_setting == 0:
            self.maximum_points = 50
        elif self.level_setting == 1:
            self.maximum_points = 100
        elif self.level_setting == 2:
            self.maximum_points = 200
        self.points = self.maximum_points/2

    # methode pour ajouter 5 points
    def ajouter_points(self):
        if self.points < self.maximum_points: # limite de points
            self.points += 5
            print(self.points)
            print("+5 points")
        if self.points >= self.maximum_points:
            #gagne
            print('Gagner')

    # methode enlever 2 points
    def enlever_points(self):
        if self.points >= 5:
            self.points -= 5
            print(self.points)
            print("-5 points")
        elif self.points <= 0:
            # perdu
            print("Perdu")

    # methode pour le deplacement droite
    def deplacement_droite(self):
        if self.rect.x < 1000: 
            self.rect.x += self.vitesse

    # methode pour le deplacement gauche
    def deplacement_gauche(self):
        if self.rect.x > -50:
            self.rect.x -= self.vitesse
