import pygame
pygame.init()
run = True
Screen = pygame.display.set_mode((714,400))
rimg = pygame.image.load(r"C:\Users\femia\Desktop\python_game_dev\Pro Game dev\rocket.png")
bimg = pygame.image.load(r"C:\Users\femia\Desktop\python_game_dev\Pro Game dev\skybg.jpg")

keys = [False,False,False,False]
#up,right,down,left
































while run == True:
    Screen.blit(bimg,(0,0))
    Screen.blit(rimg,(357,200))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                keys[0] = True
            if i.key == pygame.K_DOWN    

