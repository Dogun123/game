from random import *
import pygame
import os

img= pygame.image.load("C:\GitHubDesktop\game\pygame_project\ddong_game\images\clickedStartIcon.png")
img_scale = pygame.transform.scale(img,(162,42))
pygame.image.save(img_scale,"C:\GitHubDesktop\game\pygame_project\ddong_game\images\clickedStartIcon_big.png")
