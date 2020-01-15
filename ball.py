import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height, paddle_list):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)


        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8),randint(-8,8)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


    def update(self, paddle_list):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if pygame.sprite.spritecollide(self, paddle_list, False):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-8, 8)


    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)








