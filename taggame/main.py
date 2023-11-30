# import pygame module in this program
import pygame
import numpy

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")



# dimensions of the object
width = 20
height = 20
width2 = 20
height2 = 20

# velocity / speed of movement
vel = 2
vel2 = 2

# Indicates pygame is running
run = True

redscore = 0
bluescore = 0
isbluetagger = True

green = (0, 255, 0)
blue = (0, 0, 128)

white = (255, 255, 255)
true_blue = (0, 0, 255)
true_red = (255, 0, 0)

score_x = 10
score_y = 10
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 10)

starting_position_red = (400,400)
starting_position_blue = (100, 100)

# object current co-ordinates
x = starting_position_red[0]
y = starting_position_red[1]
x2 = starting_position_blue[0]
y2 = starting_position_blue[1]


# create a text surface object,
# on which text is drawn on it.

def detect_collision(rect1, rect2) -> bool:
    collision = pygame.Rect.collidelist(rect1, [rect2])
    # 0 if collide
    # -1 if not collide
    return True if collision == 0 else False

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()



    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:
        # decrement in x co-ordinate
        x -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 500 - width:
        # increment in x co-ordinate
        x += vel

    # if left arrow key is pressed
    if keys[pygame.K_UP] and y > 0:
        # decrement in y co-ordinate
        y -= vel

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and y < 500 - height:
        # increment in y co-ordinate
        y += vel

    # if left arrow key is pressed
    if keys[pygame.K_a] and x2 > 0:
        # decrement in x co-ordinate
        x2 -= vel2

    # if left arrow key is pressed
    if keys[pygame.K_d] and x2 < 500 - width2:
        # increment in x co-ordinate
        x2 += vel2

    # if left arrow key is pressed
    if keys[pygame.K_w] and y2 > 0:
        # decrement in y co-ordinate
        y2 -= vel2

    # if left arrow key is pressed
    if keys[pygame.K_s] and y2 < 500 - height2:
        # increment in y co-ordinate
        y2 += vel2

    # it refreshes the window
    pygame.display.update()

    # completely fill the surface object
    # with black colour
    win.fill((0, 0, 0))

    # drawing object on screen which is rectangle here
    rect1 = pygame.draw.rect(win, (0, 0, 255), (x2, y2, width2, height2))
    # drawing object on screen which is rectangle here
    rect2 = pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    if detect_collision(rect1, rect2):
        if isbluetagger:
            bluescore += 1
        else:
            redscore += 1
        x = starting_position_red[0]
        y = starting_position_red[1]
        x2 = starting_position_blue[0]
        y2 = starting_position_blue[1]
        isbluetagger = not isbluetagger

    if isbluetagger:
        taggerText = "BLUE"
    else:
        taggerText = "RED"

    redscoreText = font.render(f'Red score: {redscore}', True, green, blue)
    bluescoreText = font.render(f'Blue score: {bluescore}', True, green, blue)
    if isbluetagger:
        taggerText = font.render(f'The current tagger is: {taggerText}', True, true_blue, white)
    else:
        taggerText = font.render(f'The current tagger is: {taggerText}', True, true_red, white)

    # create a rectangular object for the
    # text surface object
    redTextRect = redscoreText.get_rect()
    blueTextRect = bluescoreText.get_rect()

    taggerTextRect = taggerText.get_rect()
    # set the center of the rectangular object.
    redTextRect.center = ((score_x // 2) + 400, score_y // 2)
    blueTextRect.center = ((score_x // 2) + 100, score_y // 2)

    taggerTextRect.center = ((score_x // 2) + 250, score_y // 2)

    win.blit(redscoreText, redTextRect)
    win.blit(bluescoreText, blueTextRect)


    win.blit(taggerText, taggerTextRect)

    # it refreshes the window
    pygame.display.update()




# closes the pygame window
pygame.quit()