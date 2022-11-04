import pygame # importe les composants

# créer une classe qui va representer le concept de joueur ou du panier sur notre jeu
class Panier(pygame.sprite.Sprite):
    """
    Objectif: permet de creer la partie du sprite du joueur qui s'occupera de l'interaction avec les objet qui tombe et s'occupe de la gestion du score
    Args: prend en parametre le module pygame afin de creer un objet a l'ecran et de pouvoir interagire ave
    Return: renvoie le sprite du joueur a l'ecran avec la possibilite de le deplacer de droite a gauche
    """

    # le constructeur
    def __init__(self, largeur_ecran, hauteur_ecran):
        super().__init__()
        # defini le niveau de difficulte qui peut etre change dans les options
        # level 0 = easy
        # level 1 = normal
        # level 2 = hard
        self.level_setting = 0

        # on defini la taille de la fenetre 
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran

        # nombre maximum de points, par defaut a 100
        self.maximum_points = 50

        # nombre de points qu'aura le joueur correspond a la moitie des points max
        self.points = self.maximum_points/2
        
        # on import le sprite du panier au premier plan, il s'agit de la partie du sprite du joueur qui servira pour la colision
        self.image = pygame.image.load('assets/SacDevant.png') # charger l'image du panier
        self.image = pygame.transform.scale(self.image, (250, 250)) # redimentionner l'image
        # on lui definit un rectangle pour permettre d'interagir avec
        self.rect = self.image.get_rect() 
        self.rect.x = (largeur_ecran / 2) - self.image.get_width() /2
        self.rect.y = hauteur_ecran - 335

        # vitesse de deplacement du panier
        self.vitesse = 12 

    # methode executer lorsque de la selection de la difficulte dans le menu des options
    def update_level(self):
        if self.level_setting == 0:
            self.maximum_points = 50
        elif self.level_setting == 1:
            self.maximum_points = 100
        elif self.level_setting == 2:
            self.maximum_points = 200
        # on recalcule le nombre de points initial a chaque changement de difficulte            
        self.points = self.maximum_points/2

    # methode pour ajouter 5 points
    def ajouter_points(self):
        if self.points < self.maximum_points: # limite de points
            self.points += 5
            print(self.points)
            print("+5 points")
        if self.points >= self.maximum_points:
            # partie gagne
            print('Gagner')

    # methode pour enlever 5 points
    def enlever_points(self):
        if self.points >= 5:
            self.points -= 5
            print(self.points)
            print("-5 points")
        elif self.points <= 0:
            # partie perdu
            print("Perdu")

    # methode pour le deplacement droite
    def deplacement_droite(self):
        if self.rect.x < 1000: 
            self.rect.x += self.vitesse

    # methode pour le deplacement gauche
    def deplacement_gauche(self):
        if self.rect.x > -50:
            self.rect.x -= self.vitesse
