IMG_PATH = "images/"
SOUND_PATH = "sounds/"
# superhero dimensions
WIDTH = 60
HEIGHT = WIDTH
VEL = 68  # box dimensions
SCREEN_DIMENSIONS = 1254, 650
SUPERHERO_SPEED = 5  # moving speed

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
