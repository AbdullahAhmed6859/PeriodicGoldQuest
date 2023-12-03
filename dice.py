import time
import pygame
from random import randint


class Dice:
    def __init__(self, dice_images, dice_sound):
        self.dice_images = dice_images
        self.dice_sound = dice_sound

    def dice_animation(self, scrn, next):
        # Animation of the rolling of a dice and displaying corresponding image.
        time1 = time.time()
        h, w = 150, 150
        x = 7
        y = 490

        self.dice_sound.play()
        while time.time() - time1 < self.dice_sound.get_length():
            img = self.dice_images[randint(0, 5)]
            diceimg = pygame.image.load(
                "images/"+img)  # images of both players
            diceimg = pygame.transform.scale(diceimg, (h, w))
            scrn.blit(diceimg, (x, y))
            pygame.display.update()
            pygame.time.delay(50)
            next()

    def dice_simulation(self, num, scrn):
        # Simulation of the rolling of a dice and displaying corresponding image.
        h, w = 150, 150
        x = 7
        y = 490
        diceimg = pygame.image.load(
            "images/"+self.dice_images[num-1])  # images of both players
        diceimg = pygame.transform.scale(diceimg, (h, w))
        scrn.blit(diceimg, (x, y))
