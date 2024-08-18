import pygame
import random
def spawn_block():

    _2_4_rng = random.randint(1,10)
    if _2_4_rng == 4:
        new_block_num = 4
        color = (245, 215, 135)
    else:
        new_block_num = 2
        color = (133, 121, 121)
    x = random.randint(0,3)
    y = random.randint(0,3)
    print(x, y)
    pygame.draw.rect(screen, color, pygame.Rect((player_x + (x*90)), (player_y + (y*90)), 80, 80))


def initiate_screen():
    global screen, clock, running, color, color2, dt, player_x, player_y
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    dt = 0
    color = (200,200,200)
    color2 = (75,75,75)
    screen.fill( "white" )
    player_x = 450
    player_y = 170
    draw_board()

def draw_board():
    pygame.draw.rect( screen, color, pygame.Rect( 440, 160, 360, 360 ) )
    for x in range( 440, 800, 90 ):
        for y in range( 160, 520, 90 ):
            pygame.draw.rect( screen, color2, pygame.Rect( x, y, 100, 100 ), 10 )
    run_game()


def run_game():
    spawn_block()
    global running, dt
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

        dt = clock.tick(30) / 1000


        keys = pygame.key.get_pressed( )
        global player_x

        if keys[ pygame.K_w ]:
            player_x += 90
            spawn_block( )
            pygame.time.wait(250)
        if keys[ pygame.K_s ]:
            spawn_block( )
            pygame.time.wait( 250 )
        if keys[ pygame.K_a ]:
            spawn_block( )
            pygame.time.wait( 250 )
        if keys[ pygame.K_d ]:
            spawn_block( )
            pygame.time.wait( 250 )

    pygame.quit()
initiate_screen()
