import pygame

# 이미지 크기 변환
start_button = pygame.image.load("C:\GitHubDesktop\game\pygame_project\ddong_game\images\clickedStartIcon.png")
img_scale = pygame.transform.scale(start_button,(200,58))  # 스케일 변환
pygame.image.save(img_scale, "StartIcon.png")
