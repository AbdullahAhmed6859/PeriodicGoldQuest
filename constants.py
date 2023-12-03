IMG_PATH = "images/"
SOUND_PATH = "sounds/"
# superhero dimensions
WIDTH = 60
HEIGHT = WIDTH
VEL = 68  # box dimensions
SCREEN_DIMENSIONS = 1254, 650
SUPERHERO_SPEED = 5  # moving speed
ROWS = 9
COLUMNS = 18

# CHARACTER INITIAL COORS x1 -> superhero 1  x2 -> superhero 2
x1a = 5+68+68+68
y1a = 5+68
x2a = 5+68+68+68+68+68
y2a = 5+68
x1b = 5+68+68+68+68
y1b = 5+68
x2b = 5+68+68+68+68+68+68
y2b = 5+68

HOME_CORS = {
    "1a": (x1a, y1a),
    "1b": (x1b, y1b),
    "2a": (x2a, y2a),
    "2b": (x2b, y2b)
}

DICE_IMAGES = ["dice.1.png", "dice.2.png", "dice.3.png",
               "dice.4.png", "dice.5.png", "dice.6.png"]

ELEMENT_SYMBOLS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce',
                   'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

ELEMENTS = {x: ELEMENT_SYMBOLS[x-1] for x in range(1, 119)}

GRP1 = [1, 3, 11, 19, 37, 55, 87]
GRP7 = [9, 17, 35, 53, 85, 117]
GRP2 = [4, 12, 20, 38, 56, 88]
GRP6 = [8, 16, 34, 52, 84, 116]
RADIOACTIVE_EL = [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
                  70, 71, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103]
SHIELD = [6, 22, 23, 24, 26, 40, 41, 46, 73, 74, 76, 78, 82, 95, 106]
SHIELD.extend(GRP1+GRP2+GRP6+GRP7)
