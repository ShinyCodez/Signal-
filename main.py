import pygame
from fox import Fox
from coin import Coin
import random
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Signal!")

# set up variables for the display
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 889
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
nuke = "nuke.png"
nuke_speed = 0.2

name = "Collect the Wifi Signal As Fast As You Can!"
nuke = pygame.image.load(nuke)
nuke = pygame.transform.scale(nuke, (75, 75))
r = 255
g = 255
b = 255
current_time = time.time()
nuke_x = random.randint(0, SCREEN_WIDTH)
nuke_y = -50

# render the text for later
display_name = my_font.render(name, True, (0, 0, 0))
f = Fox(40, 60)
c = Coin(200, 85)
clicks = 0

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
start = True
end = False
game = False
time_10 = 100

def speed_up():
    f.is_sped_up = True

# -------- Main Program Loop -----------
while run:
    # title screen
    if start == True:
        pygame.display.update()
        screen.fill((r, g, b))
        title_screen = my_font.render("Use WASD to collect coins to move the Fox!", True, (0, 0, 0))
        title_screen_2 = my_font.render("Collect Wifi to Earn a Better Signal!", True, (0, 0, 0))
        title_screen_3 = my_font.render("Press Space For a Speed Boost!", True, (0,0,0))
        title_screen_4 = my_font.render("Press any Key to Continue!", True, (0, 0, 0))
        screen.blit(title_screen, (140, 130))
        screen.blit(title_screen_2, (160, 150))
        screen.blit(title_screen_3, (170, 170))
        screen.blit(title_screen_4, (182, 190))
        for event in pygame.event.get():  # User did something
            if event.type == pygame.KEYDOWN:
                game = True
                start = False
                current_time = time.time()
            if event.type == pygame.QUIT:  # If user clicked close
                run = False

    # movement
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_w]:
        f.move_direction("up")
    if keys[pygame.K_a]:
        f.move_direction("left")
    if keys[pygame.K_s]:
        f.move_direction("down")
    if keys[pygame.K_d]:
        f.move_direction("right")
    if keys[pygame.K_SPACE]:
        if not f.is_sped_up:
            speed_up()
            f.is_sped_up = True
            speed_message = my_font.render("Speed Up Activated!", True, (0, 0, 0))
            screen.blit(speed_message, (0,60))
    else:
        f.is_sped_up = False
        speed_message = my_font.render("Speed Up Off!", True, (0, 0, 0))
        screen.blit(speed_message, (0, 60))
    # collision
    if f.rect.colliderect(c.rect) and game == True:
        clicks += 10
        screen.fill((r, g, b))
        c.x = random.randint(0, 850)
        c.y = random.randint(0, 450)
        c.set_location(c.x, c.y)
        if clicks == 150:
            game = False
            end = True

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    if clicks < 150 and game == True:
        clicks_display = "Score: " + str(clicks)
        score_display = my_font.render(clicks_display, True, (0, 0, 0))
        current_time_2 = time.time()
        time_10 = round(20 - (round(current_time_2 - current_time, 2)),2)
        if time_10 == 0:
            game = False
            end = True
        nuke_y = nuke_y + nuke_speed
        if nuke_y > SCREEN_HEIGHT:
            nuke_x = random.randint(0, SCREEN_WIDTH)
            nuke_y = -25
        counter_time = ("Time Remaining: " + str(time_10))
        counter_time = my_font.render(counter_time, True, (0, 0, 0))
        screen.fill((r, g, b))
        screen.blit(score_display, (0, 15))
        screen.blit(counter_time, (0, 30))
        screen.blit(display_name, (0, 0))
        screen.blit(f.image, f.rect)
        screen.blit(c.image, c.rect)
        pygame.display.update()

    if (clicks == 150 and end == True) or time_10 == 0:
        game = False
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        end_time = str(round(20 - (round(current_time_2 - current_time, 2)),2))
        display_end_time = my_font.render("Time remaining: " + end_time + "s", True, (0, 0, 0))
        if float(end_time) > 0:
            end_screen_win = my_font.render("You Win!", True, (0, 0, 0))
            end_screen = end_screen_win
        if float(end_time) == 0 and clicks != 1000:
            end = True
            end_screen_loose = my_font.render("You Lose!", True, (0, 0, 0))
            end_screen = end_screen_loose
        screen.fill((r,g,b))
        screen.blit(display_end_time, (45, 80))
        screen.blit(end_screen, (180, 140))
        pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()