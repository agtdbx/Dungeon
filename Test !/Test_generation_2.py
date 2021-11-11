#-------------------------------------------------------------------------------
# Name:        test2
# Purpose:     Optimisation de la génération aléatoire de dongeon !
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
Mur_obj_list = pygame.sprite.Group() #Une liste contenant tout nos murs

fen_size = fen_width, fen_height = 800, 600 #Classique
fen = pygame.display.set_mode(fen_size, pygame.RESIZABLE)
fen_surface = pygame.display.get_surface()

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



def Creation_mur():
    Mur_obj_list = pygame.sprite.Group()
    Mur_list = []
    for y in range(0, 60):
        for x in range(0, 80):
            Mur_list.append([x * 10, y * 10])
    Dest_list = []
    dest_x = random.randint(0, 80)*10
    dest_y = random.randint(0, 60)*10
    for deplacement in range(Corridor_size):
        Dest_list.append([dest_x, dest_y])
        dest_x += random.randint(-1, 1)*10
        dest_y += random.randint(-1, 1)*10

        if dest_x > fen_width or dest_x < 0: #Reste dans notre écran !
            dest_x = random.randint(0, 80)*10
        if dest_y > fen_height or dest_y < 0:
            dest_y = random.randint(0, 60)*10

    #Comparaison des listes et destructions des points commun
    for pos_dest in Dest_list:
        for pos_mur in Mur_list:
            if pos_mur == pos_dest:
                Mur_list.remove(pos_mur)


    #Création des murs
    for pos in Mur_list:
        mur = Mur(pos[0], pos[1])
        Mur_obj_list.add(mur)
    return Mur_obj_list



#Boucle principale
Mur_obj_list = Creation_mur()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    if key[pygame.K_RETURN]:
        fen_surface.fill(sprite_couloirs)
        Mur_obj_list = Creation_mur()

    clock.tick(fps) #fps
    Mur_obj_list.draw(fen)
    pygame.display.update()