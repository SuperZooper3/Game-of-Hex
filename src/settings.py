import pygame

# Width and height, respectively
x, y = 15, 10

# Max frames per seconds
MAX_FPS = 60

# Size of the window opened
RESOLUTION = (1500, 1500)

# Radius of the hexes
RADIUS = 50

# Padding around the top and left edges
OFFSET = RADIUS * 1.8

# Game clock
clock = pygame.time.Clock()

# Font for the fps counter
# Function becuase pygame needs to be initialized before calling font methods
def get_fps_font():
    return pygame.font.SysFont("verdana", 32)
