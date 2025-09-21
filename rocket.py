import pygame
from time import *
pygame.init()
run = True
Screen = pygame.display.set_mode((714,400))
rimg = pygame.image.load(r"C:\Users\femia\Desktop\python_game_dev\Pro Game dev\rocket.png")
bimg = pygame.image.load(r"C:\Users\femia\Desktop\python_game_dev\Pro Game dev\skybg.jpg")

keys = [False,False,False,False]
#up,right,down,left
rx = 357
ry = 200



while run == True:
    Screen.blit(bimg,(0,0))
    Screen.blit(rimg,(rx,ry))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                keys[0] = True
            if i.key == pygame.K_DOWN:
                keys[1] = True
            if i.key == pygame.K_LEFT:
                keys[2] = True
            if i.key == pygame.K_RIGHT:
                keys[3] = True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_UP:
                keys[0] = False
            if i.key == pygame.K_DOWN:
                keys[1] = False
            if i.key == pygame.K_LEFT:
                keys[2] = False
            if i.key == pygame.K_RIGHT:
                keys[3] = False
    if keys[0] == True:
        ry = ry - 1 
    elif keys[1] == True:
        ry = ry + .5
    elif keys[2] == True:
        rx = rx  - 1
    elif keys[3] == True:
        rx = rx + 1
    ry = ry + .5
    sleep(0.005)

