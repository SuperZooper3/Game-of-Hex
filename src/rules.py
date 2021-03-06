from board import *

# Structure of a rules is
# def rule(Board, any args)
# returns if the rule is followed or broken


def freeze(b: Board, x: int, y: int) -> Optional[bool]:
    """
    freeze(b: Board,x: int, y: int) -> bool
    Args:
            b: Board board object that is used to check the state of a cell
            x: int x the x coordinate the cell we are checking the sate of
            y: int y the y coordinate the cell we are checking the sate of
        Returns:
            bool returns if the cell is to be frozen in the next step
    """

    n = b.aliveAround(x, y)
    # list of all the adjacent values that will lead to an alive cell
    good: List[int] = [1, 3, 4, 5, 6]
    bad: List[int] = []  # list of the values that would lead to a dead cell
    if n != None:
        if n in good:
            # print("Number of alive, good:", n, x, y)
            return True
        elif n in bad:
            # print("Number of alive, bad:", n)
            return False
        else:
            # print("Number of alive is not in lists:", n)
            return False
    return None


# Different version of the freeze rule that prevents cells from dying
def eternalFreeze(b: Board, x: int, y: int) -> Optional[bool]:
    n: int = b.aliveAround(x, y)
    # list of all the adjacent values that will lead to an alive cell
    good: List[int] = [1, 3, 4, 5, 6]
    bad: List = []  # list of the values that would lead to a dead cell
    if b.alive(x, y):
        return True
    if n != None:
        if n in good:
            # print("Number of alive, good:", n, x, y)
            return True
        elif n in bad:
            # print("Number of alive, bad:", n)
            return False
        else:
            # print("Number of alive is not in lists:", n)
            return False
    return None
