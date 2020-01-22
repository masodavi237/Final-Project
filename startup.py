import pygame


def open_screen(screen):
    done = False
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return
                else:

                    return

        screen.fill(BLACK)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def transition(BLACK):
    pass


clock = pygame.time.Clock()


BLACK = (0, 0, 0,)

size = (700, 500)
screen = pygame.display.set_mode(size)


