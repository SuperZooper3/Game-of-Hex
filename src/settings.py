import pygame

# Width and height, respectively
x, y = 120, 100

# Max frames per seconds
def get_maxfps(text=False):
    return 30 if not text else 2

# Size of the window opened
RESOLUTION = (1280, 1000)

# Set the colours depending on the ages
BGCOLOUR = (55, 55, 69)
CELLCOLOURS = [(31, 143, 132),(17, 163, 173),(20, 173, 196),(33, 171, 217),(49, 143, 232),(37, 99, 207),(17, 59, 133),(40, 77, 143),(89, 122, 181),(150, 172, 212),(218, 226, 240)]
CELLSTAGES = [1,3,5,7,10,15,20,25,30,40,50]

# Radius of the hexes
RADIUS = 5
RADIUS = 2

# Padding around the top and left edges
OFFSET = RADIUS * 1.8

# If to draw the heaxagonal lines
DOLINES = False

# Game clock
clock = pygame.time.Clock()

# Cells to be there at start
startCells = []

# Font for the fps counter
# Function becuase pygame needs to be initialized before calling font methods
def get_fps_font(size=32):
    return pygame.font.SysFont("verdana", size)
