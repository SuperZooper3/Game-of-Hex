from board import write
import random

"""
    boardRandom(b,n): Randomly finds n cells and has a 50% chance of turning them on or off on board b
    Args:
        b: Baord the board to which we will write
        n: int the number of cells to be tried
"""
def boardRandom(b,n):
    for i in range(n):
        b.write(
            random.randint(0, b.x - 1), random.randint(0, b.y - 1), random.choice([True, False])
        )