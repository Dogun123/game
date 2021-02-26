import pygame
import os
from pygame.constants import K_SPACE, K_UP, QUIT
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

# 캐릭터 점프
character_jump_y = [-9, -7, -5, -3]

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
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > start_button_x_pos and pos[0] < start_button_x_pos + start_button_width:
                if pos[1] > start_button_y_pos and pos[1] < start_button_y_pos + start_button_height:
                    START = False
                    running = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                START = False
                running = True

    screen.blit(start_button,(start_button_x_pos,start_button_y_pos))
    pygame.display.update()  


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

enemies =[[randint(0,screen_width-enemy_width),randint(-500,0)]]

enemies_number = [2,3,4,5]


#font
fail_font = pygame.font.Font(None,70)
score_font = pygame.font.Font(None,40)
#character move
x_move = 0
y_move = 0
JUMP = True

#character speed
character_speed = 0.6

#enemy move
enemy_move = 0

#enemy speed
enemy_speed = 0.6



#게임 시작
start_ticks = pygame.time.get_ticks()

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
            elif event.key == pygame.K_UP:
                y_move += -0.5
                
                
                
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                x_move = 0
            if event.key == pygame.K_UP:
                JUMP = False

    if character_y_pos <= 400:
            JUMP = False
    elif character_y_pos == screen_height-character_height:
            JUMP = True
            
    if JUMP == False:
        y_move += 0.5

    character_x_pos += x_move * dt
    character_y_pos += y_move * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height
        
    
    

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    #enemies = [[e[0],e[1]+(enemy_speed*dt)] for e in enemies]



    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    

    for e in enemies:
        screen.blit(enemy,(e[0],e[1]))

    for e in enemies:
        
        if e[1] < screen_height:
            enemy_move += enemy_speed
        
        e[1] += enemy_speed * dt

        if e[1] >= screen_height:
            e[1] = randint(-500,0)
            e[0] = randint(0,screen_width-enemy_width)
            score += 1
            if score == 10:
                enemies.append([randint(0,screen_width-enemy_width),randint(-500,0)])
            elif score == 15:
                enemies.append([randint(0,screen_width-enemy_width),randint(-500,0)])
            elif score == 20:
                enemies.append([randint(0,screen_width-enemy_width),randint(-500,0)])
            elif score == 25:
                enemies.append([randint(0,screen_width-enemy_width),randint(-500,0)])
            print(score)

        enemy_rect = enemy.get_rect()
        enemy_rect.left = e[0]
        enemy_rect.top = e[1]

        
        
        if character_rect.colliderect(enemy_rect):
            fail_caption = fail_font.render("result : {}".format(score),True,(100,100,100))
            screen.blit(fail_caption,(screen_width/2-80,screen_height/2-100))
            RUN = False

    # if score == :
    #     enemies.append([randint(0,screen_width-enemy_width),randint(-500,0)])
    

    
            

    total_score = score_font.render("score : {0}".format(score),True,(150,150,150))
    screen.blit(total_score,(10,10))
    
    pygame.display.update()

pygame.quit()
