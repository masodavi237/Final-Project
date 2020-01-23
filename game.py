import pygame
from paddle import Paddle
from ball import Ball
from random import randint
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

one_graphic = pygame.image.load("one.png").convert

playerA_position_x = 100
playerA_position_y = 200
playerA = 0
playerB = 0
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

wallA = Paddle(BLACK, 10, 700)
wallA.rect.x = 0
wallA.rect.y = 0

wallB = Paddle(BLACK, 10, 700)
wallB.rect.x = 690
wallB.rect.y = 0

all_sprites_list = pygame.sprite.Group()
paddle_list = pygame.sprite.Group()
paddle_list.add(paddleA)
paddle_list.add(paddleB)

kill_listA = pygame.sprite.Group()
kill_listA.add(wallA)

kill_listB = pygame.sprite.Group()
kill_listB.add(wallB)

ball = Ball(WHITE, 10, 10, paddle_list, playerA, playerB, kill_listA, kill_listB)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

all_sprites_list.add(wallA)
all_sprites_list.add(wallB)

kill_listA = pygame.sprite.Group()
kill_listA.add(wallA)

kill_listB = pygame.sprite.Group()
kill_listB.add(wallB)

clock = pygame.time.Clock()

def reposition(ball):
    ball.velocity = [randint(2,4),randint(-2,4)]
    ball.killA = False
    ball.killB = False
    ball.rect.x = 350
    ball.rect.y = 250
    all_sprites_list.draw(screen)


carryOn = True

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    if ball.killA:
        playerA += 1
        reposition(ball)

    if ball.killB:
        playerB += 1
        reposition(ball)

    keys = pygame.key.get_pressed()
    ball.get_keys()

    if keys[pygame.K_w]:
        paddleA.moveUp(5)

    if keys[pygame.K_s]:
        paddleA.moveDown(5)

    if keys[pygame.K_UP]:
        paddleB.moveUp(5)

    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    if playerA or playerB >= 10:

        carryOn = False



    all_sprites_list.update(playerA, playerB)
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen)



    # screen.blit(screen, one_graphic, [playerA_position_x, playerA_position_y])

    font = pygame.font.Font(None, 74)
    text = font.render(str(playerA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(playerB), 1, WHITE)
    screen.blit(text, (420, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(playerA, playerB)