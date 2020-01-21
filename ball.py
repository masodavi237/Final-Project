import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):


    def __init__(self, color, width, height, paddle_list, playerA, playerB, kill_listA, kill_listB, carryOn):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.paddle_list = paddle_list

        self.kill_listA = kill_listA
        self.kill_listB = kill_listB

        self.playerA = playerA

        self.kill = False


        self.x = 5.6
        self.y = 4.5



        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # self.velocity = [randint(2,4),randint(-2,4)]
        self.velo = randint(2,4)

        self.velocity = [self.velo, 6-self.velo]

        self.rect = self.image.get_rect()

        self.keys = pygame.key.get_pressed()





    def update(self):
        self.x += self.velocity[0]
        self.rect.x  = int(self.x)
        self.y +=  self.velocity[1]
        self.rect.y += int(self.y)
        if pygame.sprite.spritecollide(self, self.paddle_list, False):
            self.hit_paddle()

        if pygame.sprite.spritecollide(self, self.kill_listA, False):
            self.b_win()

        if pygame.sprite.spritecollide(self, self.kill_listB, False):
            self.a_win()

        if self.rect.x >= 690:
            self.velocity[0] = -1 * self.velocity[0]
        if self.rect.x <= 0:
            self.velocity[0] = -1 * self.velocity[0]
        if self.rect.y > 490:
            self.velocity[1] = -1 * self.velocity[1]
        if self.rect.y < 0:
            self.velocity[1] = -1 * self.velocity[1]

    def hit_paddle(self):
        if self.keys[pygame.K_w]:
            self.velocity[1] = randint(self.velocity[1], 4)
        if self.keys[pygame.K_s]:
            self.velocity[1] = randint(-4, self.velocity[1])

        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-4, 4)

    def a_win(self):
        self.kill = True

    def b_win(self):
        self.kill = True




        pass









