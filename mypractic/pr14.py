import pygame

pygame.init()
size = ((400, 400))
dis = pygame.display.set_mode(size)
dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False

    for x in range(13):
        for y in range(13):
            pygame.draw.rect(dis, (255, 100, 0), (50*x, 50*y, 40, 40))

    pygame.display.update()
quit()