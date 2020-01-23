import pygame

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
        self.velocity = [randint(2,4),randint(-2,4)]
        self.rect = self.image.get_rect()
        self.keys = pygame.key.get_pressed()

    def update(self, playerA, playerB):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if pygame.sprite.spritecollide(self, self.paddle_list, False):
            self.hit_paddle()
        if pygame.sprite.spritecollide(self, self.kill_listA, False):
            self.b_win(playerB)
        if pygame.sprite.spritecollide(self, self.kill_listB, False):
            self.a_win(playerA)
        if self.rect.y > 490:
            self.y = self.y - self.velocity[1] - 1
            self.velocity[1] = -1 * self.velocity[1]
        if self.rect.y < 0:
            self.y = self.y - self.velocity[1] + 1
            self.velocity[1] = -1 * self.velocity[1]

    def hit_paddle(self):
        if self.keys[pygame.K_w] or self.keys[pygame.K_UP]:
            self.velocity[1] = randint(self.velocity[1], 4)
        if self.keys[pygame.K_s] or self.keys[pygame.K_DOWN]:
            self.velocity[1] = randint(-4, self.velocity[1])
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-4, 4)

    def a_win(self, playerA):
        playerA += 1
        self.killA = True

    def b_win(self, playerB):
        playerB += 1
        self.killB = True

    def get_keys(self):
        self.keys = pygame.key.get_pressed()














