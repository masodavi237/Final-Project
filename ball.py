import pygame
import time

from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height, paddle_list, playerA, playerB, kill_listA, kill_listB):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.paddle_list = paddle_list
        self.kill_listA = kill_listA
        self.kill_listB = kill_listB
        self.playerA = playerA
        self.playerB = playerB
        self.killA = False
        self.killB = False
        self.x = 100
        self.y = 200
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(5, 7), randint(-5, 7)]
        self.rect = self.image.get_rect()
        self.keys = pygame.key.get_pressed()

    def update(self, playerA, playerB, lose_sound, paddle_sound, wall_sound):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if pygame.sprite.spritecollide(self, self.paddle_list, False):
            self.hit_paddle(paddle_sound)
        if pygame.sprite.spritecollide(self, self.kill_listA, False):
            self.b_win(playerB, lose_sound)
        if pygame.sprite.spritecollide(self, self.kill_listB, False):
            self.a_win(playerA, lose_sound)
        if self.rect.y > 490:
            self.y = self.y - self.velocity[1] - 1
            self.velocity[1] = -1 * self.velocity[1]
            wall_sound.play()
        if self.rect.y < 0:
            self.y = self.y - self.velocity[1] + 1
            self.velocity[1] = -1 * self.velocity[1]
            wall_sound.play()

    def hit_paddle(self, paddle_sound):
        if self.keys[pygame.K_w] or self.keys[pygame.K_UP]:
            self.velocity[1] = randint(self.velocity[1], 5)
        if self.keys[pygame.K_s] or self.keys[pygame.K_DOWN]:
            self.velocity[1] = randint(-7, self.velocity[1])
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-5, 5)
        paddle_sound.play()

    def a_win(self, playerA, lose_sound):
        playerA += 1
        self.killA = True
        lose_sound.play()

    def b_win(self, playerB, lose_sound):
        playerB += 1
        self.killB = True
        lose_sound.play()

    def get_keys(self):
        self.keys = pygame.key.get_pressed()














