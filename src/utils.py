import random

from board import Board

"""
    boardRandom(b,n): Randomly finds n cells and has a 50% chance of turning them on or off on board b
    Args:
        b: Board the board to which we will write
        n: int the number of cells to be tried
"""


def boardRandom(b: Board, n: int) -> None:
    for _ in range(n):
        b.write(
            random.randint(0, b.x - 1),
            random.randint(0, b.y - 1),
            random.choice([True, False]),
        )
