import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)


gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)


for i in range(50, 150, 5):
    for j in range(100, 200, 5):
        pixAr[i][j] = green

pygame.draw.line(gameDisplay, blue,(250,350),(500,300),10)

pygame.draw.circle(gameDisplay,red,(500,200), 100, 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()