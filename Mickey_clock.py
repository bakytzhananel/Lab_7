import pygame
import time

def rotate_image(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    return rotated_image, new_rect

def draw_mickey_clock(screen, minute_hand, second_hand):
    now = time.localtime()
    minutes_angle = -((now.tm_min % 60) * 6)
    seconds_angle = -((now.tm_sec % 60) * 6)
    
    screen.fill((255, 255, 255))
    
    min_hand, min_rect = rotate_image(minute_hand, minutes_angle, (250, 250))
    screen.blit(min_hand, min_rect)
    
    sec_hand, sec_rect = rotate_image(second_hand, seconds_angle, (250, 250))
    screen.blit(sec_hand, sec_rect)
    
    pygame.display.flip()

def mickey_clock():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Mickey Clock")
    clock = pygame.time.Clock()
    
    minute_hand = pygame.image.load("right_hand.png")
    second_hand = pygame.image.load("left_hand.png")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_mickey_clock(screen, minute_hand, second_hand)
        clock.tick(30)
    
    pygame.quit()
