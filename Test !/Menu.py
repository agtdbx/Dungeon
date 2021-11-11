#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gugus
#
# Created:     13/08/2020
# Copyright:   (c) Gugus 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
pygame.init()

fen_size = fen_width, fen_height = 1540, 800 #Classique
fen = pygame.display.set_mode(fen_size, pygame.RESIZABLE)
fen_surface = pygame.display.get_surface()

pygame.display.set_caption("Dongeon")
clock = pygame.time.Clock() #Le nombre d'ips
fps = 30

fenetre = 0

run2 = True
run = True

def menu():
    run2 = True
    fenetre = 0
    class button():
        def __init__(self, color, x,y,width,height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text

        def draw(self,win,size,outline=None):
            #Call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

            if self.text != '':
                font = pygame.font.SysFont('comicsans', size)
                text = font.render(self.text, 1, (0,0,0))
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        def isOver(self, pos):
            #Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True

            return False

        def action(self, pos, col1, col2):
            global fenetre, run, run2
            if self.isOver(pos):
                key2 = pygame.mouse.get_pressed()
                if key2[0] == 1:
                    if self.text == 'Jouer':
                        fenetre = 1
                    elif self.text == 'Nouvelle Partie':
                        run = True
                        run2 = False
                    elif self.text == 'Continuer':
                        run = True
                        run2 = False
                    elif self.text == 'Options':
                        fenetre = 2
                    elif self.text == 'Retour':
                        fenetre = 0
                    elif self.text == 'Quitter':
                        run = False
                        run2 = False

                self.color = col2

            else:
                self.color = col1


    But1 = button((0, 255, 0), 720, 300, 100, 40, 'Jouer')
    But1_1 = button((0, 255, 0), 600, 350, 100, 40, 'Nouvelle Partie')
    But1_2 = button((0, 255, 0), 840, 350, 100, 40, 'Continuer')
    But1_3 = button((0, 255, 0), 720, 450, 100, 40, 'Retour')
    But2 = button((0, 255, 0), 720, 400, 100, 40, 'Options')
    But2_1 = button((0, 255, 0), 720, 600, 100, 40, 'Retour')
    But3 = button((0, 255, 0), 720, 500, 100, 40, 'Quitter')


    while run2:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        fen.fill((255, 255, 255))

        if fenetre == 0:
            But1.action(pos, (0, 255, 0), (255, 0, 0))
            But2.action(pos, (0, 255, 0), (255, 0, 0))
            But3.action(pos, (0, 255, 0), (255, 0, 0))
            But1.draw(fen, 30)
            But2.draw(fen, 30)
            But3.draw(fen, 30)

        elif fenetre == 1:
            But1_1.action(pos, (0, 255, 0), (255, 0, 0))
            But1_2.action(pos, (0, 255, 0), (255, 0, 0))
            But1_3.action(pos, (0, 255, 0), (255, 0, 0))
            But1_1.draw(fen, 30)
            But1_2.draw(fen, 30)
            But1_3.draw(fen, 30)

        elif fenetre == 2:
            But2_1.action(pos, (0, 255, 0), (255, 0, 0))
            But2_1.draw(fen, 30)

        pygame.display.update()
        clock.tick(fps)

    if run:
        return True
    else:
        return False

menu()

pygame.quit()
quit()
