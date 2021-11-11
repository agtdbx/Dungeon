import pygame, sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

x = 400
y = 400


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        y -= 5
    elif key[pygame.K_d]:
        x += 5
    elif key[pygame.K_s]:
        y += 5
    elif key[pygame.K_a]:
        x -= 5

    Rect1 = pygame.Rect(x, y, 50, 50)
    Rect2 = pygame.Rect(0, 0, 50, 50)

    if Rect1.colliderect(Rect2):
        print('Collision')

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), Rect1)
    pygame.draw.rect(screen, (255, 0, 0), Rect2)
    pygame.display.update()
    clock.tick(60)