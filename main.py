import pygame, sys
from CharacterObject.Enemy import Enemy, draw_health_bar
from pygame.locals import *
from CharacterObject.Player import Player, draw_lives

# Init the game and its clock
# clock is used for rendering
pygame.init()
clock = pygame.time.Clock()

# Set the screen resolution of the game window
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# fonts and text
font = pygame.font.SysFont("Comic Sans", 60)
font2 = pygame.font.SysFont("Comic Sans", 40)
font3 = pygame.font.SysFont("Comic Sans", 27)
font4 = pygame.font.SysFont("Comic Sans", 80)
game_over = font.render("Game Over", True, (255, 255, 255))
you_win = font.render("YOU WIN!", True, (0, 255, 0))
you_lost = font.render("YOU LOST :(", True, (255, 0, 0))
restart = font2.render("-- Press SPACE to restart --", True, (173, 216, 230))
quit_text = font2.render("-- Press q to quit --", True, (255, 165, 0))
welcome = font4.render("Welcome!", True, (255, 255, 255))
start_text = font2.render("Press SPACE to begin", True, (1, 50, 32))
move = font3.render("Arrow Keys = Move", True, (10, 0, 150))
shift = font3.render(" +LShift = Precise Move", True, (10, 0, 150))
shoot = font3.render("Z = Shoot", True, (10, 0, 150))

# Init enemy instance
enemy = Enemy(50, 50, 300, 150, 20000)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

# enemy movement patterns
path_pattern_1 = [(100, 150), (300, 150), (500, 150), (300, 150)]
path_pattern_2 = [(100, 100), (500, 200), (500, 100), (100, 200)]
path_pattern_3 = [(300, 200)]
path_pattern_4 = [(100, 300), (300, 100), (500, 300), (100, 175), (500, 175)]
path_pattern_5 = [(100, 100), (500, 200), (500, 100), (100, 200)]

enemy_bullets = [
    pygame.image.load("images/enemy bullet 1.png"),
    pygame.image.load("images/enemy bullet 2.png")
]

# Init player instance
player1 = Player()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
heart = pygame.image.load("images/heart.png")

player_next_time = 0  # for time counting
enemy_next_time = 0  # for time counting
spin = 0  # for spin angle iterating
bg_scroll = 0


def do_bullet_pattern(bullet_amount, speed, spin_delta):
    """Procedure for the enemy's bullet pattern.

    bullet_amount -- number of bullets in the circle

    speed -- the distance traveled every nth frame

    spin_delta -- the difference in angle every nth frame
    """

    for b in range(bullet_amount):
        enemy_bullet_group.add(enemy.create_bullet(enemy_bullets[0], b * (360 / bullet_amount), speed, spin_delta))
    enemy_bullets.append(enemy_bullets[0])
    enemy_bullets.pop(0)


def handle_game_over():
    """Handles the "Game Over" screen

    Listens to user-input for restarting (Space )or quitting the game (q)
    """

    global enemy_next_time
    event_over = pygame.event.wait()
    if event_over.type == pygame.KEYDOWN:
        # restart game
        if event_over.key == pygame.K_SPACE:
            enemy.rect.center = (300, 150)
            enemy.health = 20000
            player1.lives = 3
            player1.rect.center = (160, 550)
            for enemy_bullet_i in enemy_bullet_group:
                enemy_bullet_i.kill()
            for player_bullet_i in player_bullet_group:
                player_bullet_i.kill()
            enemy_next_time = pygame.time.get_ticks()
            pygame.display.update()
        # quit game
        if event_over.key == pygame.K_q:
            pygame.quit()
            sys.exit()


# state variables for start_game function
game_start = True
time_event = pygame.USEREVENT + 0
pygame.time.set_timer(time_event, 1000)
blink_end_time = 0


def start_game():
    """Handles the "Start Game" screen

    Listens to user-input for starting the game (Space)
    """

    global game_start, start_text, blink_end_time, now, enemy_next_time
    event_start = pygame.event.wait()
    current_time = pygame.time.get_ticks()
    if event_start.type == pygame.KEYDOWN:
        # start game
        if event_start.key == pygame.K_SPACE:
            game_start = False
            enemy_next_time = pygame.time.get_ticks()
            return
    # for blinking text
    if event_start.type == time_event:
        while current_time > blink_end_time:
            blink_end_time += 20
            screen.blit(start_text, start_text.get_rect(center=(1.2 * WIDTH / 2, 0.65 * HEIGHT / 2)))
            pygame.display.update()


