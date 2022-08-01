import pygame
pygame.font.init()
pygame.mixer.init()

FPS = 60
PLAYER_DIM = 50
PLAYER_SPEED = 4
FIREBALL_SPEED = 7
FIREBALL_DIM = 10
PLAYER_HP = 5

FIREBALL_FIRE = pygame.mixer.Sound("Assets/fireball.wav")
FIREBALL_HIT = pygame.mixer.Sound("Assets/hit.wav")
GAME_WIN =  pygame.mixer.Sound("Assets/win.wav")

POGODEMON_GOOD = pygame.image.load("Assets/pogodemon.png")
POGODEMON_BAD = pygame.image.load("Assets/bad_pogodemon.png")
BACKGROUND = pygame.image.load("Assets/background.jpg")
SEPARATOR = pygame.image.load("Assets/separator.jpg")
FIREBALL_IMG = pygame.image.load("Assets/fireball.png")
HEART_IMG = pygame.image.load("Assets/heart.png")

POGODEMON_GOOD = pygame.transform.scale(POGODEMON_GOOD, (PLAYER_DIM, PLAYER_DIM))
POGODEMON_BAD = pygame.transform.scale(POGODEMON_BAD, (PLAYER_DIM, PLAYER_DIM))
BACKGROUND = pygame.transform.scale(BACKGROUND, (800, 500))
SEPARATOR = pygame.transform.scale(SEPARATOR, (25, 500))
FIREBALL_IMG = pygame.transform.scale(FIREBALL_IMG, (10, 10))
HEART_IMG = pygame.transform.scale(HEART_IMG, (25, 25))

GAME_END_FONT = pygame.font.SysFont("Impact", 40)

WIN = pygame.display.set_mode((800, 500))
pygame.display.set_caption("POGGERS")

def draw_screen(WIN, player1, player2, fireballs_p1, fireballs_p2, hp1, hp2):
    pygame.display.update()
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(SEPARATOR, (375, 0))
    WIN.blit(POGODEMON_GOOD, (player1.x, player1.y))
    WIN.blit(POGODEMON_BAD , (player2.x, player2.y))

    for i in fireballs_p1:
        WIN.blit(FIREBALL_IMG, (i.x, i.y))
    for i in fireballs_p2:
        WIN.blit(FIREBALL_IMG, (i.x, i.y))

    for i in range(0, hp1):
        WIN.blit(HEART_IMG, (0+ i*25, 0))

    for i in range(0, hp2):
        WIN.blit(HEART_IMG, (775-i*25, 0))

    if hp1 <= 0:
        wins = GAME_END_FONT.render("GREEN WINS!", 1, (0, 255, 0))
        WIN.blit(wins, (400 - wins.get_width() // 2, 200))
        pygame.display.update()
        GAME_WIN.play()
        pygame.time.delay(5000)
        pygame.quit()

    if hp2 <= 0:
        wins = GAME_END_FONT.render("RED WINS!", 1, (255, 0, 0))
        WIN.blit(wins, (400 - wins.get_width() // 2, 200))
        pygame.display.update()
        GAME_WIN.play()
        pygame.time.delay(5000)
        pygame.quit()



def main():
    player1 = pygame.Rect(10, 200, PLAYER_DIM, PLAYER_DIM)
    player2 = pygame.Rect(710, 200, PLAYER_DIM, PLAYER_DIM)

    fireballs_p1 = []
    fireballs_p2 = []

    timer1 = 0
    timer2 = 0

    player1_hp = PLAYER_HP
    player2_hp = PLAYER_HP

    running = 1
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
        keys_pressed = pygame.key.get_pressed()

# PLAYER 1 MOVEMENT ====================================================================================================
        if keys_pressed[pygame.K_d] and player1.x < 325:
            player1.x += PLAYER_SPEED
        if keys_pressed[pygame.K_a] and player1.x > 0:
            player1.x -= PLAYER_SPEED
        if keys_pressed[pygame.K_w] and player1.y > 0:
            player1.y -= PLAYER_SPEED
        if keys_pressed[pygame.K_s] and player1.y < 450:
            player1.y += PLAYER_SPEED

        if event.type == pygame.KEYDOWN and timer1 == 0:
            if event.key == pygame.K_LCTRL:
                timer1 += 35
                FIREBALL_FIRE.play()
                fireball = pygame.Rect(player1.x + PLAYER_DIM - 15, player1.y + PLAYER_DIM - 20, FIREBALL_DIM,
                                       FIREBALL_DIM)
                fireballs_p1.append(fireball)
        if timer1 > 0:
            timer1 -= 1

# PLAYER 2 MOVEMENT ====================================================================================================
        if keys_pressed[pygame.K_RIGHT] and player2.x < 750:
            player2.x += PLAYER_SPEED
        if keys_pressed[pygame.K_LEFT] and player2.x > 400:
            player2.x -= PLAYER_SPEED
        if keys_pressed[pygame.K_UP] and player2.y > 0:
            player2.y -= PLAYER_SPEED
        if keys_pressed[pygame.K_DOWN] and player2.y < 450:
            player2.y += PLAYER_SPEED

        if event.type == pygame.KEYDOWN and timer2 == 0:
            if event.key == pygame.K_RCTRL:
                timer2 += 35
                FIREBALL_FIRE.play()
                fireball = pygame.Rect(player2.x + PLAYER_DIM - 45, player2.y + PLAYER_DIM - 20, FIREBALL_DIM,
                                       FIREBALL_DIM)
                fireballs_p2.append(fireball)
        if timer2 > 0:
            timer2 -= 1

        draw_screen(WIN, player1, player2, fireballs_p1, fireballs_p2, player1_hp, player2_hp)

        for i, j in enumerate(fireballs_p1):
            if player2.colliderect(j):
                FIREBALL_HIT.play()
                player2_hp -= 1
                fireballs_p1.pop(i)
            elif j.x > 810:
                fireballs_p1.pop(i)
            else:
                j.x += FIREBALL_SPEED

        for i, j in enumerate(fireballs_p2):
            if player1.colliderect(j):
                FIREBALL_HIT.play()
                player1_hp -= 1
                fireballs_p2.pop(i)
            elif j.x < -10:
                fireballs_p2.pop(i)
            else:
                j.x -= FIREBALL_SPEED
    pygame.quit()

if __name__ == "__main__":
    main()
