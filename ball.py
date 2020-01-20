import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height, paddle_list, playerA, playerB, kill_listA):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.paddle_list = paddle_list


        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8),randint(-8,8)]


        self.rect = self.image.get_rect()

        self.keys = pygame.key.get_pressed()





    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if pygame.sprite.spritecollide(self, self.paddle_list, False):
            self.hit_paddle()



        if self.rect.x >= 690:
            self.velocity[0] = -self.velocity[0]
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y > 490:
            self.velocity[1] = -self.velocity[1]
        if self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]


    def hit_paddle(self):
        if self.keys[pygame.K_w]:
            self.velocity[1] = randint(self.velocity - 2, 8)
        if self.keys[pygame.K_s]:
            self.velocity[1] = randint(-8 ,self.velocity + 2)
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def kill(self):
        pass









