# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)

playerA = 0
playerB = 0

# Open a new window
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

kill_listA =  pygame.sprite.Group()
kill_listA.add(wallA)

kill_listB = pygame.sprite.Group()
kill_listB.add(wallB)


carryOn = True



ball = Ball(WHITE,10,10, paddle_list, playerA, playerB, kill_listA, kill_listB, carryOn)
ball.rect.x = 345
ball.rect.y = 195
ball.rebound = False

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


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)

    if keys[pygame.K_s]:
        paddleA.moveDown(5)


    if keys[pygame.K_UP]:
        paddleB.moveUp(5)

    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)



    all_sprites_list.update()
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
