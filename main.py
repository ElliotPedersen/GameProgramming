import pygame

pygame.init()

windowSize = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

myFont = pygame.font.SysFont("Segoe UI", 90)

helloWorld = myFont.render("Hello, World!", 1, (255, 0, 255), (255, 255, 255))

while 1:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): 
            sys.exit()
        windowSize.blit(helloWorld, (0, 0))
        pygame.display.update()    