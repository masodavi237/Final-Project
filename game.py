import pygame
from paddle import Paddle
from ball import Ball
from random import randint
import time
import graphics


pygame.init()


def reposition(ball):
    ball.velocity = [randint(5, 7), randint(-5, 7)]
    ball.killA = False
    ball.killB = False
    ball.rect.x = 350
    ball.rect.y = 250
    time.sleep(0.5)
    all_sprites_list.draw(screen)


def draw_score(number_list, playerA, playerB):
    if playerA <= 9:
        screen.blit(number_list[playerA], (200, 0))
    if playerA > 9:
        screen.blit(number_list[1], (135, 0))
        screen.blit(number_list[0], (200, 0))

    if playerB <= 9:
        screen.blit(number_list[playerB], (350+20, 0))
    if playerB > 9:
        screen.blit(number_list[1], (350 + 20, 0))
        screen.blit(number_list[0], (350 + 20 + 65, 0))


def draw_button():
    mouse_pos = pygame.mouse.get_pos()
    if 270 + 140 > mouse_pos[0] > 270 and 290 + 60 > mouse_pos[1] > 290:
        screen.blit(play_button_two, [270, 290])

    else:
        screen.blit(play_button_one, [270, 290])


def draw_logo():
    screen.blit(pong_logo, [0, 0])


def start_up():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                quit()

        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 270 + 140 > mouse_pos[0] > 270 and 290 + 60 > mouse_pos[1] > 290:

            if click[0] == 1:

                intro = False

        screen.fill(BLACK)

        draw_logo()

        draw_button()

        pygame.display.flip()
        clock.tick(60)


def game_over(playerA, playerB):

    after_game = True

    while after_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                after_game = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    after_game = False
                    pygame.quit()
                    quit()

        if playerA == 10:
            draw_game_over_buttons(85)
            print('test')
        elif playerB == 10:
            draw_game_over_buttons(435)

        pygame.display.flip()
        clock.tick(60)


def draw_game_over_buttons(x_button):

    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # draws the play again buttons
    if x_button + 280 - 35 > mouse_pos[0] > x_button - 35 and 310 > mouse_pos[1] > 250:
        screen.blit(play_again_two, [x_button - 35, 250])
        if click[0] == 1:
            main(playerA, playerB)
    else:
        screen.blit(play_again_one, [x_button - 35, 250])
    # draws the quit button
    if x_button + 180 > mouse_pos[0] > x_button + 40 and 420 > mouse_pos[1] > 360:
        screen.blit(quit_two, [x_button + 40, 360])
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        screen.blit(quit_one, [x_button + 40, 360])

    screen.blit(winner_graphic, [x_button, 120])


def main(playerA, playerB):

    carryOn = True

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    carryOn = False
                    pygame.quit()
                    quit()

        if ball.killA:
            playerA += 1
            reposition(ball)

        if ball.killB:
            playerB += 1
            reposition(ball)

        keys = pygame.key.get_pressed()
        ball.get_keys()

        if keys[pygame.K_w]:
            paddleA.moveUp(10)

        if keys[pygame.K_s]:
            paddleA.moveDown(10)

        if keys[pygame.K_UP]:
            paddleB.moveUp(10)

        if keys[pygame.K_DOWN]:
            paddleB.moveDown(10)

        all_sprites_list.update(playerA, playerB, lose_sound, paddle_sound, wall_sound)
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        all_sprites_list.draw(screen)

        draw_score(number_list, playerA, playerB)

        if playerA >= 10 or playerB >= 10:
            game_over(playerA, playerB)
            carryOn = False

        print(ball.velocity[1])

        pygame.display.flip()
        clock.tick(60)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

playerA = 0
playerB = 0

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

one_graphic = pygame.image.load("graphics/one.png").convert()
one_graphic.set_colorkey(BLACK)
two_graphic = pygame.image.load('graphics/two.png').convert()
two_graphic.set_colorkey(BLACK)
three_graphic = pygame.image.load('graphics/three.png').convert()
three_graphic.set_colorkey(BLACK)
four_graphic = pygame.image.load('graphics/four.png').convert()
four_graphic.set_colorkey(BLACK)
five_graphic = pygame.image.load('graphics/five.png').convert()
five_graphic.set_colorkey(BLACK)
six_graphic = pygame.image.load('graphics/six.png').convert()
six_graphic.set_colorkey(BLACK)
seven_graphic = pygame.image.load('graphics/seven.png').convert()
seven_graphic.set_colorkey(BLACK)
eight_graphic = pygame.image.load('graphics/eight.png').convert()
eight_graphic.set_colorkey(BLACK)
nine_graphic = pygame.image.load('graphics/nine.png').convert()
nine_graphic.set_colorkey(BLACK)
zero_graphic = pygame.image.load('graphics/zero.png').convert()
zero_graphic.set_colorkey(BLACK)

pong_logo = pygame.image.load('graphics/pong_logo.png').convert()
pong_logo.set_colorkey(BLACK)

play_button_one = pygame.image.load('graphics/play_one.png').convert()
play_button_two = pygame.image.load('graphics/play_two.png').convert()

winner_graphic = pygame.image.load('graphics/winner.png').convert()
winner_graphic.set_colorkey(BLACK)
play_again_one = pygame.image.load('graphics/play_again_one.png').convert()
play_again_two = pygame.image.load('graphics/play_again_two.png').convert()
quit_one = pygame.image.load('graphics/quit_one.png').convert()
quit_two = pygame.image.load('graphics/quit_two.png').convert()

number_list = []
number_list.append(zero_graphic)
number_list.append(one_graphic)
number_list.append(two_graphic)
number_list.append(three_graphic)
number_list.append(four_graphic)
number_list.append(five_graphic)
number_list.append(six_graphic)
number_list.append(seven_graphic)
number_list.append(eight_graphic)
number_list.append(nine_graphic)

wall_sound = pygame.mixer.Sound('sounds/med_pong.wav')
paddle_sound = pygame.mixer.Sound('sounds/high_pong.wav')
lose_sound = pygame.mixer.Sound('sounds/low_pong.wav')

paddleA = Paddle(WHITE, 10, 50)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 50)
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


start_up()
main(playerA, playerB)


pygame.quit()
print(playerA, playerB)