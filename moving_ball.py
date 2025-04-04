import pygame

def moving_ball():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Moving Ball")
    clock = pygame.time.Clock()
    
    ball_x, ball_y = 250, 250
    ball_radius = 25
    ball_speed = 20
    
    running = True
    while running:
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and ball_y - ball_radius - ball_speed >= 0:
                    ball_y -= ball_speed
                elif event.key == pygame.K_DOWN and ball_y + ball_radius + ball_speed <= 500:
                    ball_y += ball_speed
                elif event.key == pygame.K_LEFT and ball_x - ball_radius - ball_speed >= 0:
                    ball_x -= ball_speed
                elif event.key == pygame.K_RIGHT and ball_x + ball_radius + ball_speed <= 500:
                    ball_x += ball_speed
        
        clock.tick(30)
    
    pygame.quit()


