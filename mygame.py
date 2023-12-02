import pygame
from random import randint, shuffle
import time

IMG_PATH = "images/"
SOUND_PATH = "sounds/"
# superhero dimensions
WIDTH = 60
HEIGHT = WIDTH
VEL = 68  # box dimensions
SCREEN_DIMENSIONS = 1254, 650
SUPERHERO_SPEED = 5  # moving speed
dice_images = ["dice.1.png", "dice.2.png", "dice.3.png",
               "dice.4.png", "dice.5.png", "dice.6.png"]

# CHARACTER INITIAL COORS x1 -> superhero 1  x2 -> superhero 2
x1a = 5+68+68+68
y1a = 5+68
x2a = 5+68+68+68+68+68
y2a = 5+68
x1b = 5+68+68+68+68
y1b = 5+68
x2b = 5+68+68+68+68+68+68
y2b = 5+68

# initialising pygame
pygame.init()

scrn = pygame.display.set_mode(SCREEN_DIMENSIONS)  # setting the screen
scrn.fill((pygame.Color("antiquewhite")))

pygame.display.set_caption("Periodic Gold Quest")  # title of the game

player1aimg = pygame.image.load(
    "images/spider red.png")  # images of both players
player1aimg = pygame.transform.scale(
    player1aimg, (WIDTH, HEIGHT))  # changing image size
player2aimg = pygame.image.load("images/bat blue.png")
player2aimg = pygame.transform.scale(player2aimg, (WIDTH, HEIGHT))
player1bimg = pygame.image.load(
    "images/spider blue.png")  # images of both players
player1bimg = pygame.transform.scale(
    player1bimg, (WIDTH, HEIGHT))  # changing image size
player2bimg = pygame.image.load("images/bat black.png")
player2bimg = pygame.transform.scale(player2bimg, (WIDTH, HEIGHT))
# setting up the sound
superhero_sound = pygame.mixer.Sound(SOUND_PATH + 'move-self.mp3')
superhero_sound.set_volume(0.5)

dice_sound = pygame.mixer.Sound(SOUND_PATH + 'dice_roll.mp3')
dice_sound.set_volume(0.5)


def player1():  # showing character on scrn
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
    x_offset = 50
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
        scrn.blit(instruction_text, (x_pos+270, y_pos + 7))


atomic = {}