# Main game loop for running procedural code
gameIsRunning = True
while gameIsRunning:
    start = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

    # player bullets
    wait = 100
    now = pygame.time.get_ticks()
    key_pressed = pygame.key.get_pressed()
    if now > player_next_time:
        player_next_time += wait
        if key_pressed[K_z]:
            player_bullet_group.add(player1.create_bullet())

    # check for collisions between player and enemy bullets
    for enemy_bullet in enemy_bullet_group:
        if enemy_bullet.rect.colliderect(player1.hitbox):
            player1.lives -= 1
            enemy_bullet.kill()

    # check for collisions between enemy and player bullets
    for player_bullet in player_bullet_group:
        if player_bullet.rect.colliderect(enemy.rect):
            player_bullet.kill()
            enemy.health -= 100

    # start screen
    while game_start:
        screen.fill((199, 120, 0))
        start_img = pygame.image.load("images/start.png")
        screen.blit(start_img, (0, 0))
        screen.blit(welcome, welcome.get_rect(center=(1.1 * WIDTH / 3, 100)))
        screen.blit(move, move.get_rect(center=(1.55 * WIDTH / 2, 1.3 * HEIGHT / 2)))
        screen.blit(shift, shift.get_rect(center=(1.48 * WIDTH / 2, 1.43 * HEIGHT / 2)))
        screen.blit(shoot, shoot.get_rect(center=(1.4 * WIDTH / 2, 1.57 * HEIGHT / 2)))
        pygame.display.update()
        start_game()

    # Update player and player_bullet_group states
    player1.update()
    player_bullet_group.update()

    # Draw background
    screen.fill((40, 127, 71))
    bg_img = pygame.image.load("images/background grass.png")
    bg_height = bg_img.get_width()
    for y in range(2):
        screen.blit(bg_img, (0, ((y * -bg_height) - bg_scroll)))
    if abs(bg_scroll) > bg_height:
        bg_scroll = 0
    bg_scroll -= 1

    # Draw objects on top of the background
    player1.draw(screen)
    player_bullet_group.draw(screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)
    enemy_group.draw(screen)

    # Draw lives for player and enemy
    draw_lives(screen, 500, 566, player1.lives, heart)
    draw_health_bar(screen, 300, 20, enemy.health, enemy.max_health)

    # determine enemy movement and bullet patterns
    # could be made more concise/reusable by using look-up tables
    now = pygame.time.get_ticks()

    if enemy.health >= enemy.max_health * (4 / 5): # % of enemy health
        enemy.move_in_pattern(path_pattern_1, 2) # pattern 1 with speed 2

        if now > enemy_next_time:
            enemy_next_time += 1000 # every 1000th frame
            do_bullet_pattern(4, 4, 0)

    elif enemy.health >= enemy.max_health * (3 / 5):
        enemy.move_in_pattern(path_pattern_2, 5)

        if now > enemy_next_time:
            enemy_next_time += 600
            do_bullet_pattern(6, 4, 0)

    elif enemy.health >= enemy.max_health * (2 / 5):
        enemy.move_in_pattern(path_pattern_3, 3)

        if now > enemy_next_time:
            enemy_next_time += 100
            spin += 30
            do_bullet_pattern(5, 4, spin % 360)

    elif enemy.health >= enemy.max_health * (1 / 5):
        enemy.move_in_pattern(path_pattern_4, 5)

        if now > enemy_next_time:
            enemy_next_time += 400
            do_bullet_pattern(12, 2, 0)

    elif enemy.health > enemy.max_health * (0 / 5):
        enemy.move_in_pattern(path_pattern_5, 20)

        if now > enemy_next_time:
            enemy_next_time += 200
            do_bullet_pattern(28, 2, 0)

    elif enemy.health <= 0: # game over if enemy dies
        screen.fill((0, 0, 0))
        screen.blit(game_over, game_over.get_rect(center=(WIDTH / 2, 220)))
        screen.blit(you_win, you_win.get_rect(center=screen.get_rect().center))
        screen.blit(restart, restart.get_rect(center=(WIDTH / 2, 360)))
        screen.blit(quit_text, quit_text.get_rect(center=(WIDTH / 2, 420)))
        pygame.display.update()
        handle_game_over()

    # game over if player has no more lives
    if player1.lives <= 0:
        screen.fill((0, 0, 0))
        screen.blit(game_over, game_over.get_rect(center=(WIDTH / 2, 220)))
        screen.blit(you_lost, you_lost.get_rect(center=screen.get_rect().center))
        screen.blit(restart, restart.get_rect(center=(WIDTH / 2, 360)))
        screen.blit(quit_text, quit_text.get_rect(center=(WIDTH / 2, 420)))
        pygame.display.update()
        handle_game_over()

    # Update the screen at 60 FPS
    pygame.display.flip()
    clock.tick(60)

# Quit when game loop ends
pygame.quit()
