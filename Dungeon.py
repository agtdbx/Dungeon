#-------------------------------------------------------------------------------
# Name:        Main
# Purpose:     Le jeu
#
# Author:      Gugus
#
# Created:     06/08/2020
# Copyright:   (c) Gugus 2020
# Licence:     <my licence>
#-------------------------------------------------------------------------------

import pygame
import pickle
import math
import random
pygame.init()



#Variables
Corridor_size = 10000 #Le nombre de pas de notre crÃ©ateur de couloir
Mur_obj_list = pygame.sprite.Group() #Une liste contenant tout nos murs

fen_size = fen_width, fen_height = 1920, 1080 #Taille de la fenÃªtre
##fen = pygame.display.set_mode(fen_size)
fen = pygame.display.set_mode(fen_size)
fen_surface = pygame.display.get_surface()

pygame.display.set_caption("Dungeon") #Nom de la fenÃªtre
clock = pygame.time.Clock()
fps = 30 #Le nombre de fps

tps = 0 #Variable qui sert Ã  calculer le temps passer Ã  jouer

run2 = True
fenetre = 0

full_screen = False

Fond_liste = [] #Liste qui va accuillir les objets de la classe Fonds

nb_niveaux = int(0) #Niveau dans lequel on se trouve

niveau_save = 0 #Niveau dans lequel on rÃ©aparait si on meurt face Ã  un boss

nb_mort = 0 #Nombre de mort

anti_bug = 0 #Cette variable sert Ã  emÃªcher creer un petit temps entre les cliques du joueur. Pygame dÃ©tecte deux fois le clic souris, c'est pour Ã©viter au joueur d'appuyer trop vite sur les boutons

test_collid = 0
test_pos = (0, 0)
#Variable permetant de dÃ©terminer au jeu dans ou on en est (fin, mort, ...)
Fin = False

run = True
run2 = True

#Ces listes contiennes les diffÃ©rents changement en augmentant de niveau. Si notre vie est niveau 3, on fait Lvl_life[3-1] -> 140 pv. Idem pour les autres niveaux
Lvl_life = [100, 120, 140, 160, 180, 200, 230, 260, 290, 340, 390, 440, 500]
Lvl_strengh = [1, 2, 3, 6, 8, 10, 13, 16, 20, 24, 29, 34, 40, 50]
Lvl_speed = [5, 6, 7, 8, 9]


