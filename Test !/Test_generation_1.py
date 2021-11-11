#-------------------------------------------------------------------------------
# Name:        test1
# Purpose:     Test sur la génération aléatoire de dongeon !
#
# Author:      Gugus
#
# Created:     06/08/2020
# Copyright:   (c) Gugus 2020
# Licence:     <my licence>
#-------------------------------------------------------------------------------

import pygame
import random
pygame.init()

sprite_couloirs = pygame.Color(0, 0, 0) #On défini les sprites des couloirs
sprite_mur = pygame.Color(255, 255, 255) #Ceux des murs
Corridor_size = 5000 #Le nombre de pas de notre créateur de couloir
Mur_list = pygame.sprite.Group() #Une liste contenant tout nos murs

fen_size = fen_width, fen_height = 800, 600 #Classique
fen = pygame.display.set_mode(fen_size, pygame.RESIZABLE)

pygame.display.set_caption("Dongeon")
clock = pygame.time.Clock() #Le nombre d'ips
fps = 60


class Mur(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Mur, self).__init__() #Fait référence à la famille supérieur
        self.image = pygame.Surface((10, 10)) #On def la surface de l'objet de la classe Mur
        self.image.fill(sprite_mur) #Son sprite
        self.rect = self.image.get_rect()
        self.rect.x = pos_x #Sa position
        self.rect.y = pos_y


class Destroyer(pygame.sprite.Sprite): #On crée un classe pour créer nos couloirs. Un petit destoyeur va se balader aléatoirement et transformer nos murs en couloirs.
    def __init__(self):
        super(Destroyer, self).__init__()
        self.image = pygame.Surface((10, 10)) #Idem mais pour le destroyeur
        self.rect = self.image.get_rect()

    def set_position(self, x, y): #Pour def sa position aléatoire
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y, collidable = pygame.sprite.Group()): #Pour update le tout
        self.set_position(x, y)
        collision_list = pygame.sprite.spritecollide(self, collidable, False, None)
        for collided_object in collision_list:
            collidable.remove(collided_object)
        return collidable


#Création des murs
for row in range(0, 60):
    for column in range(0, 80):
        mur = Mur(column * 10, row * 10) #On def toute nos cellules comme étant des murs
        Mur_list.add(mur)


#Créations et mouvement du Destroyeur
dest = Destroyer()
dest.set_position(random.randint(0, 80)*10, random.randint(0, 60)*10) #Position aléatoire de départ
dest_x = dest.rect.x
dest_y = dest.rect.y

for i in range(Corridor_size): #On déf son déplacement aussi aléatoire
    fen.blit(dest.image, (dest_x, dest_y))
    dest_x += random.randint(-1, 1)*10
    dest_y += random.randint(-1, 1)*10
    if dest_x > fen_width or dest_x < 0: #Et qu'il reste dans notre écran !!
        dest_x = random.randint(0, 80)*10
    if dest_y > fen_height or dest_y < 0:
        dest_y = random.randint(0, 60)*10

    Mur_list = dest.update(dest_x, dest_y, Mur_list)


#Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    clock.tick(fps) #fps
    Mur_list.draw(fen)
    pygame.display.update()