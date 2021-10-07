import pygame

# Width and height, respectively
x, y = 30, 25

# Max frames per seconds
def get_maxfps(text=False):
    return 60 if not text else 2

# Size of the window opened
RESOLUTION = (1280, 720)

# Radius of the hexes
RADIUS = 20

# Padding around the top and left edges
OFFSET = RADIUS * 1.8

# Game clock
clock = pygame.time.Clock()

# Cells to be there at start
startCells = [0,0],[1,1],[11,11]

# Font for the fps counter
# Function becuase pygame needs to be initialized before calling font methods
def get_fps_font(size=32):
    return pygame.font.SysFont("verdana", size)
