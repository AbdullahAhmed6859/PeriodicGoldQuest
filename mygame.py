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

blip_sound = pygame.mixer.Sound(SOUND_PATH + 'notify.mp3')
blip_sound.set_volume(0.5)

dice_sound = pygame.mixer.Sound(SOUND_PATH + 'dice_roll.mp3')
dice_sound.set_volume(0.5)

teleport_sound = pygame.mixer.Sound(SOUND_PATH + 'teleport.wav')
teleport_sound.set_volume(0.5)

win_sound = pygame.mixer.Sound(SOUND_PATH + 'win.mp3')
win_sound.set_volume(1)
# setting up the dice
dice = Dice(DICE_IMAGES, dice_sound)


# showing the heros on the screen
def player1():
    scrn.blit(player1aimg, (x1a, y1a))
    scrn.blit(player1bimg, (x1b, y1b))


def player2():
    scrn.blit(player2aimg, (x2a, y2a))
    scrn.blit(player2bimg, (x2b, y2b))


def reset_coors():
    #to send heroes back to home
    global x1a, y1a, x2a, y2a, x1b, y1b, x2b, y2b, atomicnum1a, atomicnum2a, atomicnum1b, atomicnum2b
    x1a = 5+68+68+68
    y1a = 5+68
    x2a = 5+68+68+68+68+68
    y2a = 5+68
    x1b = 5+68+68+68+68
    y1b = 5+68
    x2b = 5+68+68+68+68+68+68
    y2b = 5+68
    atomicnum1a = 0
    atomicnum2a = 0
    atomicnum1b = 119
    atomicnum2b = 119


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


def updates(player):
    # Draw the home screen on the game window.
    xh = 492
    yh = 15
    pygame.draw.rect(scrn, (pygame.Color("burlywood3")),
                     (xh, yh, 72*4, 70*2))
    font = pygame.font.Font("freesansbold.ttf", 38)
    head = font.render(player, True, (pygame.Color("burlywood4")))
    scrn.blit(head, (xh+(60), yh+40))


def instructions():
    # Display the instructions on the screen.
    scrn.fill((pygame.Color("antiquewhite")))
    font = pygame.font.Font("freesansbold.ttf", 20)
    instruction_text = font.render(">>RED IS PLAYER 1(HERO 1+HERO2) BLUE IS PLAYER 2(HERO 1+HERO2)", True, pygame.Color("azure4"))
    scrn.blit(instruction_text, (141, 43))
    instruction_text = font.render(">>HEROES 1 START FROM ATOMIC NUMBER 1, HEROES 2 START FROM ATOMIC NUMBER 118 ", True, pygame.Color("azure4"))
    scrn.blit(instruction_text, (141, 63))
    instruction_text = font.render(">>MAKE ANY OF YOUR HEROES REACH GOLD TO WIN", True, pygame.Color("azure4"))
    scrn.blit(instruction_text, (141, 83))
    instruction_text = font.render(">>PRESS 'SPACE' TO ROLL DICE", True, pygame.Color("azure4"))
    scrn.blit(instruction_text, (141, 103))
    instruction_text = font.render(">>PRESS '1' TO MOVE YOR HERO 1\n PRESS '2' TO MOVE HERO 2", True, pygame.Color("azure4"))
    scrn.blit(instruction_text, (141, 123))
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
        #drawing groups and periods
        for y in range(COLUMNS):
            if x == 0 and y > 0 and y < 17:
                pass
            elif x in (1, 2) and y > 1 and y < 12:
                pass
            elif x in (7, 8) and y < 4:
                pass
            elif (y in (0, 16) and x < 7) or (x == 4 and y == 9) or (x == 8 and y == 9):
                #grp 1 and 7 elements color coded
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
                #group 2 and 6 elements color coded
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
                #Gold Color coded
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
                #poisonous elements
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
                #shield
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
                #radioactive elements color coded 
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


player = "PLAYER 1"


def gamewin():  # main game window with all display helper functions
    # to hide previous traces with black colour(bg)
    global player
    scrn.fill((pygame.Color("antiquewhite")))
    drawboard()
    drawhome()
    updates(player)
    player1()
    player2()
    radioactive()
    dice.dice_simulation(dice_num, scrn)


