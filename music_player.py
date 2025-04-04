import pygame

def music_player():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Music Player")
    
    playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
    current_track = 0
    pygame.mixer.music.load(playlist[current_track])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                elif event.key == pygame.K_n:
                    current_track = (current_track + 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_track])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_p:
                    current_track = (current_track - 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_track])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_s:
                    pygame.mixer.music.stop()
        
        screen.fill((200, 200, 200))
        pygame.display.flip()
    
    pygame.quit()

