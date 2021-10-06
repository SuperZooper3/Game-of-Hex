from board import *
# Structure of a rules is
# def rule(Board, any args)
# returns if the rule is followed or broken

"""
freeze(b: Board,x: int, y: int) -> bool
Args:
        b: Board board object that is used to check the state of a cell
        x: int x the x coordinate the cell we are checking the sate of
        y: int y the y coordinate the cell we are checking the sate of
    Returns:
        bool returns if the cell is to be frozen in the next step
"""
def freeze(b: Board, x: int , y: int) -> bool:
    n = b.alive(x, y)
    print("Number of alive:", n)
    good = [1, 3, 4, 5, 6] # list of all the adjacent values that will lead to an alive cell
    bad = [0, 2] # list of the values that would lead to a dead cell
    if n in good:
        print("Number of alive, good:", n)
        return True
    elif n in bad:
        print("Number of alive, bad:", n)
        return False
    else:
        print("Number of alive is not in lists:", n)
        return None