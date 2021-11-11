#-------------------------------------------------------------------------------
# Name:        test3
# Purpose:     Supression du bug des diagonales !
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

fen_size = fen_width, fen_height = 1540, 800 #Classique
fen = pygame.display.set_mode(fen_size, pygame.RESIZABLE)
fen_surface = pygame.display.get_surface()

pygame.display.set_caption("Dongeon")
clock = pygame.time.Clock() #Le nombre d'ips
fps = 60


class Mur(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, cote = 20, cote2 = 20):
        super(Mur, self).__init__() #Fait référence à la famille supérieur
        self.cote = cote
        self.cote2 = cote2
        self.image = pygame.Surface((self.cote, self.cote2)) #On def la surface de l'objet de la classe Mur
        self.image.fill(sprite_mur) #Son sprite
        self.rect = self.image.get_rect()
        self.rect.x = pos_x #Sa position
        self.rect.y = pos_y




def Creation_mur():
    Mur_obj_list = pygame.sprite.Group()
    Mur_list = []
    for y in range(0, (fen_height//20)):
        for x in range(0, (fen_width//20)):
            Mur_list.append([x * 20, y * 20])
    Dest_list = []
    dest_x = 780
    dest_y = 400
    for deplacement in range(Corridor_size):
        Dest_list.append([dest_x, dest_y])

        rand = random.randint(0, 1) #Variable aléatoire qui détermine si le destoyeur ce déplace en x ou en y

        if rand == 0: #Si rand = 0, on bouge en x
            moveX = random.randint(-1, 1) * 20
            dest_x += moveX
            if moveX == 0: #Si x ne change pas, on change en y
                moveY = random.randint(-1, 1) * 20
                dest_y += moveY
                while moveY == 0:
                    moveY = random.randint(-1, 1) * 20
                    dest_y += moveY

        elif rand == 1: #Si rand = 1, on bouge en y
            moveY = random.randint(-1, 1) * 20
            dest_y += moveY
            if moveY == 0: #Si y ne change pas, on change en x
                moveX = random.randint(-1, 1) * 20
                dest_x += moveX
                while moveX == 0:
                    moveX = random.randint(-1, 1) * 20
                    dest_x += moveX


        if dest_x > fen_width or dest_x < 0: #Reste dans notre écran !
            dest_x = 780
        if dest_y > fen_height or dest_y < 0:
            dest_y = 400

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



def optimisation(liste, mode = 0):
    Mur_opti_list = pygame.sprite.Group()
    Mur_obj_list2 = liste
    if mode == 0:
        for mur in Mur_obj_list2:
            posx = mur.rect.x
            posy = mur.rect.y
            width = mur.cote
            height = mur.cote2
            for mur in Mur_obj_list2:
                if mur.rect.y == posy:
                    if mur.rect.x == posx + 20:
                        mur2 = Mur(posx, posy, width + mur.cote)
                        Mur_opti_list.add(mur2)
    elif mode == 1:
        for mur in Mur_obj_list2:
            posx = mur.rect.x
            posy = mur.rect.y
            width = mur.cote
            height = mur.cote2
            for mur in Mur_obj_list2:
                if mur.rect.x == posx:
                    if mur.rect.y == posy + 20:
                        mur2 = Mur(posx, posy, width, height + mur.cote2)
                        Mur_opti_list.add(mur2)



    return Mur_opti_list




#Boucle principale
Mur_obj_list = Creation_mur()
Mur_opti_list = optimisation(Mur_obj_list)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    if key[pygame.K_SPACE]:
        fen_surface.fill(sprite_couloirs)
        Mur_obj_list = Creation_mur()
        Mur_opti_list = optimisation(Mur_obj_list)

    if key[pygame.K_k]:
        print(len(Mur_obj_list))
        print(len(Mur_opti_list))

    if key[pygame.K_i]:
        fen.fill((0, 255, 0))
        Mur_opti_list.draw(fen)
    else:
        fen.fill((0, 0, 0))
        Mur_obj_list.draw(fen)

    clock.tick(fps) #fps

    pygame.display.update()