Map = [[0 for j in range(fen_width // 20)] for i in range(fen_height // 20)]

nb_arme = 0



# Importation des sons
Son_rapiere = pygame.mixer.Sound('Sons/Rapiere.wav')
Son_epee = pygame.mixer.Sound('Sons/Epee.wav')
Son_marteau = pygame.mixer.Sound('Sons/Marteau.wav')
Son_lvlup = pygame.mixer.Sound('Sons/Lvl_up.wav')
Son_perso_toucher = pygame.mixer.Sound('Sons/Perso_toucher.wav')
Son_mob_toucher = pygame.mixer.Sound('Sons/Mob_toucher.wav')
Son_boss_atk1 = pygame.mixer.Sound('Sons/Boss_atk1.wav')
Son_boss_atk2 = pygame.mixer.Sound('Sons/Boss_atk2.wav')
Son_projectile = pygame.mixer.Sound('Sons/Projectiles.wav')
Son_bouton = pygame.mixer.Sound('Sons/Button.wav')
Son_crit = pygame.mixer.Sound('Sons/Crit.wav')




#Importation des sprites (C'est long)
sprite_perso_U = pygame.image.load('Sprites/Perso/Perso_U.png').convert_alpha()
sprite_perso_R = pygame.image.load('Sprites/Perso/Perso_R.png').convert_alpha()
sprite_perso_L = pygame.image.load('Sprites/Perso/Perso_L.png').convert_alpha()
sprite_perso_D = pygame.image.load('Sprites/Perso/Perso_D.png').convert_alpha()

sprite_mob_U = pygame.image.load('Sprites/Ennemy/Mobs_U.png').convert_alpha()
sprite_mob_R = pygame.image.load('Sprites/Ennemy/Mobs_R.png').convert_alpha()
sprite_mob_L = pygame.image.load('Sprites/Ennemy/Mobs_L.png').convert_alpha()
sprite_mob_D = pygame.image.load('Sprites/Ennemy/Mobs_D.png').convert_alpha()

sprite_boss_U = pygame.image.load('Sprites/Ennemy/Boss_U.png')
sprite_boss_R = pygame.image.load('Sprites/Ennemy/Boss_R.png')
sprite_boss_L = pygame.image.load('Sprites/Ennemy/Boss_L.png')
sprite_boss_D = pygame.image.load('Sprites/Ennemy/Boss_D.png')

sprite_boss_atk1_RL = [pygame.image.load('Sprites/Ennemy/Boss_atk1_RL1.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL2.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL3.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL4.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL4.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL5.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL6.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL7.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL8.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL9.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL10.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL11.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL12.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL13.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL14.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL15.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL16.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL17.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL18.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL19.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL20.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL21.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL22.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL23.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL24.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL25.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL26.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL27.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL28.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL29.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL30.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL31.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL32.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL33.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL34.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL35.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL36.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL37.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL38.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL39.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL40.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL41.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL42.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL43.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL44.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL45.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL46.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL47.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL48.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL49.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL50.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL51.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL52.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL53.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL54.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL55.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL56.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL57.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL58.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL59.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL60.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL61.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL62.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL63.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL64.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL65.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL66.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL67.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL68.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL69.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL70.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL71.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL72.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL73.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL74.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL75.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL76.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL77.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL78.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL79.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL80.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL81.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL82.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL83.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL84.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL85.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL86.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL87.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL88.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL89.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_RL90.png')]

sprite_boss_atk1_UD = [pygame.image.load('Sprites/Ennemy/Boss_atk1_UD1.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD2.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD3.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD4.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD4.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD5.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD6.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD7.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD8.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD9.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD10.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD11.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD12.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD13.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD14.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD15.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD16.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD17.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD18.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD19.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD20.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD21.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD22.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD23.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD24.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD25.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD26.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD27.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD28.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD29.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD30.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD31.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD32.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD33.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD34.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD35.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD36.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD37.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD38.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD39.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD40.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD41.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD42.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD43.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD44.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD45.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD46.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD47.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD48.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD49.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD50.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD51.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD52.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD53.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD54.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD55.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD56.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD57.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD58.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD59.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD60.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD61.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD62.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD63.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD64.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD65.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD66.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD67.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD68.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD69.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD70.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD71.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD72.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD73.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD74.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD75.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD76.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD77.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD78.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD79.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD80.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD81.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD82.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD83.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD84.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD85.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD86.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD87.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD88.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD89.png'),
                        pygame.image.load('Sprites/Ennemy/Boss_atk1_UD90.png')]


sprite_boss_atk2 = [pygame.image.load('Sprites/Ennemy/Boss_atk2_1.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_2.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_3.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_4.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_5.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_6.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_7.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_8.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_9.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_10.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_11.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_12.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_13.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_14.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_15.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_16.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_17.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_18.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_19.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk2_20.png')]


sprite_boss_atk3_U = [pygame.image.load('Sprites/Ennemy/Boss_atk3_U1.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_U2.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_U3.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_U4.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_U5.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_U6.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_U7.png')]

sprite_boss_atk3_D = [pygame.image.load('Sprites/Ennemy/Boss_atk3_D1.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_D2.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_D3.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_D4.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_D5.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_D6.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_D7.png')]

sprite_boss_atk3_L = [pygame.image.load('Sprites/Ennemy/Boss_atk3_L1.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_L2.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_L3.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_L4.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_L5.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_L6.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_L7.png')]

sprite_boss_atk3_R = [pygame.image.load('Sprites/Ennemy/Boss_atk3_R1.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_R2.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_R3.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_R4.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_R5.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_R6.png'),
                    pygame.image.load('Sprites/Ennemy/Boss_atk3_R7.png')]

sprite_pro_U = pygame.image.load('Sprites/Ennemy/Pro_U.png').convert_alpha()
sprite_pro_R = pygame.image.load('Sprites/Ennemy/Pro_R.png').convert_alpha()
sprite_pro_L = pygame.image.load('Sprites/Ennemy/Pro_L.png').convert_alpha()
sprite_pro_D = pygame.image.load('Sprites/Ennemy/Pro_D.png').convert_alpha()


Ecran_titre = pygame.image.load('Sprites/Fonds/Ecran_titre1.png').convert_alpha()

Menu = pygame.image.load('Sprites/Fonds/Menu.png').convert_alpha()

sprite_epee_U = [pygame.image.load('Sprites/Armes/Epee_U1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_U2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_U3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_U4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_U5.png').convert_alpha()]
sprite_epee_R = [pygame.image.load('Sprites/Armes/Epee_R1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_R2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_R3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_R4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_R5.png').convert_alpha()]
sprite_epee_L = [pygame.image.load('Sprites/Armes/Epee_L1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_L2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_L3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_L4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_L5.png').convert_alpha()]
sprite_epee_D = [pygame.image.load('Sprites/Armes/Epee_D1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_D2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_D3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_D4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Epee_D5.png').convert_alpha()]
sprite_cepee_U = [pygame.image.load('Sprites/Armes/Cepee_U1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_U2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_U3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_U4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_U5.png').convert_alpha()]
sprite_cepee_R = [pygame.image.load('Sprites/Armes/Cepee_R1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_R2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_R3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_R4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_R5.png').convert_alpha()]
sprite_cepee_L = [pygame.image.load('Sprites/Armes/Cepee_L1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_L2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_L3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_L4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_L5.png').convert_alpha()]
sprite_cepee_D = [pygame.image.load('Sprites/Armes/Cepee_D1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_D2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_D3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_D4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Cepee_D5.png').convert_alpha()]
sprite_rap_U = [pygame.image.load('Sprites/Armes/Rap_U1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_U2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_U3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_U4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_U5.png').convert_alpha()]
sprite_rap_R = [pygame.image.load('Sprites/Armes/Rap_R1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_R2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_R3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_R4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_R5.png').convert_alpha()]
sprite_rap_L = [pygame.image.load('Sprites/Armes/Rap_L1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_L2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_L3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_L4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_L5.png').convert_alpha()]
sprite_rap_D = [pygame.image.load('Sprites/Armes/Rap_D1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_D2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_D3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_D4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Rap_D5.png').convert_alpha()]
sprite_bepee_U = [pygame.image.load('Sprites/Armes/Bepee_U1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_U2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_U3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_U4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_U5.png').convert_alpha()]
sprite_bepee_R = [pygame.image.load('Sprites/Armes/Bepee_R1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_R2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_R3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_R4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_R5.png').convert_alpha()]
sprite_bepee_L = [pygame.image.load('Sprites/Armes/Bepee_L1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_L2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_L3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_L4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_L5.png').convert_alpha()]
sprite_bepee_D = [pygame.image.load('Sprites/Armes/Bepee_D1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_D2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_D3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_D4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/Bepee_D5.png').convert_alpha()]
sprite_hache_U = [pygame.image.load('Sprites/Armes/hache_U1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_U2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_U3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_U4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_U5.png').convert_alpha()]
sprite_hache_R = [pygame.image.load('Sprites/Armes/hache_R1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_R2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_R3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_R4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_R5.png').convert_alpha()]
sprite_hache_L = [pygame.image.load('Sprites/Armes/hache_L1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_L2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_L3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_L4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_L5.png').convert_alpha()]
sprite_hache_D = [pygame.image.load('Sprites/Armes/hache_D1.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_D2.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_D3.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_D4.png').convert_alpha(),
                pygame.image.load('Sprites/Armes/hache_D5.png').convert_alpha()]
sprite_marteau_U = [pygame.image.load('Sprites/Armes/marteau_U1.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_U2.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_U3.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_U4.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_U5.png').convert_alpha()]
sprite_marteau_R = [pygame.image.load('Sprites/Armes/marteau_R1.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_R2.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_R3.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_R4.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_R5.png').convert_alpha()]
sprite_marteau_L = [pygame.image.load('Sprites/Armes/marteau_L1.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_L2.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_L3.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_L4.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_L5.png').convert_alpha()]
sprite_marteau_D = [pygame.image.load('Sprites/Armes/marteau_D1.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_D2.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_D3.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_D4.png').convert_alpha(),
                    pygame.image.load('Sprites/Armes/marteau_D5.png').convert_alpha()]

sprite_couloirs = pygame.image.load('Sprites/Fonds/couloirss.png').convert_alpha()
sprite_mur = pygame.image.load('Sprites/Fonds/Murs.png').convert_alpha()

Button = pygame.image.load('Sprites/Fonds/But.png').convert_alpha()
Button2 = pygame.image.load('Sprites/Fonds/But2_.png').convert_alpha()

Mbutton = pygame.image.load('Sprites/Fonds/Mbut.png').convert_alpha()
Mbutton2 = pygame.image.load('Sprites/Fonds/Mbut2.png').convert_alpha()

Ecran_suite = pygame.image.load('Sprites/Fonds/Ecran_suite.png').convert_alpha()

Ecran_mort = pygame.image.load('Sprites/Fonds/Ecran_mort.png').convert_alpha()




#Classes
class Fonds(pygame.sprite.Sprite):
    """Classe des murs"""
    def __init__(self, pos_x, pos_y, nb):
        """CrÃ©er nos murs. Prends en parametre  x int(x), y int(y) et nb int(nb). Nb vaut un si c'est un mur, 0 si c'est un couloir"""
        self.image = pygame.Surface((20, 20)) #On def la surface de l'objet de la classe Mur
        self.rect = self.image.get_rect()
        self.rect.x = pos_x #Sa position
        self.rect.y = pos_y
        self.nb = nb
        if nb == 0:
            self.image = sprite_couloirs
        elif nb == 1:
            self.image = sprite_mur


    def draw(self, fen):
        """MÃ©thode permettant de voire nos fonds ! Prends en parametre la surface de dessins fen"""
        fen.blit(self.image, (self.rect.x, self.rect.y))



class Arme():
    """La classe des armes !"""

    def __init__(self, nom,  atk, rangee, coldown, num):
        """On crÃ©er nos armes. Prends en parametre son nom str(nom), ses dÃ©gats de base int(atk), sa portÃ©e int(rangee), son rythme d'attaque int(coldown) et son numÃ©ro int(num).
        Son numÃ©ro sert Ã  diffÃ©rencier les types d'armes. 1 pour les Ã©pees Ã  une main, 2 pour les Ã©pees courtes, 3 pour les rapiÃ¨res, 4 pour les Ã©pÃ©es Ã  deux mains,
        5 pour les haches et 6 pour les marteaux"""
        self.nom = str(nom)
        self.atk = int(atk)
        self.range = int(rangee)
        self.coldown = int(coldown)
        self.lvl = 0
        self.num = num


    def upgrade(self):
        """MÃ©thode permettant d'amÃ©liorer nos armes"""
        perso.gold -= 50 + (25*self.lvl)
        self.atk += (self.atk//5)
        self.lvl += 1


arm1 = Arme("Apprentice sword", 15, 20, 15, 1) #30 dps
arm2 = Arme('Used sword', 20, 20, 15, 1) #40 dps
arm3 = Arme('Rusty sword', 10, 20, 15, 1) #20 dps
arm4 = Arme('Knight\'s sword', 35, 20, 15, 1) #70 dps
arm5 = Arme('Sharp sword', 45, 20, 15, 1) #90 dps
arm6 = Arme('Muramasa', 60, 20, 15, 1) #120 dps

arm7 = Arme('Dagger', 50, 10, 10, 2) #150 dps
arm8 = Arme('Short sword', 30, 10, 10, 2) #60 dps

arm9 = Arme('Rapier', 20, 20, 5, 3) #120 dps
arm10 = Arme('Fine sword', 10, 20, 5, 3) #60 dps

arm11 = Arme('Two-handed sword', 30, 25, 25, 4) #36 dps
arm12 = Arme('Fake Sacred Sword', 40, 25, 25, 4) #48 dps
arm13 = Arme('40 meter sword', 50, 25, 25, 4) #60 dps
arm14 = Arme('Excalibur', 100, 20, 25, 4) #120 dps

arm15 = Arme('Lumberjack\'s axe', 30, 30, 25, 5) #36 dps
arm16 = Arme('Halbard', 40, 30, 25, 5) #48 dps
arm17 = Arme('Guillotine', 50, 30, 25, 5) #60 dps

arm18 = Arme('War hammer', 60, 20, 45, 6) #40 dps
arm19 = Arme("Big hammer", 100, 20, 45, 6) #66.7 dps
arm20 = Arme('Mjolnir', 150, 20, 45, 6) #100 dps

arme_list = [arm1, arm2, arm3, arm4, arm5,
            arm6, arm7, arm8, arm9, arm10,
            arm11, arm12, arm13, arm14, arm15,
            arm16, arm17, arm18, arm19, arm20]






class Projectile():
    """Classe pour les projectiles des boss !"""

    def __init__(self, x, y, vel, atk, direction):
        """Prends en parametre x int(x) et y int(y) de base du tire, la vÃ©locitÃ© int(vel), les dÃ©gats int(atk) et la direction str(direction).
        La direction peut valoir 'Up', 'Down', 'Right' ou 'Left'."""
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.vel = vel
        self.atk = atk
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = str(direction)


    def draw(self):
        """MÃ©thode permettant d'afficher les projectiles"""
        if self.direction == 'Up':
            self.width = 20
            self.height = 50
            fen.blit(sprite_pro_U, (self.x, self.y))
        elif self.direction == 'Down':
            self.width = 20
            self.height = 50
            fen.blit(sprite_pro_D, (self.x, self.y))
        elif self.direction == 'Right':
            self.width = 50
            self.height = 20
            fen.blit(sprite_pro_R, (self.x, self.y))
        elif self.direction == 'Left':
            self.width = 50
            self.height = 20
            fen.blit(sprite_pro_L, (self.x, self.y))


    def move(self):
        """MÃ©thodes permettant de faire bouger les projectiles"""
        if self.direction == 'Up':
            self.y -= self.vel
        elif self.direction == 'Right':
            self.x += self.vel
        elif self.direction == 'Left':
            self.x -= self.vel
        elif self.direction == 'Down':
            self.y += self.vel


    def attaque(self):
        """MÃ©thode dÃ©finissant ce qu'il se passe lors d'une collision avec le joueur."""
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.hitbox.colliderect(perso.hitbox):
            perso.pv -= self.atk

projectiles_list = []






class Personnage(object):
    """Classe du personnage"""

    def __init__(self, arm):
        """Prends en parametre l'arme de dÃ©part (arm)"""
        self.x = 740
        self.y = 400
        self.width = 16
        self.height = 16
        self.arme = arm
        self.vel = 5
        self.life = 100
        self.pv = self.life
        self.strengh = 1
        self.dommage = self.arme.atk
        self.atk = self.dommage + self.strengh
        self.range = self.arme.range
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.r_atk_U = pygame.Rect(self.x, self.y - self.height, self.width, self.height)
        self.r_atk_R = pygame.Rect(self.x + self.width, self.y, self.width, self.height)
        self.r_atk_D = pygame.Rect(self.x, self.y + self.height, self.width, self.height)
        self.r_atk_L = pygame.Rect(self.x - self.height, self.y, self.width, self.height)
        self.U = True
        self.R = False
        self.D = False
        self.L = False
        self.coldown = self.arme.coldown
        self.col = 0
        self.xp = 0
        self.lvl = 0
        self.lvl_life = 0
        self.lvl_strengh = 0
        self.lvl_speed = 0
        self.gold = 0
        self.alea = 0
        self.crit = 0



    def draw(self):
        """Permet d'afficher le personnage"""
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.U:
            fen.blit(sprite_perso_U, (self.x, self.y))
        elif self.R:
            fen.blit(sprite_perso_R, (self.x, self.y))
        elif self.L:
            fen.blit(sprite_perso_L, (self.x, self.y))
        elif self.D:
            fen.blit(sprite_perso_D, (self.x, self.y))

        pygame.draw.rect(fen, (200, 0, 0), (self.x - (self.life //10) + self.width //2, self.y - 8, self.life // 5, 4))
        if self.pv < 0:
            self.pv == 0
        pygame.draw.rect(fen, (0, 200, 0), (self.x - (self.life //10) + self.width //2, self.y - 8, self.pv // 5, 4))


    def move(self, direct):
        """Permet de faire bouger le personnage. Prends en paramÃ¨tre la direction int(direct) dans laquelle il va.
        Si direct = 0, le personnage va en haut, si il vaut 1, il va Ã  droite, 2 pour en bas et 3 pour la gauche"""
        a = True
        b = 0
        X = int((self.x + self.width/2)/20)
        Y = int((self.y + self.height/2)/20)
        if direct == 0 and self.y >0:
            while a:
                self.y -= 1
                self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
                b += 1
                fond = Map[Y-1][X]
                if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                    a = False
                    self.y += 1
                if b == self.vel:
                    a = False
            self.U = True
            self.R = False
            self.D = False
            self.L = False

        elif direct == 1 and self.x < (1920 - self.width - self.vel - 5):
            while a:
                self.x += 1
                self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
                b += 1
                fond = Map[Y][X+1]
                if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                    a = False
                    self.x -= 1
                if b == self.vel:
                    a = False
            self.U = False
            self.R = True
            self.D = False
            self.L = False

        elif direct == 2 and self.y < (1080 - self.height - self.vel - 5):
            while a:
                self.y += 1
                self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
                b += 1
                fond = Map[Y+1][X]
                if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                    a = False
                    self.y -= 1
                if b == self.vel:
                    a = False
            self.U = False
            self.R = False
            self.D = True
            self.L = False

        elif direct == 3 and self.x > 0:
            while a:
                self.x -= 1
                self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
                b += 1
                fond = Map[Y][X-1]
                if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                    a = False
                    self.x += 1
                if b == self.vel:
                    a = False
            self.U = False
            self.R = False
            self.D = False
            self.L = True


    def Dammage(self):
        """Permet de faire attaquer le personnage"""
        self.alea = random.randint(-10, 10)
        self.crit = random.randint(0, 100)
        self.r_atk_U = pygame.Rect(self.x - self.width // 2, self.y - self.range, self.width * 2, self.range)
        self.r_atk_R = pygame.Rect(self.x + self.width, self.y - self.height // 2, self.range, self.height * 2)
        self.r_atk_D = pygame.Rect(self.x - self.width // 2, self.y + self.height, self.width * 2, self.range)
        self.r_atk_L = pygame.Rect(self.x - self.range, self.y - self.height // 2, self.range, self.height * 2)

        key2 = pygame.mouse.get_pressed()
        if key2[0] == 1 and self.col == 0:
            if self.arme.num == 1 or self.arme.num == 4 or self.arme.num == 5:
                Son_epee.play()
            elif self.arme.num == 2 or self.arme.num == 3:
                Son_rapiere.play()
            elif self.arme.num == 6:
                Son_marteau.play()
            self.col += 1

            if nb_niveaux == 5:
                if boss1.hitbox.colliderect(self.r_atk_U):
                    if self.crit > 95:
                        boss1.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss1.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss1.hitbox.colliderect(self.r_atk_R):
                    if self.crit > 95:
                        boss1.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss1.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss1.hitbox.colliderect(self.r_atk_D):
                    if self.crit > 95:
                        boss1.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss1.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss1.hitbox.colliderect(self.r_atk_L):
                    if self.crit > 95:
                        boss1.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss1.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()

            elif nb_niveaux == 10:
                if boss2.hitbox.colliderect(self.r_atk_U):
                    if self.crit > 95:
                        boss2.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss2.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss1.hitbox.colliderect(self.r_atk_R):
                    if self.crit > 95:
                        boss2.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss2.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss2.hitbox.colliderect(self.r_atk_D):
                    if self.crit > 95:
                        boss2.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss2.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss2.hitbox.colliderect(self.r_atk_L):
                    if self.crit > 95:
                        boss2.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss2.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()

            elif nb_niveaux == 15:
                if boss3.hitbox.colliderect(self.r_atk_U):
                    if self.crit > 95:
                        boss3.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss3.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss3.hitbox.colliderect(self.r_atk_R):
                    if self.crit > 95:
                        boss3.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss3.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss3.hitbox.colliderect(self.r_atk_D):
                    if self.crit > 95:
                        boss3.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss3.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss3.hitbox.colliderect(self.r_atk_L):
                    if self.crit > 95:
                        boss3.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss3.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()

            elif nb_niveaux == 20:
                if boss4.hitbox.colliderect(self.r_atk_U):
                    if self.crit > 95:
                        boss4.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss4.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss4.hitbox.colliderect(self.r_atk_R):
                    if self.crit > 95:
                        boss4.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss4.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss4.hitbox.colliderect(self.r_atk_D):
                    if self.crit > 95:
                        boss4.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss4.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss4.hitbox.colliderect(self.r_atk_L):
                    if self.crit > 95:
                        boss4.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss4.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()


            elif nb_niveaux == 25:
                if boss5.hitbox.colliderect(self.r_atk_U):
                    if self.crit > 95:
                        boss5.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss5.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss5.hitbox.colliderect(self.r_atk_R):
                    if self.crit > 95:
                        boss5.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss5.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss5.hitbox.colliderect(self.r_atk_D):
                    if self.crit > 95:
                        boss5.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss5.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss5.hitbox.colliderect(self.r_atk_L):
                    if self.crit > 95:
                        boss5.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss5.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()

            elif nb_niveaux == 30:
                if boss_final.hitbox.colliderect(self.r_atk_U):
                    if self.crit > 95:
                        boss_final.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss_final.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss_final.hitbox.colliderect(self.r_atk_R):
                    if self.crit > 95:
                        boss_final.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss_final.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss_final.hitbox.colliderect(self.r_atk_D):
                    if self.crit > 95:
                        boss_final.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss_final.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()
                elif boss_final.hitbox.colliderect(self.r_atk_L):
                    if self.crit > 95:
                        boss_final.pv -= self.atk * 2
                        Son_crit.play()
                    else:
                        boss_final.pv -= self.atk + ((self.atk // 100) * self.alea)
                        Son_mob_toucher.play()

            else:
                for mob in Mobs:
                    if mob.hitbox.colliderect(self.r_atk_U):
                        if self.crit > 95:
                            mob.pv -= self.atk * 2
                            Son_crit.play()
                        else:
                            mob.pv -= self.atk + ((self.atk // 100) * self.alea)
                            Son_mob_toucher.play()
                        mob.y -= self.arme.range
                    elif mob.hitbox.colliderect(self.r_atk_R):
                        if self.crit > 95:
                            mob.pv -= self.atk * 2
                            Son_crit.play()
                        else:
                            mob.pv -= self.atk + ((self.atk // 100) * self.alea)
                            Son_mob_toucher.play()
                        mob.x += self.arme.range
                    elif mob.hitbox.colliderect(self.r_atk_D):
                        if self.crit > 95:
                            mob.pv -= self.atk * 2
                            Son_crit.play()
                        else:
                            mob.pv -= self.atk + ((self.atk // 100) * self.alea)
                            Son_mob_toucher.play()
                        mob.y += self.arme.range
                    elif mob.hitbox.colliderect(self.r_atk_L):
                        if self.crit > 95:
                            mob.pv -= self.atk * 2
                            Son_crit.play()
                        else:
                            mob.pv -= self.atk + ((self.atk // 100) * self.alea)
                            Son_mob_toucher.play()
                        mob.x -= self.arme.range

        if self.col != 0 and self.col < 6:
            if self.arme.num == 1:
                if self.U:
                    fen.blit(sprite_epee_U[self.col-1], (self.x - self.width // 2, self.y - self.height))
                elif self.R:
                    fen.blit(sprite_epee_R[self.col-1], (self.x + self.width, self.y - self.height // 2))
                elif self.L:
                    fen.blit(sprite_epee_L[self.col-1], (self.x - self.width, self.y - self.height // 2))
                elif self.D:
                    fen.blit(sprite_epee_D[self.col-1], (self.x - self.width // 2, self.y + self.height))

            elif self.arme.num == 2:
                if self.U:
                    fen.blit(sprite_cepee_U[self.col-1], (self.x - self.width // 2, self.y - self.height))
                elif self.R:
                    fen.blit(sprite_cepee_R[self.col-1], (self.x + self.width, self.y - self.height // 2))
                elif self.L:
                    fen.blit(sprite_cepee_L[self.col-1], (self.x - self.width, self.y - self.height // 2))
                elif self.D:
                    fen.blit(sprite_cepee_D[self.col-1], (self.x - self.width // 2, self.y + self.height))

            elif self.arme.num == 3:
                if self.U:
                    fen.blit(sprite_rap_U[self.col-1], (self.x - self.width // 2, self.y - self.height))
                elif self.R:
                    fen.blit(sprite_rap_R[self.col-1], (self.x + self.width, self.y - self.height // 2))
                elif self.L:
                    fen.blit(sprite_rap_L[self.col-1], (self.x - self.width, self.y - self.height // 2))
                elif self.D:
                    fen.blit(sprite_rap_D[self.col-1], (self.x - self.width // 2, self.y + self.height))

            elif self.arme.num == 4:
                if self.U:
                    fen.blit(sprite_bepee_U[self.col-1], (self.x - self.width // 2, self.y - self.height))
                elif self.R:
                    fen.blit(sprite_bepee_R[self.col-1], (self.x + self.width, self.y - self.height // 2))
                elif self.L:
                    fen.blit(sprite_bepee_L[self.col-1], (self.x - self.width, self.y - self.height // 2))
                elif self.D:
                    fen.blit(sprite_bepee_D[self.col-1], (self.x - self.width // 2, self.y + self.height))

            elif self.arme.num == 5:
                if self.U:
                    fen.blit(sprite_hache_U[self.col-1], (self.x - self.width // 2, self.y - self.height))
                elif self.R:
                    fen.blit(sprite_hache_R[self.col-1], (self.x + self.width, self.y - self.height // 2))
                elif self.L:
                    fen.blit(sprite_hache_L[self.col-1], (self.x - self.width, self.y - self.height // 2))
                elif self.D:
                    fen.blit(sprite_hache_D[self.col-1], (self.x - self.width // 2, self.y + self.height))

            else:
                if self.U:
                    fen.blit(sprite_marteau_U[self.col-1], (self.x - self.width // 2, self.y - self.height))
                elif self.R:
                    fen.blit(sprite_marteau_R[self.col-1], (self.x + self.width, self.y - self.height // 2))
                elif self.L:
                    fen.blit(sprite_marteau_L[self.col-1], (self.x - self.width, self.y - self.height // 2))
                elif self.D:
                    fen.blit(sprite_marteau_D[self.col-1], (self.x - self.width // 2, self.y + self.height))


        if self.col >= self.coldown:
            self.col = 0
        elif self.col != 0:
            self.col += 1


    def lvl_up(self, choix):
        """Permet au jour de passer de niveau. Prends en paramÃ¨tre le choix str(choix). Le choix peut valoir 'Vie', 'Force' ou 'Vitesse'."""
        self.xp -= (10 + (10*self.lvl))
        self.lvl += 1

        if choix == 'Vie' and self.lvl_life < 12:
            self.lvl_life += 1
            a = self.life - self.pv
            self.life = Lvl_life[self.lvl_life]
            self.pv = self.life - a

        elif choix == 'Force' and self.lvl_strengh < 13:
            self.lvl_strengh += 1
            self.strengh = Lvl_strengh[self.lvl_strengh]
            self.atk = self.dommage + self.strengh

        elif choix == 'Vitesse' and self.lvl_speed < 4:
            self.lvl_speed += 1
            self.vel = Lvl_speed[self.lvl_speed]


    def change(self, arme, act):
        """Permet au personnage de changer d'armes. Prends en paramÃ¨tre la nouvelle arme (arm) et le choix int(act). Si act vaut 0, il y a changement d'arme, sinon on garde la mÃªme."""
        global boss
        if act == 0:
            self.arme = arme
            self.dommage = arme.atk
            self.range = arme.range
            self.coldown = arme.coldown
        boss = True

perso = Personnage(arm1)




class Monstre():
    """Classe des monstres"""

    def __init__(self, nb_niveaux):
        """Prends en paramÃ¨tre le nombre de niveau int(nb_niveau)"""
        self.x = 100
        self.y = 100
        self.width = 16
        self.height = 16
        if nb_niveaux < 5:
            self.life = random.randint(30, 100)
            self.atk = random.randint(2, 10)
            self.vel = random.randint(1, 3)
        elif nb_niveaux < 10:
            self.life = random.randint(50, 200)
            self.atk = random.randint(4, 20)
            self.vel = random.randint(1, 3)
        elif nb_niveaux < 15:
            self.life = random.randint(50, 300)
            self.atk = random.randint(10, 40)
            self.vel = random.randint(1, 4)
        elif nb_niveaux < 20:
            self.life = random.randint(50, 400)
            self.atk = random.randint(20, 60)
            self.vel = random.randint(2, 4)
        elif nb_niveaux < 25:
            self.life = random.randint(100, 500)
            self.atk = random.randint(30, 80)
            self.vel = random.randint(2, 5)
        else:
            self.life = random.randint(100, 600)
            self.atk = random.randint(20, 60)
            self.vel = random.randint(3, 6)

        self.pv = self.life
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.U = True
        self.R = False
        self.D = False
        self.L = False
        self.son = 0
        self.alea = 0
        self.crit = 0


    def draw(self):
        """Permet de dessiner nos montres"""
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.U:
            fen.blit(sprite_mob_U, (self.x, self.y))
        elif self.R:
            fen.blit(sprite_mob_R, (self.x, self.y))
        elif self.L:
            fen.blit(sprite_mob_L, (self.x, self.y))
        elif self.D:
            fen.blit(sprite_mob_D, (self.x, self.y))

        if self.pv < 0:
            self.pv == 0
        pygame.draw.rect(fen, (200, 0, 0), (self.x - (self.life //10) + self.width //2, self.y - 6, self.life // 5, 4))
        pygame.draw.rect(fen, (0, 200, 0), (self.x - (self.life //10) + self.width //2, self.y - 6, self.pv // 5, 4))


    def move(self, Map):
        """Permet de faire bouger nos monstres"""
        X = int((self.x + self.width/2)/20)
        Y = int((self.y + self.height/2)/20)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        a = math.sqrt((perso.x - self.x)**2 + (perso.y - self.y)**2)
        b = random.randint(0, 1)
        if a < 200:
            fixX = self.x - perso.x
            fixY = self.y - perso.y

            if fixX < 0 and b == 0:
                fond = Map[Y][X + 1]
                if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                    self.x -= self.vel
                else:
                    self.x += self.vel
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False

            elif fixX > 0 and b == 0:
                fond = Map[Y][X - 1]
                if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                    self.x += self.vel
                else:
                    self.x -= self.vel
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True

            elif fixX == 0 and b != 0:
                if fixY < 0:
                    fond = Map[Y + 1][X]
                    if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                        self.y -= self.vel
                    else:
                        self.y += self.vel
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False

                elif fixY > 0:
                    fond = Map[Y - 1][X]
                    if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                        self.y += self.vel
                    else:
                        self.y -= self.vel
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False


            if fixY < 0 and b == 1:
                fond = Map[Y + 1][X]
                if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                    self.y -= self.vel
                else:
                    self.y += self.vel
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False

            elif fixY > 0 and b == 1:
                fond = Map[Y - 1][X]
                if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                    self.y += self.vel
                else:
                    self.y -= self.vel
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False

            elif fixY == 0  and b == 1:
                if fixX < 0:
                    fond = Map[Y][X + 1]
                    if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                        self.x -= self.vel
                    else:
                        self.x += self.vel
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False

                elif fixX > 0:
                    fond = Map[Y][X - 1]
                    if fond.rect.colliderect(self.hitbox) and fond.nb == 1:
                            self.x += self.vel
                    else:
                        self.x -= self.vel
                        self.U = False
                        self.R = False
                        self.D = False
                        self.L = True



    def spawn(self, Map):
        """Permet de faire apparaitre nos monstre dans le niveau"""
        a = True
        while a:
            b = c = x = y = 0
            self.x = random.randint(0, 72)*20
            self.y = random.randint(0, 35)*20
            self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
            for y in range(fen_height//20):
                for x in range(fen_width//20):
                    b += 1
                    fond = Map[y][x]
                    if fond.nb == 1:
                        if fond.rect.colliderect(self.hitbox) == False:
                            c += 1
                    else:
                        c+= 1
            if b == c:
                a = False
            d = math.sqrt((perso.x - self.x)**2 + (perso.y - self.y)**2)
            if d < 100:
                a = True


    def Dammage(self):
        """DÃ©fini ce qui ce passe lors du contact entre un monstre et le personnage"""
        self.alea = random.randint(-10, 10)
        self.crit = random.randint(0, 100)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        Hitbox = self.hitbox

        if Hitbox.colliderect(perso.hitbox):
            if self.crit > 95:
                perso.pv -= self.atk * 2
            else:
                perso.pv -= self.atk + ((self.atk // 100) * self.alea)
            Son_perso_toucher.play()
            if self.U:
                perso.y -= perso.height
            elif self.D:
                perso.y += perso.height
            elif self.R:
                perso.x += perso.width
            elif self.L:
                perso.x -= perso.width


    def mort(self):
        """DÃ©fini ce qui ce passe lors de la mort du monstre"""
        Xp = (self.life//50) + (self.atk//4) + self.vel
        perso.xp += Xp * 2
        Or = (self.life//70) + (self.atk//6) + self.vel
        perso.gold += Or
        perso.pv += perso.life // 20
        if perso.pv > perso.life:
            perso.pv = perso.life







class Boss_final():
    """Classe du boss final !"""

    def __init__(self, life, atk, vel):
        """Prends en paramÃ¨tre la vie du boss int(life), l'attaque du boss int(atk), sa vitesse int(vel)"""
        self.x = 100
        self.y = 100
        self.width = 40
        self.height = 40
        self.life = life
        self.pv = self.life
        self.atk = atk
        self.vel = vel
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.U = False
        self.R = False
        self.D = False
        self.L = False
        self.patern = 0
        self.rect = pygame.Rect(self.x - 25, self.y - 500, 100, 500)
        self.rect2 = pygame.Rect(self.x - 25, self.y - 500, 100, 500)
        self.rect3 = pygame.Rect(self.x - 25, self.y - 500, 100, 500)
        self.rect4 = pygame.Rect(self.x - 25, self.y - 500, 100, 500)
        self.X1 = 0
        self.X2 = 0
        self.Y1 = 0
        self.Y2 = 0
        self.b = 0
        self.c = 0
        self.son = 0
        self.alea = 0
        self.crit = 0


    def draw(self):
        """MÃ©thode qui permet l'affichage du boss"""
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.U:
            fen.blit(sprite_boss_U, (self.x - 5, self.y - 5))
        elif self.R:
            fen.blit(sprite_boss_R, (self.x - 5, self.y - 5))
        elif self.L:
            fen.blit(sprite_boss_L, (self.x - 5, self.y - 5))
        elif self.D:
            fen.blit(sprite_boss_D, (self.x - 5, self.y - 5))

        pygame.draw.rect(fen, (200, 0, 0), (self.x - (self.life //10) + self.width //2, self.y - 10, self.life // 5, 4))
        pygame.draw.rect(fen, (0, 200, 0), (self.x - (self.life //10) + self.width //2, self.y - 10, self.pv // 5, 4))


    def move(self, projectiles_list):
        """MÃ©thode dÃ©finissant le mouvement du boss, ainsi que son parterne d'attaque"""
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        fixX = self.x - perso.x
        fixY = self.y - perso.y
        a = random.randint(0, 1)

        if self.patern < 150:
            if a == 0:
                if fixX <0:
                    self.x += self.vel
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= self.vel
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += self.vel
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= self.vel
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
            else:
                if fixY <0:
                    self.y += self.vel
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= self.vel
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += self.vel
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= self.vel
                        self.U = False
                        self.R = False
                        self.D = False
                        self.L = True

        elif self.patern < 155:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)

        elif self.patern < 160:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 160], (self.X1, self.Y1 - 48))

        elif self.patern < 175:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 160], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 180:
            self.son = 0
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)

        elif self.patern < 185:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 185], (self.X1, self.Y1 - 48))

        elif self.patern < 200:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 185], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 205:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            self.son = 0

        elif self.patern < 210:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 210], (self.X1, self.Y1 - 48))

        elif self.patern < 225:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 210], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 230:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            self.son = 0

        elif self.patern < 235:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 235], (self.X1, self.Y1 - 48))

        elif self.patern < 250:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 235], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 255:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            self.son = 0

        elif self.patern < 260:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 260], (self.X1, self.Y1 - 48))

        elif self.patern < 265:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 260], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 580:
            self.son = 0
            if self.patern % 7 == 0:
                if fixX <0:
                    self.x += 40
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= 40
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += 40
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= 40
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
                if fixY <0:
                    self.y += 40
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= 40
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += 40
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= 40
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False

        elif self.patern < 600: #PrÃ©parations Ã  la premiÃ¨re grosse attaque
            if fixX < 0:
                self.rect = pygame.Rect(self.x + self.width, self.y - 25, 500, 100)
                self.X1 = (self.x + self.width)
                self.Y1 = (self.y - 25)
                pygame.draw.rect(fen, (255, 0, 0), self.rect, 2)

            elif fixX > 0:
                self.rect = pygame.Rect(self.x - 500, self.y - 25, 500, 100)
                self.X1 = (self.x - 500)
                self.Y1 = (self.y - 25)
                pygame.draw.rect(fen, (255, 0, 0), self.rect, 2)

            if fixY < 0:
                self.rect2 = pygame.Rect(self.x - 25, self.y + self.height, 100, 500)
                self.X2 = (self.x - 25)
                self.Y2 = (self.y + self.height)
                pygame.draw.rect(fen, (255, 0, 0), self.rect2, 2)

            elif fixY > 0:
                self.rect2 = pygame.Rect(self.x - 25, self.y - 500, 100, 500)
                self.X2 = (self.x - 25)
                self.Y2 = (self.y - 500)
                pygame.draw.rect(fen, (255, 0, 0), self.rect2, 2)

        elif self.patern < 690: #Attaque de zone
            if self.son == 0:
                Son_boss_atk1.play()
                self.son = 1
            fen.blit(sprite_boss_atk1_RL[self.patern - 600], (self.X1, self.Y1))
            fen.blit(sprite_boss_atk1_UD[self.patern - 600], (self.X2, self.Y2))
            if self.rect.colliderect(perso.hitbox) or self.rect2.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 990:
            self.son = 0
            if self.patern % 7 == 0:
                if fixX <0:
                    self.x += 40
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= 40
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += 40
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= 40
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
                if fixY <0:
                    self.y += 40
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= 40
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += 40
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= 40
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False

        elif self.patern < 1010: #PrÃ©parations Ã  la premiÃ¨re grosse attaque
            if fixX < 0:
                self.rect = pygame.Rect(self.x + self.width, self.y - 25, 500, 100)
                self.X1 = (self.x + self.width)
                self.Y1 = (self.y - 25)
                pygame.draw.rect(fen, (255, 0, 0), self.rect, 2)

            elif fixX > 0:
                self.rect = pygame.Rect(self.x - 500, self.y - 25, 500, 100)
                self.X1 = (self.x - 500)
                self.Y1 = (self.y - 25)
                pygame.draw.rect(fen, (255, 0, 0), self.rect, 2)

            if fixY < 0:
                self.rect2 = pygame.Rect(self.x - 25, self.y + self.height, 100, 500)
                self.X2 = (self.x - 25)
                self.Y2 = (self.y + self.height)
                pygame.draw.rect(fen, (255, 0, 0), self.rect2, 2)

            elif fixY > 0:
                self.rect2 = pygame.Rect(self.x - 25, self.y - 500, 100, 500)
                self.X2 = (self.x - 25)
                self.Y2 = (self.y - 500)
                pygame.draw.rect(fen, (255, 0, 0), self.rect2, 2)

        elif self.patern < 1100: #Attaque de zone
            if self.son == 0:
                Son_boss_atk1.play()
                self.son = 1
            fen.blit(sprite_boss_atk1_RL[self.patern - 1010], (self.X1, self.Y1))
            fen.blit(sprite_boss_atk1_UD[self.patern - 1010], (self.X2, self.Y2))
            if self.rect.colliderect(perso.hitbox) or self.rect2.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 1401: #Il te lance des projectiles !!!
            self.son = 0
            if self.patern % 7 == 0:
                if a == 0:
                    self.x = random.randint(0, 1540 - self.width)
                    self.y = perso.y
                    if math.sqrt((self.x - perso.x)**2 + (self.y - perso.y)**2) < 150:
                        while math.sqrt((self.x - perso.x)**2 + (self.y - perso.y)**2) < 150:
                            self.x = random.randint(0, 1540 - self.width)
                elif a == 1:
                    self.y = random.randint(0, 800 - self.height)
                    self.x = perso.x
                    if math.sqrt((self.x - perso.x)**2 + (self.y - perso.y)**2) < 150:
                        while math.sqrt((self.x - perso.x)**2 + (self.y - perso.y)**2) < 150:
                            self.y = random.randint(0, 800 - self.height)

                if fixY <0:
                    Son_projectile.play()
                    pro = Projectile(self.x, self.y, self.vel * 2, self.atk, 'Down')
                    projectiles_list.append(pro)
                elif fixY >0:
                    Son_projectile.play()
                    pro = Projectile(self.x, self.y, self.vel * 2, self.atk, 'Up')
                    projectiles_list.append(pro)

                if fixX <0:
                    Son_projectile.play()
                    pro = Projectile(self.x, self.y, self.vel * 2, self.atk, 'Right')
                    projectiles_list.append(pro)
                elif fixX >0:
                    Son_projectile.play()
                    pro = Projectile(self.x, self.y, self.vel * 2, self.atk, 'Left')
                    projectiles_list.append(pro)

        elif self.patern < 1501:
            if a == 0:
                if fixX <0:
                    self.x += self.vel
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= self.vel
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += self.vel
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= self.vel
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
            else:
                if fixY <0:
                    self.y += self.vel
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= self.vel
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += self.vel
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= self.vel
                        self.U = False
                        self.R = False
                        self.D = False
                        self.L = True

        elif self.patern < 1646: #Il t'attire !
            if a == 0:
                if fixX <0:
                    self.x += self.vel
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= self.vel
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += self.vel
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= self.vel
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
            else:
                if fixY <0:
                    self.y += self.vel
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= self.vel
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += self.vel
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= self.vel
                        self.U = False
                        self.R = False
                        self.D = False
                        self.L = True

            self.rect = pygame.Rect(self.x + self.width, (self.y - 75) + self.height // 2, 1000, 150)

            self.rect2 = pygame.Rect(self.x - 1000, (self.y - 75) + self.height // 2, 1000, 150)

            self.rect3 = pygame.Rect((self.x - 75) + self.width // 2, self.y + self.height, 150, 1000)

            self.rect4 = pygame.Rect((self.x - 75) + self.width // 2, self.y - 1000, 150, 1000)

            self.c = 0
            self.b = (self.patern - 900) - self.c
            while self.b > 6:
                self.c += 7
                self.b = (self.patern - 900) - self.c

            fen.blit(sprite_boss_atk3_R[self.b], (self.x + self.width, (self.y - 75) + self.height // 2))
            fen.blit(sprite_boss_atk3_L[self.b], (self.x - 1000, (self.y - 75) + self.height // 2))
            fen.blit(sprite_boss_atk3_D[self.b], ((self.x - 75) + self.width // 2, self.y + self.height))
            fen.blit(sprite_boss_atk3_U[self.b], ((self.x - 75) + self.width // 2, self.y - 1000))

            if self.rect.colliderect(perso.hitbox):
                perso.x -= self.vel
            elif self.rect2.colliderect(perso.hitbox):
                perso.x += self.vel
            elif self.rect3.colliderect(perso.hitbox):
                perso.y -= self.vel
            elif self.rect4.colliderect(perso.hitbox):
                perso.y += self.vel

        elif self.patern < 1666: #PrÃ©parations Ã  la premiÃ¨re grosse attaque
            if fixX < 0:
                self.rect = pygame.Rect(self.x + self.width, self.y - 25, 500, 100)
                self.X1 = (self.x + self.width)
                self.Y1 = (self.y - 25)
                pygame.draw.rect(fen, (255, 0, 0), self.rect, 2)

            elif fixX > 0:
                self.rect = pygame.Rect(self.x - 500, self.y - 25, 500, 100)
                self.X1 = (self.x - 500)
                self.Y1 = (self.y - 25)
                pygame.draw.rect(fen, (255, 0, 0), self.rect, 2)

            if fixY < 0:
                self.rect2 = pygame.Rect(self.x - 25, self.y + self.height, 100, 500)
                self.X2 = (self.x - 25)
                self.Y2 = (self.y + self.height)
                pygame.draw.rect(fen, (255, 0, 0), self.rect2, 2)

            elif fixY > 0:
                self.rect2 = pygame.Rect(self.x - 25, self.y - 500, 100, 500)
                self.X2 = (self.x - 25)
                self.Y2 = (self.y - 500)
                pygame.draw.rect(fen, (255, 0, 0), self.rect2, 2)

        elif self.patern < 1756: #Attaque de zone
            if self.son == 0:
                Son_boss_atk1.play()
                self.son = 1
            fen.blit(sprite_boss_atk1_RL[self.patern - 1666], (self.X1, self.Y1))
            fen.blit(sprite_boss_atk1_UD[self.patern - 1666], (self.X2, self.Y2))
            if self.rect.colliderect(perso.hitbox) or self.rect2.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)


        if self.patern > 1756:
            self.patern = 0
            self.son = 0
        else:
            self.patern += 1

        return projectiles_list



    def Dammage(self):
        """MÃ©thode permettant de dÃ©finir ce qui se passe quand le joueur entre en collision avec le boss"""
        self.alea = random.randint(-10, 10)
        self.crit = random.randint(0, 100)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        Hitbox = self.hitbox

        if Hitbox.colliderect(perso.hitbox):
            if self.crit > 95:
                perso.pv -= self.atk * 2
            else:
                perso.pv -= self.atk + ((self.atk // 100) * self.alea)
            Son_perso_toucher.play()
            if self.U:
                perso.y -= self.height
            elif self.D:
                perso.y += self.height
            elif self.R:
                perso.x += self.width
            elif self.L:
                perso.x -= self.width


    def mort(self, Fin, tps):
        """MÃ©thode permettant de dÃ©finir ce qui ce passe Ã  la mort du boss"""
        tps = tps // 30
        Fin = True
        return Fin, tps

boss_final = Boss_final(3000, 70, 7)






class Boss(Boss_final):
    """Classe de nos boss !"""

    def __init__(self, life, atk, vel, nb):
        """Prends en paramÃ¨tre la vie du boss int(life), l'attaque du boss int(atk), sa vitesse int(vel)"""
        Boss_final.__init__(self, life, atk, vel)
        self.nb = nb


    def move(self, projectiles_list):
        """MÃ©thode dÃ©finissant le mouvement du boss, ainsi que son parterne d'attaque"""
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        fixX = self.x - perso.x
        fixY = self.y - perso.y
        a = random.randint(0, 1)

        if self.patern < 150: #Deplacement classique
            if a == 0:
                if fixX <0:
                    self.x += self.vel
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= self.vel
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += self.vel
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= self.vel
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
            else:
                if fixY <0:
                    self.y += self.vel
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= self.vel
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += self.vel
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= self.vel
                        self.U = False
                        self.R = False
                        self.D = False
                        self.L = True

        elif self.patern < 180: #PrÃ©parations Ã  la premiÃ¨re grosse attaque
            if fixX < 0:
                self.rect = pygame.Rect(self.x + self.width, self.y - 25, 500, 100)
                self.X1 = (self.x + self.width)
                self.Y1 = (self.y - 25)
                pygame.draw.rect(fen, (255, 0, 0), self.rect, 2)

            elif fixX > 0:
                self.rect = pygame.Rect(self.x - 500, self.y - 25, 500, 100)
                self.X1 = (self.x - 500)
                self.Y1 = (self.y - 25)
                pygame.draw.rect(fen, (255, 0, 0), self.rect, 2)

            if fixY < 0:
                self.rect2 = pygame.Rect(self.x - 25, self.y + self.height, 100, 500)
                self.X2 = (self.x - 25)
                self.Y2 = (self.y + self.height)
                pygame.draw.rect(fen, (255, 0, 0), self.rect2, 2)

            elif fixY > 0:
                self.rect2 = pygame.Rect(self.x - 25, self.y - 500, 100, 500)
                self.X2 = (self.x - 25)
                self.Y2 = (self.y - 500)
                pygame.draw.rect(fen, (255, 0, 0), self.rect2, 2)

        elif self.patern < 270: #Attaque de zone
            if self.son == 0:
                Son_boss_atk1.play()
                self.son = 1
            fen.blit(sprite_boss_atk1_RL[self.patern - 180], (self.X1, self.Y1))
            fen.blit(sprite_boss_atk1_UD[self.patern - 180], (self.X2, self.Y2))
            if self.rect.colliderect(perso.hitbox) or self.rect2.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 430:
            self.son = 0
            if a == 0:
                if fixX <0:
                    self.x += self.vel
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= self.vel
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += self.vel
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= self.vel
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
            else:
                if fixY <0:
                    self.y += self.vel
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= self.vel
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += self.vel
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= self.vel
                        self.U = False
                        self.R = False
                        self.D = False
                        self.L = True

        elif self.patern < 570: #Avance sacadÃ©e et rapide : attaque qui surprends
            if self.patern % 7 == 0:
                if fixX <0:
                    self.x += 40
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= 40
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += 40
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= 40
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
                if fixY <0:
                    self.y += 40
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= 40
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += 40
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= 40
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False

        elif self.patern < 720: #Marche classique
            if a == 0:
                if fixX <0:
                    self.x += self.vel
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= self.vel
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += self.vel
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= self.vel
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
            else:
                if fixY <0:
                    self.y += self.vel
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= self.vel
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += self.vel
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= self.vel
                        self.U = False
                        self.R = False
                        self.D = False
                        self.L = True

        elif self.patern < 735: #MÃ©tÃ©ores !
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)

        elif self.patern < 745:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 735], (self.X1, self.Y1 - 48))

        elif self.patern < 750:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 735], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 765:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            self.son = 0

        elif self.patern < 775:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 765], (self.X1, self.Y1 - 48))

        elif self.patern < 780:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 765], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 795:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            self.son = 0

        elif self.patern < 805:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 795], (self.X1, self.Y1 - 48))

        elif self.patern < 810:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 795], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 825:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            self.son = 0

        elif self.patern < 835:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 825], (self.X1, self.Y1 - 48))

        elif self.patern < 840:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 825], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 855:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            self.son = 0

        elif self.patern < 865:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 855], (self.X1, self.Y1 - 48))

        elif self.patern < 870:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 855], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 885:
            self.X1 = perso.x - 16
            self.Y1 = perso.y - 16
            self.rect = pygame.Rect(self.X1, self.Y1, 48, 48)
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            self.son = 0

        elif self.patern < 895:
            pygame.draw.rect(fen, (255, 0, 0), self.rect, 1)
            fen.blit(sprite_boss_atk2[self.patern - 885], (self.X1, self.Y1 - 48))

        elif self.patern < 900:
            if self.son == 0:
                Son_boss_atk2.play()
                self.son = 1
            fen.blit(sprite_boss_atk2[self.patern - 885], (self.X1, self.Y1 - 48))
            if self.rect.colliderect(perso.hitbox):
                perso.pv -= (self.atk // 5)

        elif self.patern < 1110: #Il t'attire !
            self.son = 0
            if a == 0:
                if fixX <0:
                    self.x += self.vel
                    self.U = False
                    self.R = True
                    self.D = False
                    self.L = False
                elif fixX >0:
                    self.x -= self.vel
                    self.U = False
                    self.R = False
                    self.D = False
                    self.L = True
                else:
                    if fixY <0:
                        self.y += self.vel
                        self.U = False
                        self.R = False
                        self.D = True
                        self.L = False
                    elif fixY >0:
                        self.y -= self.vel
                        self.U = True
                        self.R = False
                        self.D = False
                        self.L = False
            else:
                if fixY <0:
                    self.y += self.vel
                    self.U = False
                    self.R = False
                    self.D = True
                    self.L = False
                elif fixY >0:
                    self.y -= self.vel
                    self.U = True
                    self.R = False
                    self.D = False
                    self.L = False
                else:
                    if fixX <0:
                        self.x += self.vel
                        self.U = False
                        self.R = True
                        self.D = False
                        self.L = False
                    elif fixX >0:
                        self.x -= self.vel
                        self.U = False
                        self.R = False
                        self.D = False
                        self.L = True

            self.rect = pygame.Rect(self.x + self.width, (self.y - 75) + self.height // 2, 1000, 150)

            self.rect2 = pygame.Rect(self.x - 1000, (self.y - 75) + self.height // 2, 1000, 150)

            self.rect3 = pygame.Rect((self.x - 75) + self.width // 2, self.y + self.height, 150, 1000)

            self.rect4 = pygame.Rect((self.x - 75) + self.width // 2, self.y - 1000, 150, 1000)

            self.c = 0
            self.b = (self.patern - 900) - self.c
            while self.b > 6:
                self.c += 7
                self.b = (self.patern - 900) - self.c

            fen.blit(sprite_boss_atk3_R[self.b], (self.x + self.width, (self.y - 75) + self.height // 2))
            fen.blit(sprite_boss_atk3_L[self.b], (self.x - 1000, (self.y - 75) + self.height // 2))
            fen.blit(sprite_boss_atk3_D[self.b], ((self.x - 75) + self.width // 2, self.y + self.height))
            fen.blit(sprite_boss_atk3_U[self.b], ((self.x - 75) + self.width // 2, self.y - 1000))

            if self.rect.colliderect(perso.hitbox):
                perso.x -= self.vel
            elif self.rect2.colliderect(perso.hitbox):
                perso.x += self.vel
            elif self.rect3.colliderect(perso.hitbox):
                perso.y -= self.vel
            elif self.rect4.colliderect(perso.hitbox):
                perso.y += self.vel


        elif self.patern < 1410: #Il te lance des projectiles !!!
            if self.patern % 10 == 0:
                if a == 0:
                    self.x = random.randint(0, 1540 - self.width)
                    self.y = perso.y
                    if math.sqrt((self.x - perso.x)**2 + (self.y - perso.y)**2) < 150:
                        while math.sqrt((self.x - perso.x)**2 + (self.y - perso.y)**2) < 150:
                            self.x = random.randint(0, 1540 - self.width)
                elif a == 1:
                    self.y = random.randint(0, 800 - self.height)
                    self.x = perso.x
                    if math.sqrt((self.x - perso.x)**2 + (self.y - perso.y)**2) < 150:
                        while math.sqrt((self.x - perso.x)**2 + (self.y - perso.y)**2) < 150:
                            self.y = random.randint(0, 800 - self.height)

                if fixY <0:
                    Son_projectile.play()
                    pro = Projectile(self.x, self.y, self.vel * 2, self.atk, 'Down')
                    projectiles_list.append(pro)
                elif fixY >0:
                    Son_projectile.play()
                    pro = Projectile(self.x, self.y, self.vel * 2, self.atk, 'Up')
                    projectiles_list.append(pro)

                if fixX <0:
                    Son_projectile.play()
                    pro = Projectile(self.x, self.y, self.vel * 2, self.atk, 'Right')
                    projectiles_list.append(pro)
                elif fixX >0:
                    Son_projectile.play()
                    pro = Projectile(self.x, self.y, self.vel * 2, self.atk, 'Left')
                    projectiles_list.append(pro)


        self.patern += 1
        if self.patern > 270 and self.nb == 1:
            self.patern = 0
        elif self.patern > 570 and self.nb == 2:
            self.patern = 0
        elif self.patern > 899 and self.nb == 3:
            self.patern = 0
        elif self.patern > 1109 and self.nb == 4:
            self.patern = 0
        elif self.patern > 1410 and self.nb == 5:
            self.patern = 0

        return projectiles_list



    def mort(self, boss, nb_arme, niveau_save):
        """MÃ©thode permettant de dÃ©finir ce qui ce pass lors de la mort du boss"""
        boss = False
        nb_arme = random.randint(0, 19)
        if self.nb == 1:
            perso.xp += 80
            perso.gold += 50
            niveau_save = 6

        elif self.nb == 2:
            perso.xp += 128
            perso.gold += 80
            niveau_save = 11

        elif self.nb == 3:
            perso.xp += 205
            perso.gold += 128
            niveau_save = 16

        elif self.nb == 4:
            perso.xp += 328
            perso.gold += 205
            niveau_save = 21

        elif self.nb == 5:
            perso.xp += 525
            perso.gold += 258
            niveau_save = 26

        perso.pv = perso.life

        return boss, nb_arme, niveau_save


boss = True
boss1 = Boss(500, 20, 3, 1)
boss2 = Boss(800, 30, 3, 2)
boss3 = Boss(1200, 40, 4, 3)
boss4 = Boss(1500, 50, 5, 4)
boss5 = Boss(2000, 60, 6, 5)









class button():
    """Classe crÃ©ant les boutons"""

    def __init__(self, color, x,y,width,height, text=''):
        """Prends en paramÃ¨tre sa couleur initial, x, y, sa largeur (width), sa hauteur (height) et le texte que tu souhaite"""
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        if self.text == 'Life' or self.text == 'Strengh' or self.text == 'Speed':
            self.sprite1 = Mbutton
            self.sprite2 = Mbutton2
        else:
            self.sprite1 = Button
            self.sprite2 = Button2
        self.etat = 0


    def draw(self,win,size,outline=None):
        """MÃ©thode permettant d'afficher nos boutons. Prends en paramÃ¨tre la surface (win), la taille de la police (size) et la bordure(outline).
        Pour la bordure, ne rien mettre pour ne pas en avoir, sinon mettre un int pour sa taille."""
        if self.etat == 0:
            win.blit(self.sprite1, (self.x, self.y))
        elif self.etat == 1:
            win.blit(self.sprite2, (self.x, self.y))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', size)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


    def isOver(self, pos):
        """Permet de savoir si la sourie est sur un bouton. Prends en paramÃ¨tre les coordonÃ©es de la sourie dans un tuple (x, y) (pos)"""
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


    def action(self, pos, col1, col2, arme = None):
        """Permet de dÃ©finir l'action du clique sur un bouton. Prends en paramÃ¨tre les coordonÃ©es de la sourie dans un tuple (x, y) (pos), col1 et col2 qui sont des couleurs.
        col1 est la couleur de base, et col2 est la couleur quand la sourie est sur le bouton. Prends aussi l'arme (arme) pour le changement. Sinon, laisser vide"""
        global fenetre, run, run2, Mobs, nb_mob, nb_niveaux, boss, boss1, boss2, boss3, boss4, boss5, perso, boss_final, niveau_save, nb_mort, tps, projectiles_list, Map
        if self.isOver(pos):
            key2 = pygame.mouse.get_pressed()
            if key2[0] == 1:
                if self.text == 'Play':
                    Son_bouton.play()
                    fenetre = 1


                elif self.text == 'New Game':
                    Son_bouton.play()
                    perso = Personnage(arm1)
                    nb_niveaux = 0
                    niveau_save = 0
                    run = True
                    run2 = False
                    nb_mort = 0
                    tps = 0


                elif self.text == 'Continue':
                    Son_bouton.play()
                    perso = Personnage(arm1)
                    with open('Save_game', 'rb') as fichier:
                        mon_depickler = pickle.Unpickler(fichier)
                        save = mon_depickler.load()

                    perso.arme = save[0]
                    perso.lvl = save[1]
                    perso.xp = save[2]
                    perso.lvl_life = save[3]
                    perso.lvl_speed = save[4]
                    perso.lvl_strengh = save[5]
                    perso.gold = save[6]
                    nb_niveaux = save[7]
                    niveau_save = save[8]
                    nb_mort = save[9]
                    tps = save[10]
                    if nb_niveaux == 5 or nb_niveaux == 10 or nb_niveaux == 15 or nb_niveaux == 20 or nb_niveaux == 25 or nb_niveaux == 30:
                        nb_niveaux -= 1

                    elif nb_niveaux < niveau_save:
                        nb_niveaux = niveau_save

                    perso.life = Lvl_life[perso.lvl_life]
                    perso.pv = perso.life
                    perso.vel = Lvl_speed[perso.lvl_speed]
                    perso.strengh = Lvl_strengh[perso.lvl_strengh]
                    perso.dommage = perso.arme.atk
                    perso.atk = perso.dommage + perso.strengh
                    run = True
                    run2 = False


                elif self.text == 'Options':
                    Son_bouton.play()
                    fenetre = 2


                elif self.text == 'Back':
                    Son_bouton.play()
                    fenetre = 0


                elif self.text == 'Quit':
                    Son_bouton.play()
                    run = False
                    run2 = False


                elif self.text == 'Life':
                    Son_bouton.play()
                    perso.lvl_up('Vie')


                elif self.text == 'Strengh':
                    Son_bouton.play()
                    perso.lvl_up('Force')


                elif self.text == 'Speed':
                    Son_bouton.play()
                    perso.lvl_up('Vitesse')


                elif self.text == 'Level up':
                    Son_bouton.play()
                    boss = 1
                    perso.x = 740
                    perso.y = 400
                    Mobs = []
                    projectiles_list = []
                    nb_niveaux += 1

                    if nb_niveaux != 5 and nb_niveaux != 10 and nb_niveaux != 15 and nb_niveaux != 20 and nb_niveaux != 25 and nb_niveaux != 30:
                        Map = Creation_mur(Map)
                    else:
                        Map = salle_boss(Map)
                        perso.pv = perso.life


                    if nb_niveaux < 5:
                        nb_mob = random.randint(2, 6)

                    elif nb_niveaux == 5:
                        nb_mob = 1
                        boss1 = Boss(500, 20, 3, 1)

                    elif nb_niveaux < 10:
                        nb_mob = random.randint(2, 8)

                    elif nb_niveaux == 10:
                        nb_mob = 1
                        boss2 = Boss(700, 30, 3, 2)

                    elif nb_niveaux < 15:
                        nb_mob = random.randint(4, 10)

                    elif nb_niveaux == 15:
                        nb_mob = 1
                        boss3 = Boss(900, 40, 4, 3)

                    elif nb_niveaux < 20:
                        nb_mob = random.randint(6, 13)

                    elif nb_niveaux == 20:
                        nb_mob = 1
                        boss4 = Boss(1200, 50, 5, 4)

                    elif nb_niveaux < 25:
                        nb_mob = random.randint(8, 16)

                    elif nb_niveaux == 25:
                        nb_mob = 1
                        boss5 = Boss(1500, 60, 6, 5)

                    elif nb_niveaux == 30:
                        nb_mob = 1
                        boss_final = Boss_final(3000, 70, 7)

                    else:
                        nb_mob = random.randint(10, 20)

                    if nb_niveaux != 5 and nb_niveaux != 10 and nb_niveaux != 15 and nb_niveaux != 20 and nb_niveaux != 25 and nb_niveaux != 30:
                        for i in range(nb_mob):
                            mob = Monstre(nb_niveaux)
                            Mobs.append(mob)
                        for mob in Mobs:
                            mob.spawn(Map)
                    raffraichissement(test_pos, nb_mob, test_collid)


                elif self.text == 'Play again':
                    Son_bouton.play()
                    nb_mort += 1
                    boss = 1
                    perso.x = 740
                    perso.y = 400
                    perso.pv = perso.life
                    Mobs = []
                    projectiles_list = []
                    nb_niveaux -= 1
                    if nb_niveaux < niveau_save:
                        nb_niveaux = niveau_save
                    elif nb_niveaux == 5 and nb_niveaux == 10 and nb_niveaux == 15 and nb_niveaux == 20 and nb_niveaux == 25 and nb_niveaux == 30:
                        nb_niveaux -= 1

                    if nb_niveaux != 5 and nb_niveaux != 10 and nb_niveaux != 15 and nb_niveaux != 20 and nb_niveaux != 25 and nb_niveaux != 30:
                        Map = Creation_mur(Map)
                    else:
                        Map = salle_boss(Map)

                    if nb_niveaux < 5:
                        nb_mob = random.randint(2, 6)

                    elif nb_niveaux == 5:
                        nb_mob = 1
                        boss1 = Boss(500, 20, 3, 1)

                    elif nb_niveaux < 10:
                        nb_mob = random.randint(2, 8)

                    elif nb_niveaux == 10:
                        nb_mob = 1
                        boss2 = Boss(700, 30, 3, 2)

                    elif nb_niveaux < 15:
                        nb_mob = random.randint(4, 10)

                    elif nb_niveaux == 15:
                        nb_mob = 1
                        boss3 = Boss(900, 40, 4, 3)

                    elif nb_niveaux < 20:
                        nb_mob = random.randint(6, 13)

                    elif nb_niveaux == 20:
                        nb_mob = 1
                        boss4 = Boss(1200, 50, 5, 4)

                    elif nb_niveaux < 25:
                        nb_mob = random.randint(8, 16)

                    elif nb_niveaux == 25:
                        nb_mob = 1
                        boss5 = Boss(1500, 60, 6, 5)

                    elif nb_niveaux < 30:
                        nb_mob = random.randint(10, 20)

                    elif nb_niveaux == 30:
                        nb_mob = 1
                        boss_final = Boss_final(3000, 70, 7)

                    if nb_niveaux != 5 and nb_niveaux != 10 and nb_niveaux != 15 and nb_niveaux != 20 and nb_niveaux != 25 and nb_niveaux != 30:
                        for i in range(nb_mob):
                            mob = Monstre(nb_niveaux)
                            Mobs.append(mob)
                        for mob in Mobs:
                            mob.spawn(Map)
                    raffraichissement(test_pos, nb_mob, test_collid)


                elif self.text == 'Upgrade':
                    Son_bouton.play()
                    arme.upgrade()
                    perso.dommage = arme.atk
                    perso.atk = perso.dommage + perso.strengh

                elif self.text == 'Yes':
                    Son_bouton.play()
                    perso.change(arme, 0)

                elif self.text == 'No':
                    Son_bouton.play()
                    perso.change(arme, 1)

            self.etat = 1

        else:
            self.etat = 0


But1 = button((0, 200, 0), 860, 440, 200, 40, 'Play')
But1_1 = button((0, 200, 0), 750, 490, 200, 40, 'New Game')
But1_2 = button((0, 200, 0), 970, 490, 200, 40, 'Continue')
But1_3 = button((0, 200, 0), 860, 590, 200, 40, 'Back')
But2 = button((0, 200, 0), 860, 540, 200, 40, 'Options')
But2_1 = button((0, 200, 0), 860, 740, 200, 40, 'Back')
But3 = button((0, 200, 0), 860, 640, 200, 40, 'Quit')
But3_1 = button((0, 0, 255), 970, 600, 200, 40, 'Quit')
But3_2 = button((0, 0, 255), 970, 560, 200, 40, 'Quit')
But3_3 = button((0, 0, 255), 970, 560, 200, 40, 'Quit')
But4 = button((0, 0, 255), 800, 540, 100, 40, 'Life')
But5 = button((0, 0, 255), 910, 540, 100, 40, 'Strengh')
But6 = button((0, 0, 255), 1020, 540, 100, 40, 'Speed')
But7 = button((0, 0, 255), 750, 560, 200, 40, 'Play again')
But8 = button((0, 0, 255), 750, 560, 200, 40, 'Level up')
But9 = button((0, 0, 255), 1680, 640, 200, 40, 'Upgrade')
But10 = button((0, 0, 255), 750, 600, 200, 40, 'Yes')
But11 = button((0, 0, 255), 970, 600, 200, 40, 'No')



#Fonctions

def salle_boss(Map):
    """Fonction permettant de crÃ©er la salle pour les boss"""
    Sol_list = []
    Map = [[0 for j in range(fen_width // 20)] for i in range(fen_height // 20)]

    for y in range((fen_height//20)):
        for x in range(fen_width//20):
            Sol_list.append([x * 20, y * 20])

    for pos in Sol_list:
        fond = Fonds(pos[0], pos[1], 0)
        Map[pos[1]//20][pos[0]//20] = fond

    return Map



def Creation_mur(Map):
    """Fonction permettant de crÃ©er les niveaux alÃ©atoirement"""
    Mur_list = []
    Sol_list = []

    for y in range((fen_height//20)):
        for x in range(fen_width//20):
            Mur_list.append([x * 20, y * 20])
    Dest_list = []
    dest_x = 740
    dest_y = 400
    for deplacement in range(Corridor_size):
        Dest_list.append([dest_x, dest_y])

        rand = random.randint(0, 1) #Variable alÃ©atoire qui dÃ©termine si le destroyeur ce dÃ©place en x ou en y

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


        if dest_x > fen_width or dest_x < 0: #Reste dans notre Ã©cran !
            dest_x = 740
            dest_y = 400
        if dest_y > fen_height or dest_y < 0:
            dest_x = 740
            dest_y = 400

    #Comparaison des listes et destructions des points commun
    for pos_dest in Dest_list:
        for pos_mur in Mur_list:
            if pos_mur == pos_dest:
                Sol_list.append(pos_mur)
                Mur_list.remove(pos_mur)


    #CrÃ©ation des sols
    for pos in Sol_list:
        fond = Fonds(pos[0], pos[1], 0)
        Map[pos[1]//20][pos[0]//20] = fond

    #CrÃ©ation des murs
    for pos in Mur_list:
        fond = Fonds(pos[0], pos[1], 1)
        Map[pos[1]//20][pos[0]//20] = fond

    return Map




def update_boss(boss0, nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save):
    """Fonction permettant de raffraichir le jeu durant les combats de boss. Prends un boss en paramÃ¨tre"""
    x = y = 0
    for y in range(fen_height // 20):
        for x in range(fen_width // 20):
            fond = Map[y][x]
            fond.draw(fen)
        x = 0

    if boss0.pv <= 0:
        if boss0.life == 3000:
            Fin, tps = boss0.mort(Fin, tps)
        else:
            boss, nb_arme, niveau_save = boss0.mort(boss, nb_arme, niveau_save)
            nb_mob = 0

    projectiles_list = boss0.move(projectiles_list)
    boss0.Dammage()
    boss0.draw()

    for pro in projectiles_list:
        pro.move()
        pro.attaque()
        pro.draw()

    if key[pygame.K_w] or key[pygame.K_z] or key[pygame.K_UP]:
        perso.move(0)
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        perso.move(1)
    elif key[pygame.K_s] or key[pygame.K_DOWN]:
        perso.move(2)
    elif key[pygame.K_a] or key[pygame.K_q] or key[pygame.K_LEFT]:
        perso.move(3)

    perso.Dammage()
    perso.draw()

    pygame.display.update()

    return nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save



def raffraichissement(test_pos, nb_mob, test_collid, Fin = 0, tps = 0, projectiles_list = [], boss = False, nb_arme = 0, niveau_save = 0):
    """Fonction raffraichissant le jeu"""

    Son = 0

    if nb_niveaux == 5:
        nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save = update_boss(boss1, nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save)

    elif nb_niveaux == 10:
        nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save = update_boss(boss2, nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save)

    elif nb_niveaux == 15:
        nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save = update_boss(boss3, nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save)

    elif nb_niveaux == 20:
        nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save = update_boss(boss4, nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save)

    elif nb_niveaux == 25:
        nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save = update_boss(boss5, nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save)

    elif nb_niveaux == 30:
        nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save = update_boss(boss_final, nb_mob, Fin, tps, projectiles_list, boss, nb_arme, niveau_save)

    else:
        x = y = 0
        for y in range(fen_height // 20):
            for x in range(fen_width // 20):
                fond = Map[y][x]
                fond.draw(fen)
            x = 0

        if key[pygame.K_w] or key[pygame.K_z] or key[pygame.K_UP]:
            perso.move(0)
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            perso.move(1)
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            perso.move(2)
        elif key[pygame.K_a] or key[pygame.K_q] or key[pygame.K_LEFT]:
            perso.move(3)

        if (perso.x, perso.y) == test_pos:
            test_collid += 1
        else:
            test_pos = (perso.x, perso.y)
            test_collid = 0

        if test_collid >= 180:
            perso.x = 780
            perso.y = 400


        for mob in Mobs:
            if mob.pv <= 0:
                mob.mort()
                Mobs.remove(mob)
                nb_mob -= 1
            elif mob.x < 0 or mob.x > 1540  or mob.y < 0 or mob.y > 800:
                mob.mort()
                Mobs.remove(mob)
                nb_mob -= 1
            mob.move(Map)
            mob.Dammage()
            mob.draw()

        perso.Dammage()
        perso.draw()

    return nb_mob, Son, test_collid, test_pos, Fin, tps, projectiles_list, boss, nb_arme, niveau_save




def menu(fenetre):
    """Fonction permettant de mettre Ã  jour le menu. Prends en paramÃ¨tre la fenÃªtre int(fenetre) pour savoir qu'elle partie du menu afficher"""
    string = "Press F4 to switch in full screen !"
    font = pygame.font.SysFont("comicsans", 30)
    text = font.render(string, 1, (255, 255, 255))
    fen.blit(text, (10, 10))

    if fenetre == 0:
        But1.action(pos, (0, 200, 0), (0, 255, 0))
        But2.action(pos, (0, 200, 0), (0, 255, 0))
        But3.action(pos, (0, 200, 0), (0, 255, 0))
        But1.draw(fen, 30)
        But2.draw(fen, 30)
        But3.draw(fen, 30)


    elif fenetre == 1:
        But1_1.action(pos, (0, 200, 0), (0, 255, 0))
        But1_2.action(pos, (0, 200, 0), (0, 255, 0))
        But1_3.action(pos, (0, 200, 0), (0, 255, 0))
        But1_1.draw(fen, 30)
        But1_2.draw(fen, 30)
        But1_3.draw(fen, 30)


    elif fenetre == 2:
        But2_1.action(pos, (0, 200, 0), (0, 255, 0))
        But2_1.draw(fen, 30)

        font1 = pygame.font.SysFont("comicsans", 60)
        text1 = font1.render("Controls", 1, (255, 255, 255))
        fen.blit(text1, (960 - (text1.get_width()/2), 340))

        font2 = pygame.font.SysFont("comicsans", 40)
        text2 = font2.render("Up : W or Z", 1, (255, 255, 255))
        fen.blit(text2, (960 - (text2.get_width()/2), 390))

        font3 = pygame.font.SysFont("comicsans", 40)
        text3 = font3.render("Down : S", 1, (255, 255, 255))
        fen.blit(text3, (960 - (text3.get_width()/2), 440))

        font4 = pygame.font.SysFont("comicsans", 40)
        text4 = font4.render("Right : A or D", 1, (255, 255, 255))
        fen.blit(text4, (960 - (text4.get_width()/2), 490))

        font5 = pygame.font.SysFont("comicsans", 40)
        text5 = font5.render("Left : Q", 1, (255, 255, 255))
        fen.blit(text5, (960 - (text5.get_width()/2), 540))

        font6 = pygame.font.SysFont("comicsans", 40)
        text6 = font6.render("Menu : TAB", 1, (255, 255, 255))
        fen.blit(text6, (960 - (text6.get_width()/2), 590))

        font7 = pygame.font.SysFont("comicsans", 40)
        text7 = font7.render("Quit : Echap", 1, (255, 255, 255))
        fen.blit(text7, (960 - (text7.get_width()/2), 640))


    pygame.display.update()




def End(anti_bug):
    """Fonction gÃ©rant la fin du jeu. Prends en paramÃ¨tre un anti bug int(anti_bug) afin d'Ã©viter d'appuyer du les boutons sans avoir lu le reste avant"""
    font1 = pygame.font.SysFont("comicsans", 40)
    text1 = font1.render("Congratulations for completing the game!", 1, (0, 0, 0))
    fen.blit(text1, (770 - ((text1.get_width()/1)//2), 340))

    mins = tps // 60
    sec = tps % 60
    Time = 'You have play ' +  str(mins) + ' minutes and ' + str(sec) + ' secondes.'
    font2 = pygame.font.SysFont("comicsans", 40)
    text2 = font2.render(Time, 1, (0, 0, 0))
    fen.blit(text2, (770 - (text2.get_width()/2), 370))

    Mort = 'You are dead ' + str(nb_mort) + ' times.'
    font3 = pygame.font.SysFont("comicsans", 40)
    text3 = font3.render(Mort, 1, (0, 0, 0))
    fen.blit(text3, (770 - ((text3.get_width()/1)/2), 400))

    font4 = pygame.font.SysFont("comicsans", 40)
    text4 = font4.render("Game made by Auguste Deroubaix", 1, (0, 0, 0))
    fen.blit(text4, (770 - (text4.get_width()/2), 430))

    if anti_bug < 15:
        anti_bug += 1
    else:
        But3_1.action(pos, (200, 0, 0), (0, 0, 0))

        But3_1.draw(fen, 30)

    pygame.display.update()
    return anti_bug




def New_arme():
    """Fonction permettant de gÃ©rer le changement d'arme."""
    pygame.draw.rect(fen,(255, 255, 255), (685, 425, 550, 220))
    pygame.draw.rect(fen,(255, 0, 0), (685, 425, 550, 220), 1)
    arme = arme_list[nb_arme]
    b = True
    font1 = pygame.font.SysFont("comicsans", 40)
    text1 = font1.render("Current weapon : ", 1, (0, 0, 0))
    fen.blit(text1, (930 - (text1.get_width()/1), 430))

    Name = 'Name : ' + str(perso.arme.nom)
    font2 = pygame.font.SysFont("comicsans", 30)
    text2 = font2.render(Name, 1, (0, 0, 0))
    fen.blit(text2, (930 - (text2.get_width()/1), 460))

    Niv = 'Level : ' + str(perso.arme.lvl)
    font3  = pygame.font.SysFont("comicsans", 30)
    text3 = font3.render(Niv, 1, (0, 0, 0))
    fen.blit(text3, (930 - (text3.get_width()/1), 480))

    Atk = 'Dammage : ' + str(perso.arme.atk)
    font4 = pygame.font.SysFont("comicsans", 30)
    text4 = font4.render(Atk, 1, (0, 0, 0))
    fen.blit(text4, (930 - (text4.get_width()/1), 500))

    Range = 'Range : ' + str(perso.arme.range)
    font5 = pygame.font.SysFont("comicsans", 30)
    text5 = font5.render(Range, 1, (0, 0, 0))
    fen.blit(text5, (930 - (text5.get_width()/1), 520))

    Col = 'Speed : ' + str(math.ceil(30 / perso.arme.coldown))
    font6 = pygame.font.SysFont("comicsans", 30)
    text6 = font6.render(Col, 1, (0, 0, 0))
    fen.blit(text6, (930 - (text6.get_width()/1), 540))


    font7 = pygame.font.SysFont("comicsans", 40)
    text7 = font7.render("Nouvelle Arme : ", 1, (0, 0, 0))
    fen.blit(text7, (990, 430))

    Name2 = 'Name : ' + str(arme.nom)
    font8 = pygame.font.SysFont("comicsans", 30)
    text8 = font8.render(Name2, 1, (0, 0, 0))
    fen.blit(text8, (990, 460))

    if perso.arme.lvl > arme.lvl:
        color = (255, 0, 0)
    elif perso.arme.lvl == arme.lvl:
        color = (0, 0, 0)
    elif perso.arme.lvl < arme.lvl:
        color = (0, 255, 0)
    Niv2 = 'Level : ' + str(arme.lvl)
    font9  = pygame.font.SysFont("comicsans", 30)
    text9 = font9.render(Niv2, 1, color)
    fen.blit(text9, (990, 480))

    if perso.arme.atk > arme.atk:
        color = (255, 0, 0)
    elif perso.arme.atk == arme.atk:
        color = (0, 0, 0)
    elif perso.arme.atk < arme.atk:
        color = (0, 255, 0)
    Atk2 = 'Dammage : ' + str(arme.atk)
    font10 = pygame.font.SysFont("comicsans", 30)
    text10 = font10.render(Atk2, 1, color)
    fen.blit(text10, (990, 500))

    if perso.arme.range > arme.range:
        color = (255, 0, 0)
    elif perso.arme.range == arme.range:
        color = (0, 0, 0)
    elif perso.arme.range < arme.range:
        color = (0, 255, 0)
    Range2 = 'Range : ' + str(arme.range)
    font11 = pygame.font.SysFont("comicsans", 30)
    text11 = font11.render(Range2, 1, color)
    fen.blit(text11, (990, 520))

    Cold = 'Speed : ' + str(math.ceil(30 / arme.coldown))
    if Col > Cold:
        color = (255, 0, 0)
    elif Col == Cold:
        color = (0, 0, 0)
    elif Col < Cold:
        color = (0, 255, 0)
    font12 = pygame.font.SysFont("comicsans", 30)
    text12 = font12.render(Cold, 1, color)
    fen.blit(text12, (990, 540))


    font13 = pygame.font.SysFont("comicsans", 40)
    text13 = font13.render('Change ?', 1, (0, 0, 0))
    fen.blit(text13, (960 - (text6.get_width()/2), 570))

    But10.action(pos, (0, 0, 255), (0, 0, 150), arme)
    But10.draw(fen, 30)
    But11.action(pos, (0, 0, 255), (0, 0, 150))
    But11.draw(fen, 30)




def Mort():
    """Fonction permettant de gÃ©rer la mort du joueur"""
    fen.blit(Ecran_mort, (0, 0))
    font1 = pygame.font.SysFont("comicsans", 40)
    text1 = font1.render("You are dead", 1, (255, 0, 0))
    fen.blit(text1, (960 - (text1.get_width()/2), 520))

    But3_2.action(pos, (200, 0, 0), (255, 0, 0))
    But7.action(pos, (200, 0, 0), (255, 0, 0))

    But3_2.draw(fen, 30)
    But7.draw(fen, 30)




def Inventaire(tps):
    """Fonction gÃ©rant l'invantaire du joueur. Prends en paramÃ¨tre le temps Ã©couler depuis le dÃ©but de la partie int(tps)"""
    tps += 1
    fen.blit(Menu, (510, 270))

    Or = str(perso.gold)
    font8 = pygame.font.SysFont("comicsans", 60)
    text8 = font8.render(Or, 1, (255, 255, 255))
    fen.blit(text8, (801 - (text8.get_width()/1), 596))

    exp = (10 + (10*perso.lvl))
    Exp = str(perso.xp) + '/' + str(exp)
    font2 = pygame.font.SysFont("comicsans", 60)
    text2 = font2.render(Exp, 1, (255, 255, 255))
    fen.blit(text2, (810 - (text2.get_width()/1), 418))

    niv = perso.lvl + 1
    Niv = str(niv)
    font3 = pygame.font.SysFont("comicsans", 60)
    text3 = font3.render(Niv, 1, (255, 255, 255))
    fen.blit(text3, (990 - (text3.get_width()/1), 290))

    Vie = str(perso.pv) + '/' + str(perso.life)
    font4 = pygame.font.SysFont("comicsans", 60)
    text4 = font4.render(Vie, 1, (255, 255, 255))
    fen.blit(text4, (1119, 469))

    Force = str(perso.strengh)
    font5 = pygame.font.SysFont("comicsans", 60)
    text5 = font5.render(Force, 1, (255, 255, 255))
    fen.blit(text5, (1130, 551))

    atk = str(perso.atk)
    font6 = pygame.font.SysFont("comicsans", 60)
    text6 = font6.render(atk, 1, (255, 255, 255))
    fen.blit(text6, (1066, 635))

    Vitesse = str(perso.vel)
    font7 = pygame.font.SysFont("comicsans", 60)
    text7 = font7.render(Vitesse, 1, (255, 255, 255))
    fen.blit(text7, (834 - (text7.get_width()/1), 755))

    Niveau = 'Depth : ' + str(nb_niveaux)
    font8 = pygame.font.SysFont("comicsans", 60)
    text8 = font8.render(Niveau, 1, (255, 255, 255))
    fen.blit(text8, (1920 - (text8.get_width()/1), 0))

    return tps




def Fin_niveau(anti_bug):
    """Fonction permettant de gÃ©rer la fin de niveau et son changement. Prends en fonction l'anti bug int(anti_bug) afin de ne pas appuyer sur des boutons lors d'une attaque
    (pygame dÃ©tecte deux fois le clique de la sourie)"""
    fen.blit(Ecran_suite, (0, 0))
    Niv = "You have completed this deep " + str(nb_niveaux)
    font1 = pygame.font.SysFont("comicsans", 40)
    text1 = font1.render(Niv, 1, (0, 0, 0))
    fen.blit(text1, (960 - (text1.get_width()/2), 520))

    arme = perso.arme
    font2 = pygame.font.SysFont("comicsans", 40)
    text2 = font2.render("Weapon characteristics :", 1, (0, 0, 0))
    fen.blit(text2, (1880 - (text2.get_width()/1), 440))

    Nom = 'Name : ' + str(arme.nom)
    font3 = pygame.font.SysFont("comicsans", 30)
    text3 = font3.render(Nom, 1, (0, 0, 0))
    fen.blit(text3, (1880 - (text3.get_width()/1), 480))

    Atk = 'Dammage : ' + str(arme.atk)
    font4 = pygame.font.SysFont("comicsans", 30)
    text4 = font4.render(Atk, 1, (0, 0, 0))
    fen.blit(text4, (1880 - (text4.get_width()/1), 500))

    Range = 'Range : ' + str(arme.range)
    font5 = pygame.font.SysFont("comicsans", 30)
    text5 = font5.render(Range, 1, (0, 0, 0))
    fen.blit(text5, (1880 - (text5.get_width()/1), 520))

    Lvl = 'Level : ' + str(arme.lvl)
    font8 = pygame.font.SysFont("comicsans", 30)
    text8 = font8.render(Lvl, 1, (0, 0, 0))
    fen.blit(text8, (1880 - (text8.get_width()/1), 540))

    Or = "Current gold : " + str(perso.gold) + ' or'
    font7 = pygame.font.SysFont("comicsans", 30)
    text7 = font7.render(Or, 1, (0, 0, 0))
    fen.blit(text7, (1880 - (text7.get_width()/1), 560))

    if anti_bug < 15:
        anti_bug += 1
    else:
        But3_3.action(pos, (200, 0, 0), (0, 0, 0))
        But8.action(pos, (200, 0, 0), (0, 0, 0))

        But3_3.draw(fen, 30)
        But8.draw(fen, 30)

    if perso.gold >= (50 + (50*arme.lvl)) and arme.lvl < 10:
        Coup = "Upgrade cost : " + str(50 + (25*arme.lvl)) + ' or'
        font6 = pygame.font.SysFont("comicsans", 30)
        text6 = font6.render(Coup, 1, (0, 0, 0))
        fen.blit(text6, (1880 - (text6.get_width()/1), 580))

        Am = "Upagrade :"
        font7 = pygame.font.SysFont("comicsans", 30)
        text7 = font7.render(Am, 1, (0, 0, 0))
        fen.blit(text7, (1880 - (text7.get_width()/1), 600))

        Am2 = "Dammage + " + str((arme.atk//5))
        font7 = pygame.font.SysFont("comicsans", 30)
        text7 = font7.render(Am2, 1, (0, 0, 0))
        fen.blit(text7, (1880 - (text7.get_width()/1), 620))
        But9.action(pos, (0, 0, 200), (0, 0, 255), arme)
        But9.draw(fen, 30)

    return anti_bug




def Montee_niveau(tps, Son, anti_bug):
    """Fonction s'occupant de gÃ©rer la montÃ©e de niveau du joueur. Prends en paramÃ¨tre le temps Ã©coulÃ© depuis le dÃ©but de la partie int(tps),
    la variable son permettant de jouer qu'une seule fois le son int(Son) et encore l'anti bug int(anti_bug)"""
    tps += 1
    if Son == 0:
        Son_lvlup.play()
        Son =1
    pygame.draw.rect(fen, (255, 255, 255), (760, 460, 400, 160))
    pygame.draw.rect(fen, (200, 0, 0), (760, 460, 400, 160), 2)


    font1 = pygame.font.SysFont("comicsans", 30)
    text1 = font1.render("You have level up !", 1, (0, 0, 0))
    fen.blit(text1, (960 - (text1.get_width()/2), 480))

    font2 = pygame.font.SysFont("comicsans", 30)
    text2 = font2.render("Which stat would you upgrade :", 1, (0, 0, 0))
    fen.blit(text2, (960 - (text2.get_width()/2), 510))

    if anti_bug < 15:
        anti_bug += 1
    else:
        if perso.lvl_life < 12:
            But4.action(pos, (0, 0, 255), (0, 0, 150))
            But4.draw(fen, 30)

        if perso.lvl_strengh < 13:
            But5.action(pos, (0, 0, 255), (0, 0, 150))
            But5.draw(fen, 30)

        if perso.lvl_speed < 4:
            But6.action(pos, (0, 0, 255), (0, 0, 150))
            But6.draw(fen, 30)

    return tps, Son, anti_bug




temps_attente_touche = 0.0


#Boucle du menu
Son = 0
while run2:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        run = False
        pygame.quit()
        quit()

    if key[pygame.K_F4] and temps_attente_touche == 0.0:
        if full_screen:
            fen = pygame.display.set_mode(fen_size)
            full_screen = False
        else:
            fen = pygame.display.set_mode(fen_size, pygame.FULLSCREEN)
            full_screen = True
        temps_attente_touche = 0.5

    fps = clock.get_fps()
    if (temps_attente_touche > 0.0 and fps > 0):
        temps_attente_touche -= 1 / fps
        if (temps_attente_touche < 0.0):
            temps_attente_touche = 0.0

    fen.blit(Ecran_titre, (0, 0))

    menu(fenetre)

    clock.tick(30)




#Boucle principale
if run:
    Mobs = []
    Map = Creation_mur(Map)

    nb_mob = random.randint(2, 6)
    for i in range(nb_mob):
        mob = Monstre(nb_niveaux)
        Mobs.append(mob)

    for mob in Mobs:
        mob.spawn(Map)


while run:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        run = False

    if key[pygame.K_k]:
        perso.xp += 100
        perso.gold += 100


    if Fin:
        pygame.mouse.set_visible(True)
        anti_bug = End(anti_bug)


    elif not boss:
        pygame.mouse.set_visible(True)
        New_arme()


    elif perso.pv <= 0:
        pygame.mouse.set_visible(True)
        Mort()


    elif key[pygame.K_TAB]:
        pygame.mouse.set_visible(False)
        tps = Inventaire(tps)


    elif nb_mob == 0:
        pygame.mouse.set_visible(True)
        anti_bug = Fin_niveau(anti_bug)


    elif perso.xp >= (10 + (10*perso.lvl)) and perso.lvl < 29:
        pygame.mouse.set_visible(True)
        tps, Son, anti_bug = Montee_niveau(tps, Son, anti_bug)


    else:
        pygame.mouse.set_visible(False)
        tps += 1
        anti_bug = 0
        nb_mob, Son, test_collid, test_pos, Fin, tps, projectiles_list, boss, nb_arme, niveau_save = raffraichissement(test_pos, nb_mob, test_collid, Fin, tps, projectiles_list, boss, nb_arme, niveau_save )

    pygame.display.update()
    clock.tick(30) #fps



save = [perso.arme, perso.lvl, perso.xp, perso.lvl_life, perso.lvl_speed, perso.lvl_strengh, perso.gold, nb_niveaux, niveau_save, nb_mort, tps]

with open('Save_game', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(save)

pygame.quit()
quit()
