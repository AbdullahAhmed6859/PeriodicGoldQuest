import pygame
from random import randint
from dice import Dice
from constants import *

# initialising pygame
pygame.init()

scrn = pygame.display.set_mode(SCREEN_DIMENSIONS)  # setting the screen
scrn.fill((pygame.Color("antiquewhite")))

pygame.display.set_caption("Periodic Gold Quest")  # title of the game

player1aimg = pygame.image.load(
    IMG_PATH+"spider red.png")  # images of both players
player1aimg = pygame.transform.scale(
    player1aimg, (WIDTH, HEIGHT))  # changing image size
player2aimg = pygame.image.load(IMG_PATH+"spider blue.png")
player2aimg = pygame.transform.scale(player2aimg, (WIDTH, HEIGHT))
player1bimg = pygame.image.load(
    IMG_PATH+"bat red.png")  # images of both players
player1bimg = pygame.transform.scale(
    player1bimg, (WIDTH, HEIGHT))  # changing image size
player2bimg = pygame.image.load(IMG_PATH+"bat blue.png")
player2bimg = pygame.transform.scale(player2bimg, (WIDTH, HEIGHT))


# setting up the sound effects
superhero_sound = pygame.mixer.Sound(SOUND_PATH + 'move-self.mp3')
superhero_sound.set_volume(0.5)

hero_die_sound = pygame.mixer.Sound(SOUND_PATH + 'notify.mp3')
hero_die_sound.set_volume(0.5)

dice_sound = pygame.mixer.Sound(SOUND_PATH + 'dice_roll.mp3')
dice_sound.set_volume(0.5)

# setting up the dice
dice = Dice(DICE_IMAGES, dice_sound)


# showing the heros on the screen
def player1():
    scrn.blit(player1aimg, (x1a, y1a))
    scrn.blit(player1bimg, (x1b, y1b))


def player2():
    scrn.blit(player2aimg, (x2a, y2a))
    scrn.blit(player2bimg, (x2b, y2b))


def radioactive():
    # showing a radioactive line on the screen.
    pygame.draw.line(scrn, (pygame.Color("lightsteelblue4")),
                     (209, 345), (209, 413+68), 7)


def drawhome():
    # Draw the home screen on the game window.
    xh = 200
    yh = 15
    pygame.draw.rect(scrn, (pygame.Color("darkseagreen2")),
                     (xh, yh, 72*4, 77*2))
    font = pygame.font.Font("freesansbold.ttf", 38)
    head = font.render("HOME", True, (pygame.Color("darkseagreen3")))
    scrn.blit(head, (xh+(72), yh+3))
    font2 = pygame.font.Font("freesansbold.ttf", 18)
    ins = font2.render("Hold on to 'i' for instructions",
                       True, (pygame.Color("goldenrod3")))
    scrn.blit(ins, (821, 5))


def instructions():
    # Display the instructions on the screen.
    font = pygame.font.Font("freesansbold.ttf", 20)
    scrn.fill((pygame.Color("antiquewhite")))
    x_offset = 68
    y_offset = 120
    instructions_list = [
        (pygame.Color("lightgoldenrod1"),
         "Grp1 and Grp7 elements reacting and ending at colored positions", (141, 73)),
        (pygame.Color("pink2"),
         "Grp2 and Grp6 elements reacting and ending at colored positions", (141, 113)),
        (pygame.Color("indianred2"),
         "Poisonous elements return player to home", (141, 153)),
        (pygame.Color("lightsteelblue3"),
         "Radioactive elements attack opponent", (141, 193)),
        (pygame.Color("cyan2"), "Shield protects from attack of opponent", (141, 233)),
        (pygame.Color("darkgoldenrod"),
         "Player wins when it reaches Gold(Au)", (141, 273))
    ]

    for color, description, position in instructions_list:
        x_pos = position[0] + x_offset
        y_pos = position[1] + y_offset
        pygame.draw.rect(scrn, color, (x_pos, y_pos, 34, 34))
        pygame.draw.rect(scrn, pygame.Color("lightgoldenrod4"),
                         (x_pos, y_pos, 34, 34), 1)
        instruction_text = font.render(
            description, True, pygame.Color("azure4"))
        scrn.blit(instruction_text, (x_pos+x_offset, y_pos + 7))
    pygame.draw.rect(scrn, (pygame.Color("gold1")),
                     (141+x_offset, 273+120, 34, 34), 3)


atomic = {}