def drawboard():  # drawing periodic table and color coding
    global atomic
    rows = 9
    column = 18
    x_co = 5
    y_co = 5
    atomicnum = 1
    elements = {}  # elements dictionary
    element_symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce',
                       'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

    for x in range(len(element_symbols)):  # filling dictionary
        elements[x+1] = element_symbols[x]

    font = pygame.font.Font("freesansbold.ttf", 38)
    font2 = pygame.font.Font("freesansbold.ttf", 20)

    for x in range(rows):
        for y in range(column):
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
                    elements[atomicnum], True, (pygame.Color("lightgoldenrod3")))
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
                    elements[atomicnum], True, (pygame.Color("pink3")))
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
                    elements[atomicnum], True, (pygame.Color("gold1")))
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
                    elements[atomicnum], True, (pygame.Color("indianred3")))
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
                    elements[atomicnum], True, (pygame.Color("cyan3")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            elif x > 6:
                pygame.draw.rect(
                    scrn, (pygame.Color("lightsteelblue3")), (x_co, y_co, 68, 68))
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod4")), (x_co, y_co, 68, 68), 1)
                element = font.render(
                    elements[atomicnum], True, (pygame.Color("lightsteelblue4")))
                scrn.blit(element, (x_co+10, y_co+30))
                num = font2.render(str(atomicnum), True,
                                   (pygame.Color("azure4")))
                scrn.blit(num, (x_co, y_co))
                atomic[atomicnum] = (x_co, y_co)
                atomicnum += 1

            else:
                pygame.draw.rect(
                    scrn, (pygame.Color("lightgoldenrod4")), (x_co, y_co, 68, 68), 1)
                element = font.render(
                    elements[atomicnum], True, (pygame.Color("antiquewhite3")))
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


def dice_animation():
    # Animation of the rolling of a dice and displaying corresponding image.
    time1 = time.time()
    h, w = 150, 150
    x = 7
    y = 490

    dice_sound.play()
    while time.time() - time1 < dice_sound.get_length():
        img = dice_images[randint(0, 5)]
        diceimg = pygame.image.load(
            "images/"+img)  # images of both players
        diceimg = pygame.transform.scale(diceimg, (h, w))
        scrn.blit(diceimg, (x, y))
        pygame.display.update()
        pygame.time.delay(50)
        views("g")


def dice_simulation(num):
    # Simulation of the rolling of a dice and displaying corresponding image.
    h, w = 150, 150
    x = 7
    y = 490
    diceimg = pygame.image.load(
        "images/"+dice_images[num-1])  # images of both players
    diceimg = pygame.transform.scale(diceimg, (h, w))
    scrn.blit(diceimg, (x, y))


def gamewin():  # main game window with all display helper functions
    # to hide previous traces with black colour(bg)
    scrn.fill((pygame.Color("antiquewhite")))
    drawboard()
    drawhome()
    player1()
    player2()
    radioactive()
    dice_simulation(dice_num)


def views(view):
    if view == "i":
        instructions()
    if view == "g":
        gamewin()


# Atomic numer of SuperHeroes
atomicnum1a = 0
atomicnum2a = 0
atomicnum1b = 118
atomicnum2b = 118
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
            dice_animation()
            dice_simulation(dice_num)
            if turn % 2 == 0 and atomicnum1a+dice_num <= 79:
                for i in range(atomicnum1a+1, atomicnum1a+dice_num+1):
                    atomicnum1a = i
                    x1a = atomic[atomicnum1a][0]+5
                    y1a = atomic[atomicnum1a][1]+5
                    views(view)
                    pygame.display.update()
                    superhero_sound.play()
                    pygame.time.delay(1000//SUPERHERO_SPEED)

            elif turn % 2 != 0 and atomicnum2a+dice_num <= 79:
                for i in range(atomicnum2a+1, atomicnum2a+dice_num+1):
                    atomicnum2a = i
                    x2a = atomic[atomicnum2a][0]+5
                    y2a = atomic[atomicnum2a][1]+5
                    views(view)
                    pygame.display.update()
                    superhero_sound.play()
                    pygame.time.delay(1000//SUPERHERO_SPEED)

            turn += 1
        elif keys[pygame.K_2] and event.type == pygame.KEYDOWN:
            dice_num = randint(1, 6)
            dice_animation()
            dice_simulation(dice_num)
            if turn % 2 == 0 and atomicnum1b+dice_num >= 79:
                for i in range(atomicnum1b, atomicnum1b-dice_num-1,-1):
                    atomicnum1b = i
                    x1b = atomic[atomicnum1b][0]+5
                    y1b = atomic[atomicnum1b][1]+5
                    views(view)
                    pygame.display.update()
                    superhero_sound.play()
                    pygame.time.delay(1000//SUPERHERO_SPEED)

            elif turn % 2 != 0 and atomicnum2b+dice_num >= 79:
                for i in range(atomicnum2b, atomicnum2b-dice_num-1,-1):
                    atomicnum2b = i
                    x2b = atomic[atomicnum2b][0]+5
                    y2b = atomic[atomicnum2b][1]+5
                    views(view)
                    pygame.display.update()
                    superhero_sound.play()
                    pygame.time.delay(1000//SUPERHERO_SPEED)

            turn += 1
            
        elif keys[pygame.K_i]:
            view = "i"

        views(view)
        pygame.display.update()  # to update changes on screen

    pygame.time.delay(100)
pygame.quit()