def winning(player):
    #showing winner on screen
    global win
    win_sound.play()
    pygame.draw.ellipse(
        scrn, (pygame.Color("gold")), (300, 100, 400, 200))
    font = pygame.font.Font("freesansbold.ttf", 38)
    TEXT = font.render(player+" WINS!", True, (pygame.Color("darkgoldenrod")))
    scrn.blit(TEXT, (370, 170))
    pygame.display.update()
    win = False
    pygame.time.delay(5000)
    reset_coors()
    pygame.display.update()


def views(view):
    #showing game window and instruction window
    if view == "i":
        instructions()
    if view == "g":
        gamewin()


def movingforward1a(current, next):
    #recursive loop for moving player
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
    #recursive loop for moving player
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
    #recursive loop for moving player
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
    #recursive loop for moving player
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
dicerun = True
win = False
# main loop
run = True
while run:
    # to delay the game
    for event in pygame.event.get():  # all inputs from user are events
        if event.type == pygame.QUIT:
            run = False  # for quitting the game
        view = "g"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and dicerun == True:
            #to roll the dice
            dice_num = randint(1, 6)
            dice.dice_animation(scrn, lambda: views("g"))
            dice.dice_simulation(dice_num, scrn)
            views(view)
            pygame.display.update()
            dicerun = False

        elif keys[pygame.K_1] and event.type == pygame.KEYDOWN and dicerun == False:
            # to move player's first tile
            if turn % 2 == 0 and atomicnum1a+dice_num <= 79:
                #player 1 turn
                movingforward1a(atomicnum1a+1, atomicnum1a+dice_num)
                if check_posion(atomic[atomicnum1a]):
                    atomicnum1a = 0
                    x1a, y1a = HOME_CORS["1a"]
                    blip_sound.play()
                if atomicnum1a in RADIOACTIVE_EL and atomicnum2a not in SHIELD and atomicnum2a not in RADIOACTIVE_EL:
                    atomicnum2a = 0
                    x2a, y2a = HOME_CORS["2a"]
                    blip_sound.play()
                if atomicnum1a in RADIOACTIVE_EL and atomicnum2b not in SHIELD and atomicnum2b not in RADIOACTIVE_EL:
                    atomicnum2b = 119
                    x2b, y2b = HOME_CORS["2b"]
                    blip_sound.play()
                if atomicnum1a in GRP1 and atomicnum1b in GRP7 or atomicnum1a in GRP7 and atomicnum1b in GRP1:
                    atomicnum1a = 46
                    atomicnum1b = 95
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
                    teleport_sound.play()
                if atomicnum1a in GRP2 and atomicnum1b in GRP6 or atomicnum1a in GRP6 and atomicnum1b in GRP2:
                    atomicnum1a = 41
                    atomicnum1b = 106
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
                    teleport_sound.play()
                if atomicnum1a == 79:
                    win = True
                    winner = "PLAYER1"
                player = "PLAYER 2"

            elif turn % 2 != 0 and atomicnum2a+dice_num <= 79:
                #player 2 turn
                movingforward2a(atomicnum2a+1, atomicnum2a+dice_num)
                if check_posion(atomic[atomicnum2a]):
                    atomicnum2a = 0
                    x2a, y2a = HOME_CORS["2a"]
                    blip_sound.play()
                if atomicnum2a in RADIOACTIVE_EL and atomicnum1a not in SHIELD and atomicnum1a not in RADIOACTIVE_EL:
                    atomicnum1a = 0
                    x1a, y1a = HOME_CORS["1a"]
                    blip_sound.play()
                if atomicnum2a in RADIOACTIVE_EL and atomicnum1b not in SHIELD and atomicnum1b not in RADIOACTIVE_EL:
                    atomicnum1b = 119
                    x1b, y1b = HOME_CORS["1b"]
                    blip_sound.play()
                if atomicnum2a in GRP1 and atomicnum2b in GRP7 or atomicnum2a in GRP7 and atomicnum2b in GRP1:
                    atomicnum2a = 46
                    atomicnum2b = 95
                    x2a, y2a = atomic[atomicnum2a][0] + \
                        5, atomic[atomicnum2a][1]+5
                    x2b, y2b = atomic[atomicnum2b][0] + \
                        5, atomic[atomicnum2b][1]+5
                    teleport_sound.play()
                if atomicnum2a in GRP2 and atomicnum2b in GRP6 or atomicnum2a in GRP6 and atomicnum2b in GRP2:
                    atomicnum2a = 41
                    atomicnum2b = 106
                    x2a, y2a = atomic[atomicnum2a][0] + \
                        5, atomic[atomicnum2a][1]+5
                    x2b, y2b = atomic[atomicnum2b][0] + \
                        5, atomic[atomicnum2b][1]+5
                    teleport_sound.play()
                if atomicnum2a == 79:
                    win = True
                    winner = "PLAYER2"
                player = "PLAYER 1"

            turn += 1
            dicerun = True
        elif keys[pygame.K_2] and event.type == pygame.KEYDOWN and dicerun == False:
            # to move player's second tile
            if turn % 2 == 0 and atomicnum1b-dice_num >= 79:
                #player 1 turn
                player = "PLAYER 1"
                movingforward1b(atomicnum1b-1, atomicnum1b-dice_num)

                if check_posion(atomic[atomicnum1b]):
                    atomicnum1b = 119
                    x1b, y1b = HOME_CORS["1b"]
                    blip_sound.play()
                if atomicnum1b in RADIOACTIVE_EL and atomicnum2a not in SHIELD and atomicnum2a not in RADIOACTIVE_EL:
                    atomicnum2a = 0
                    x2a, y2a = HOME_CORS["2a"]
                    blip_sound.play()
                if atomicnum1b in RADIOACTIVE_EL and atomicnum2b not in SHIELD and atomicnum2b not in RADIOACTIVE_EL:
                    atomicnum2b = 119
                    x2b, y2b = HOME_CORS["2b"]
                    blip_sound.play()
                if atomicnum1a in GRP1 and atomicnum1b in GRP7 or atomicnum1a in GRP7 and atomicnum1b in GRP1:
                    atomicnum1a = 46
                    atomicnum1b = 95
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
                    teleport_sound.play()
                if atomicnum1a in GRP2 and atomicnum1b in GRP6 or atomicnum1a in GRP6 and atomicnum1b in GRP2:
                    atomicnum1a = 41
                    atomicnum1b = 106
                    x1a, y1a = atomic[atomicnum1a][0] + \
                        5, atomic[atomicnum1a][1]+5
                    x1b, y1b = atomic[atomicnum1b][0] + \
                        5, atomic[atomicnum1b][1]+5
                    teleport_sound.play()
                if atomicnum1b == 79:
                    win = True
                    winner = "PLAYER1"
                player = "PLAYER 2"

            elif turn % 2 != 0 and atomicnum2b-dice_num >= 79:
                #player 2 turn
                player = "PLAYER 2"
                movingforward2b(atomicnum2b-1, atomicnum2b-dice_num)

                if check_posion(atomic[atomicnum2b]):
                    atomicnum2b = 119
                    x2b, y2b = HOME_CORS["2b"]
                    blip_sound.play()
                if atomicnum2b in RADIOACTIVE_EL and atomicnum1a not in SHIELD and atomicnum1a not in RADIOACTIVE_EL:
                    atomicnum1a = 0
                    x1a, y1a = HOME_CORS["1a"]
                    blip_sound.play()
                if atomicnum2b in RADIOACTIVE_EL and atomicnum1b not in SHIELD and atomicnum1b not in RADIOACTIVE_EL:
                    atomicnum1b = 119
                    x1b, y1b = HOME_CORS["1b"]
                    blip_sound.play()
                if atomicnum2a in GRP1 and atomicnum2b in GRP7 or atomicnum2a in GRP7 and atomicnum2b in GRP1:
                    atomicnum2a = 46
                    atomicnum2b = 95
                    x2a, y2a = atomic[atomicnum2a][0] + \
                        5, atomic[atomicnum2a][1]+5
                    x2b, y2b = atomic[atomicnum2b][0] + \
                        5, atomic[atomicnum2b][1]+5
                    teleport_sound.play()
                if atomicnum2a in GRP2 and atomicnum2b in GRP6 or atomicnum2a in GRP6 and atomicnum2b in GRP2:
                    atomicnum2a = 41
                    atomicnum2b = 106
                    x2a, y2a = atomic[atomicnum2a][0] + \
                        5, atomic[atomicnum2a][1]+5
                    x2b, y2b = atomic[atomicnum2b][0] + \
                        5, atomic[atomicnum2b][1]+5
                    teleport_sound.play()
                if atomicnum2b == 79:
                    win = True
                    winner = "PLAYER2"
                player = "PLAYER 1"
            dicerun = True

            turn += 1
            pygame.display.update()

        elif keys[pygame.K_i]:
            view = "i"

        views(view)
        if win == True:
            winning(winner)
        pygame.display.update()  # to update changes on screen

    pygame.time.delay(100)
pygame.quit()
