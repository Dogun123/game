import pygame
import os
from pygame.constants import K_UP, QUIT
from random import *

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))



pygame.display.set_caption("똥피하기")

clock = pygame.time.Clock()

# 사용자 게임 초기화
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images")
music_path = os.path.join(current_path,"sound")

# 배경
background = pygame.image.load(os.path.join(image_path,"background.png"))



# start button
start_button = pygame.image.load(os.path.join(image_path,"StartIcon.png"))
start_button_size = start_button.get_rect().size
start_button_width = start_button_size[0]
start_button_height = start_button_size[1]
start_button_x_pos = screen_width/2 - start_button_width/2
start_button_y_pos = screen_height/2 - start_button_height/2



running = False

score = 0

RUN = True
PLAY = 1
STOP = 0

START = True
READY = True
screen.blit(background,(0,0))
pygame.display.flip()

ready_font = pygame.font.Font(None,100)

start_buttons = [pygame.image.load(os.path.join(image_path,"StartIcon.png"))]

while START:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        # if event.type == pygame.MOUSEMOTION:
        #     if pos[0] > start_button_x_pos and pos[0] < start_button_x_pos + start_button_width:
        #         if pos[1] > start_button_y_pos and pos[1] < start_button_y_pos + start_button_height:
        #             print("마우스포착")
        #             del start_buttons[0]
        #             start_buttons = [pygame.image.load(os.path.join(image_path,"clickedStartIcon_big.png"))]
        #         else: 
        #             start_icon = "StartIcon.png"         
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > start_button_x_pos and pos[0] < start_button_x_pos + start_button_width:
                if pos[1] > start_button_y_pos and pos[1] < start_button_y_pos + start_button_height:
                    START = False
                    running = True

    screen.blit(start_button,(start_button_x_pos,start_button_y_pos))
    pygame.display.update()  


pygame.time.delay(1000)

# 배경음악
pygame.mixer.music.load(os.path.join(music_path,"backgroundmusic.mp3"))

# Music stream 무한 반복
pygame.mixer.music.play(-1)

#character
character = pygame.image.load(os.path.join(image_path,"spongebob.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height-character_height

#enemy
enemy = pygame.image.load(os.path.join(image_path,"ddong.png")) 
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy1_x_pos = randint(0,screen_width-enemy_width)
enemy1_y_pos = randint(-500,0)
enemy2_x_pos = randint(0,screen_width-enemy_width)
enemy2_y_pos = randint(-500,0)


#font
fail_font = pygame.font.Font(None,70)
score_font = pygame.font.Font(None,40)
#character move
x_move = 0
y_move = 0

#character speed
character_speed = 0.6

#enemy move
enemy_move = 0

#enemy speed
enemy_speed = 0.6



while running:

    if RUN == True:
        dt = clock.tick(60) * PLAY
    else:
        dt = clock.tick(60) * STOP
        pygame.mixer.music.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_move += character_speed
            elif event.key == pygame.K_LEFT:
                x_move -= character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_move = 0

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height
    
    character_x_pos += x_move * dt
    character_y_pos += y_move * dt

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    if enemy1_y_pos < screen_height:
        enemy_move += enemy_speed
    
    enemy1_y_pos += enemy_speed * dt

    if enemy1_y_pos >= screen_height:
        enemy1_y_pos = randint(-500,0)
        enemy1_x_pos = randint(0,screen_width-enemy_width)
        score += 1
        print(score)

    enemy_rect1 = enemy.get_rect()
    enemy_rect1.left = enemy1_x_pos
    enemy_rect1.top = enemy1_y_pos

    if enemy2_y_pos < screen_height:
        enemy_move += enemy_speed
    
    enemy2_y_pos += enemy_speed * dt

    if enemy2_y_pos >= screen_height:
        enemy2_y_pos = randint(-500,0)
        enemy2_x_pos = randint(0,screen_width-enemy_width)
        score += 1
        print(score)

    enemy_rect2 = enemy.get_rect()
    enemy_rect2.left = enemy2_x_pos
    enemy_rect2.top = enemy2_y_pos
    
    enemy_rect = [enemy_rect1,enemy_rect2]
    
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy1_x_pos,enemy1_y_pos))
    screen.blit(enemy,(enemy2_x_pos,enemy2_y_pos)) 

    for i in enemy_rect:
        if character_rect.colliderect(i):
            fail_caption = fail_font.render("result : {}".format(score),True,(100,100,100))
            screen.blit(fail_caption,(screen_width/2-80,screen_height/2-100))
            RUN = False
            

    total_score = score_font.render("score : {0}".format(score),True,(150,150,150))
    screen.blit(total_score,(10,10))
    
    pygame.display.update()

pygame.quit()
