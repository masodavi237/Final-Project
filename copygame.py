
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

playerA = 0
playerB = 0
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# paddleA = Paddle(WHITE, 10, 100)
# paddleA.rect.x = 20
# paddleA.rect.y = 200
#
# paddleB = Paddle(WHITE, 10, 100)
# paddleB.rect.x = 670
# paddleB.rect.y = 200


wallA = Paddle(BLACK, 10, 700)
wallA.rect.x = 0
wallA.rect.y = 0

wallB = Paddle(BLACK, 10, 700)
wallB.rect.x = 690
wallB.rect.y = 0


all_sprites_list = pygame.sprite.Group()
paddle_list = pygame.sprite.Group()
# paddle_list.add(paddleA)
# paddle_list.add(paddleB)

kill_listA = pygame.sprite.Group()
kill_listA.add(wallA)

kill_listB = pygame.sprite.Group()
kill_listB.add(wallB)


carryOn = True



ball = Ball(WHITE,10,10, paddle_list, playerA, playerB, kill_listA, kill_listB, carryOn)
ball.rect.x = 345
ball.rect.y = 195
ball.rebound = False
#
# all_sprites_list.add(paddleA)
# all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


all_sprites_list.add(wallA)
all_sprites_list.add(wallB)

kill_listA = pygame.sprite.Group()
kill_listA.add(wallA)

kill_listB = pygame.sprite.Group()
kill_listB.add(wallB)


clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    if ball.kill:
        carryOn = False


    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     paddleA.moveUp(5)
    #
    # if keys[pygame.K_s]:
    #     paddleA.moveDown(5)
    #
    #
    # if keys[pygame.K_UP]:
    #     paddleB.moveUp(5)
    #
    # if keys[pygame.K_DOWN]:
    #     paddleB.moveDown(5)



    all_sprites_list.update()
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()





import pygame

from random import randint, uniform
import math

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

        self.speed = math.sqrt(4)


        self.x = 10
        self.y = 10



        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # self.velocity = [randint(2,4),randint(-2,4)]


        self.velocity = [uniform(0,2)]
        self.yspeed = math.sqrt((self.speed**2) - (self.velocity[0]**2))
        self.velocity.append(self.yspeed)


        self.rect = self.image.get_rect()

        self.keys = pygame.key.get_pressed()





    def update(self):
        self.x += self.velocity[0]
        self.rect.x = int(self.x)
        self.y += self.velocity[1]
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
            self.y = self.y - self.velocity[1] - 1
            self.velocity[1] = -1 * self.velocity[1]
        if self.rect.y < 0:
            self.y = self.y - self.velocity[1] + 1
            self.velocity[1] = -1 * self.velocity[1]

        print(self.velocity)
        print(self.x)
        print(self.y)


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









