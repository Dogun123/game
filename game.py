import sys
import pygame
from pygame.locals import QUIT
from random import *
WIDTH = 500
HEIGHT = 500 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])
FPSCLOCK = pygame.time.Clock() 

# def ball():
#     ball = pygame.draw.circle(SCREEN,BLACK,(WIDTH*0.2,HEIGHT*0.8),5)

#     key_event = pygame.key.get_pressed()
#     if key_event[pygame.K_LEFT]:
#         pos_x -= 1
#     if key_event[pygame.K_RIGHT]:
#         pos_x += 1
#     if key_event[pygame.K_UP]:
#         pos_y -= 1
#     if key_event[pygame.K_DOWN]:
#         pos_y += 1


#     return ball

def ball(color,x,y):
    ball = pygame.draw.circle(SCREEN,color,(x,y),5)
    return ball 


def main():  
    
    pos_x = WIDTH*0.2
    pos_y = HEIGHT*0.8

    target_xpos = random()*WIDTH-20
    target_ypos = random()*HEIGHT-20
    
    target = pygame.image.load("car.png")
    target = pygame.transform.scale(target,(100,100))
    
    COUNT = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        SCREEN.fill(WHITE)
        
        my_ball = ball(BLACK,pos_x,pos_y)

        
        my_ball
        

        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_LEFT]:
            pos_x -= 1
        if key_event[pygame.K_RIGHT]:
            pos_x += 1
        if key_event[pygame.K_UP]:
            pos_y -= 1
        if key_event[pygame.K_DOWN]:
            pos_y += 1
        
        
        


        pygame.display.update()
        FPSCLOCK.tick(200)  


if __name__ == '__main__':
    main() 