def drawboard():  # drawing periodic table and color coding
    global atomic
    x_co = 5
    y_co = 5
    atomicnum = 1  # elements dictionary

    font = pygame.font.Font("freesansbold.ttf", 38)
    font2 = pygame.font.Font("freesansbold.ttf", 20)

    for x in range(ROWS):
        for y in range(COLUMNS):
            if x == 0 and y > 0 and y < 17:
                pass
            elif x in (1, 2) and y > 1 and y < 12:
                pass
            elif x in (7, 8) and y < 4:
                pass
            elif (y in (0, 16) and x < 7) or (x == 4 and y == 9) or (x == 8 and y == 9):
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod1")), (x_co, y_co, 68, 68))
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod4")), (x_co, y_co, 68, 68), 1)
                element = font.render(
                    ELEMENTS[atomicnum], True, (pygame.Color("lightgoldenrod3")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            elif (y in (1, 15) and x < 7) or (x == 4 and y == 4) or (x == 6 and y == 5):
                pygame.draw.rect(scrn, (pygame.Color("pink2")),
                                 (x_co, y_co, 68, 68))
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod4")), (x_co, y_co, 68, 68), 1)
                element = font.render(
                    ELEMENTS[atomicnum], True, (pygame.Color("pink3")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            elif y == 10 and x == 5:
                pygame.draw.rect(
                    scrn, (pygame.Color("darkgoldenrod")), (x_co-1, y_co, 69, 68))
                pygame.draw.rect(scrn, (pygame.Color("gold1")),
                                 (x_co, y_co, 68, 68), 3)
                element = font.render(
                    ELEMENTS[atomicnum], True, (pygame.Color("gold1")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            elif (x in (4, 5) and y == 11) or (x == 3 and y == 14) or (x == 3 and y in (6, 8)) or (x == 5 and y == 12) or (x == 4 and y == 13) or (x == 6 and y == 3):
                pygame.draw.rect(
                    scrn, (pygame.Color("indianred2")), (x_co, y_co, 68, 68))
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod4")), (x_co, y_co, 68, 68), 1)
                element = font.render(
                    ELEMENTS[atomicnum], True, (pygame.Color("indianred3")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            elif (x == 3 and y in (3, 4, 5, 7)) or (x == 1 and y == 13) or (x == 4 and y == 3) or (x == 5 and y in (4, 5, 7, 9, 13)):
                pygame.draw.rect(scrn, (pygame.Color("cyan2")),
                                 (x_co, y_co, 68, 68))
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod4")), (x_co, y_co, 68, 68), 1)
                element = font.render(
                    ELEMENTS[atomicnum], True, (pygame.Color("cyan3")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                SHIELD.append(atomicnum)
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            elif x > 6:
                pygame.draw.rect(
                    scrn, (pygame.Color("lightsteelblue3")), (x_co, y_co, 68, 68))
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod4")), (x_co, y_co, 68, 68), 1)
                element = font.render(
                    ELEMENTS[atomicnum], True, (pygame.Color("lightsteelblue4")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                RADIOACTIVE_EL.append(atomicnum)
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            else:
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod4")), (x_co, y_co, 68, 68), 1)
                element = font.render(
                    ELEMENTS[atomicnum], True, (pygame.Color("antiquewhite3")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            if x == 5 and y == 2:
                atomicnum = 72
            elif x == 6 and y == 2:
                atomicnum = 104
            elif x == 7 and y == 3:
                atomicnum = 58
            elif x == 8 and y == 3:
                atomicnum = 90

            x_co += 68
        y_co += 68
        x_co = 5


def check_posion(coors):  # checking if the position is poisonous
    y, x = coors[0]//68, coors[1]//68
    result = (x in (4, 5) and y == 11) or (x == 3 and y == 14) or (x == 3 and y in (
        6, 8)) or (x == 5 and y == 12) or (x == 4 and y == 13) or (x == 6 and y == 3)
    # print(x, y, result)
    return result


def gamewin():  # main game window with all display helper functions
    # to hide previous traces with black colour(bg)
    scrn.fill((pygame.Color("antiquewhite")))
    drawboard()
    drawhome()
    player1()
    player2()
    radioactive()
    dice.dice_simulation(dice_num, scrn)


def views(view):
    if view == "i":
        instructions()
    if view == "g":
        gamewin()


def movingforward1a(current, next):
    global atomic, x1a, y1a, atomicnum1a

    if current == next:
        x1a = atomic[current][0]+5
        y1a = atomic[current][1]+5
        views(view)
        pygame.display.update()
        superhero_sound.play()
        pygame.time.delay(1000//SUPERHERO_SPEED)
        atomicnum1a = next
    else:
        x1a = atomic[current][0]+5
        y1a = atomic[current][1]+5
        views(view)
        pygame.display.update()
        superhero_sound.play()
        pygame.time.delay(1000//SUPERHERO_SPEED)
        movingforward1a(current+1, next)


def movingforward2a(current, next):
    global atomic, x2a, y2a, atomicnum2a

    if current == next:
        x2a = atomic[current][0]+5
        y2a = atomic[current][1]+5
        views(view)
        pygame.display.update()
        superhero_sound.play()
        pygame.time.delay(1000//SUPERHERO_SPEED)
        atomicnum2a = next
    else:
        x2a = atomic[current][0]+5
        y2a = atomic[current][1]+5
        views(view)
        pygame.display.update()
        superhero_sound.play()
        pygame.time.delay(1000//SUPERHERO_SPEED)
        movingforward2a(current+1, next)


def movingforward1b(current, next):
    global atomic, x1b, y1b, atomicnum1b

    if current == next:
        x1b = atomic[current][0]+5
        y1b = atomic[current][1]+5
        views(view)
        pygame.display.update()
        superhero_sound.play()
        pygame.time.delay(1000//SUPERHERO_SPEED)
        atomicnum1b = next
    else:
        x1b = atomic[current][0]+5
        y1b = atomic[current][1]+5
        views(view)
        pygame.display.update()
        superhero_sound.play()
        pygame.time.delay(1000//SUPERHERO_SPEED)
        movingforward1b(current-1, next)


def movingforward2b(current, next):
    global atomic, x2b, y2b, atomicnum2b

    if current == next:
        x2b = atomic[current][0]+5
        y2b = atomic[current][1]+5
        views(view)
        pygame.display.update()
        superhero_sound.play()
        pygame.time.delay(1000//SUPERHERO_SPEED)
        atomicnum2b = next
    else:
        x2b = atomic[current][0]+5
        y2b = atomic[current][1]+5
        views(view)
        pygame.display.update()
        superhero_sound.play()
        pygame.time.delay(1000//SUPERHERO_SPEED)
        movingforward2b(current-1, next)


# Atomic numer of SuperHeroes
atomicnum1a = 0
atomicnum2a = 0
atomicnum1b = 119
atomicnum2b = 119
# to switch turns: if turn is even then player 1 else player 2
turn = 0
dice_num = 0
# main loop
run = True
while run:
    # to delay the game
    for event in pygame.event.get():  # all inputs from user are events
        if event.type == pygame.QUIT:
            run = False  # for quitting the game
        view = "g"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and event.type == pygame.KEYDOWN:
            dice_num = randint(1, 6)
            dice.dice_animation(scrn, lambda: views("g"))
            dice.dice_simulation(dice_num, scrn)
            if turn % 2 == 0 and atomicnum1a+dice_num <= 79:
                movingforward1a(atomicnum1a+1, atomicnum1a+dice_num)
                if check_posion(atomic[atomicnum1a]):
                    atomicnum1a = 0
                    x1a, y1a = HOME_CORS["1a"]
                    hero_die_sound.play()
                if atomicnum1a in RADIOACTIVE_EL and atomicnum2a not in SHIELD and atomicnum2a not in RADIOACTIVE_EL:
                    atomicnum2a = 0
                    x2a, y2a = HOME_CORS["2a"]
                    hero_die_sound.play()
                if atomicnum1a in RADIOACTIVE_EL and atomicnum2b not in SHIELD and atomicnum2b not in RADIOACTIVE_EL:
                    atomicnum2b = 119
                    x2b, y2b = HOME_CORS["2b"]
                    hero_die_sound.play()
                if atomicnum1a in GRP1 and atomicnum1b in GRP7 or atomicnum1a in GRP7 and atomicnum1b in GRP1:
                    atomicnum1a = 46
                    atomicnum1b = 95
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
                if atomicnum1a in GRP2 and atomicnum1b in GRP6 or atomicnum1a in GRP6 and atomicnum1b in GRP2:
                    atomicnum1a = 41
                    atomicnum1b = 106
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
            elif turn % 2 != 0 and atomicnum2a+dice_num <= 79:
                movingforward2a(atomicnum2a+1, atomicnum2a+dice_num)
                if check_posion(atomic[atomicnum2a]):
                    atomicnum2a = 0
                    x2a, y2a = HOME_CORS["2a"]
                    hero_die_sound.play()
                if atomicnum2a in RADIOACTIVE_EL and atomicnum1a not in SHIELD and atomicnum1a not in RADIOACTIVE_EL:
                    atomicnum1a = 0
                    x1a, y1a = HOME_CORS["1a"]
                    hero_die_sound.play()
                if atomicnum2a in RADIOACTIVE_EL and atomicnum1b not in SHIELD and atomicnum1b not in RADIOACTIVE_EL:
                    atomicnum1b = 119
                    x1b, y1b = HOME_CORS["1b"]
                    hero_die_sound.play()
                if atomicnum1a in GRP1 and atomicnum1b in GRP7 or atomicnum1a in GRP7 and atomicnum1b in GRP1:
                    atomicnum1a = 46
                    atomicnum1b = 95
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
                if atomicnum2a in GRP2 and atomicnum2b in GRP6 or atomicnum2a in GRP6 and atomicnum2b in GRP2:
                    atomicnum2a = 41
                    atomicnum2b = 106
                    x2a, y2a = atomic[atomicnum2a][0] + \
                        5, atomic[atomicnum2a][1]+5
                    x2b, y2b = atomic[atomicnum2b][0] + \
                        5, atomic[atomicnum2b][1]+5

            turn += 1
        elif keys[pygame.K_2] and event.type == pygame.KEYDOWN:
            dice_num = randint(1, 6)
            dice.dice_animation(scrn, lambda: views("g"))
            dice.dice_simulation(dice_num, scrn)
            if turn % 2 == 0 and atomicnum1b-dice_num >= 79:
                movingforward1b(atomicnum1b-1, atomicnum1b-dice_num)

                if check_posion(atomic[atomicnum1b]):
                    atomicnum1b = 119
                    x1b, y1b = HOME_CORS["1b"]
                    hero_die_sound.play()
                if atomicnum1b in RADIOACTIVE_EL and atomicnum2a not in SHIELD and atomicnum2a not in RADIOACTIVE_EL:
                    atomicnum2a = 0
                    x2a, y2a = HOME_CORS["2a"]
                    hero_die_sound.play()
                if atomicnum1b in RADIOACTIVE_EL and atomicnum2b not in SHIELD and atomicnum2b not in RADIOACTIVE_EL:
                    atomicnum2b = 119
                    x2b, y2b = HOME_CORS["2b"]
                    hero_die_sound.play()
                if atomicnum1a in GRP1 and atomicnum1b in GRP7 or atomicnum1a in GRP7 and atomicnum1b in GRP1:
                    atomicnum1a = 46
                    atomicnum1b = 95
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
                if atomicnum1a in GRP2 and atomicnum1b in GRP6 or atomicnum1a in GRP6 and atomicnum1b in GRP2:
                    atomicnum1a = 41
                    atomicnum1b = 106
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5

            elif turn % 2 != 0 and atomicnum2b-dice_num >= 79:
                movingforward2b(atomicnum2b-1, atomicnum2b-dice_num)

                if check_posion(atomic[atomicnum2b]):
                    atomicnum2b = 119
                    x2b, y2b = HOME_CORS["2b"]
                    hero_die_sound.play()
                if atomicnum2b in RADIOACTIVE_EL and atomicnum1a not in SHIELD and atomicnum1a not in RADIOACTIVE_EL:
                    atomicnum1a = 0
                    x1a, y1a = HOME_CORS["1a"]
                    hero_die_sound.play()
                if atomicnum2b in RADIOACTIVE_EL and atomicnum1b not in SHIELD and atomicnum1b not in RADIOACTIVE_EL:
                    atomicnum1b = 119
                    x1b, y1b = HOME_CORS["1b"]
                    hero_die_sound.play()
                if atomicnum1a in GRP1 and atomicnum1b in GRP7 or atomicnum1a in GRP7 and atomicnum1b in GRP1:
                    atomicnum1a = 46
                    atomicnum1b = 95
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
                if atomicnum2a in GRP2 and atomicnum2b in GRP6 or atomicnum2a in GRP6 and atomicnum2b in GRP2:
                    atomicnum2a = 41
                    atomicnum2b = 106
                    x2a, y2a = atomic[atomicnum2a][0] + \
                        5, atomic[atomicnum2a][1]+5
                    x2b, y2b = atomic[atomicnum2b][0] + \
                        5, atomic[atomicnum2b][1]+5

            turn += 1
            pygame.display.update()

        elif keys[pygame.K_i]:
            view = "i"

        views(view)
        pygame.display.update()  # to update changes on screen

    pygame.time.delay(100)
pygame.quit()
