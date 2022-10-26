import pygame # importe les composants

# créer une classe qui va representer le concept de joueur ou du panier sur notre jeu
class Panier(pygame.sprite.Sprite):

    # le constructeur
    def __init__(self, largeur_ecran, hauteur_ecran):
        super().__init__()
        self.largeur_ecran = largeur_ecran
        self.maximum_points = 10 # nombre maximum de points
        self.points = self.maximum_points/2 # nombre de points qu'aura le joueur
        if self.points == 0:
            self.positionLife = 0
        else:
            self.positionLife = 1 + ((self.points*4.8)/self.maximum_points) #position du logo de vie sur la jauge
        self.image = pygame.image.load('assets/SacDevant.png') # charger l'image du panier
        self.image = pygame.transform.scale(self.image, (250, 250)) # redimentionner l'image
        self.rect = self.image.get_rect() # on lui definit un rectangle
        self.rect.x = (largeur_ecran / 2) - self.image.get_width() /2
        self.rect.y = hauteur_ecran - 335
        self.vitesse = 12 # vitesse de deplacement du panier


    # methode pour ajouter 5 points
    def ajouter_points(self):
        if self.points < self.maximum_points: # limite de points
            print("+5 points")
            self.points += 5
            self.positionLife += (5*(4.8/self.maximum_points))
            print(self.points)
            print(self.positionLife)
        if self.points >= self.maximum_points:
            #gagne
            print('Gagner')
            self.points = self.maximum_points

    # methode enlever 2 points
    def enlever_points(self):
        if self.points > 0: 
            print("-5 points")
            self.points -= 5
            self.positionLife -= (5*(4.8/self.maximum_points))
            print(self.points)
            print(self.positionLife)
        else:
            # perdu
            self.positionLife = 0
            self.points = 0
            print("Perdu")

    # methode pour le deplacement droite
    def deplacement_droite(self):
        if self.rect.x < 1000: 
            self.rect.x += self.vitesse

    # methode pour le deplacement gauche
    def deplacement_gauche(self):
        if self.rect.x > -50:
            self.rect.x -= self.vitesse
