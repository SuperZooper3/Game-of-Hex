from board import *
# Structure of a rules is
# def rule(Board, any args)
# returns if the rule is followed or broken

"""
crowded(b: Board,x: int, y: int, n: int) -> bool
Args:
        b: Board board object that is used to check the state of a cell
        x: int x the x coordinate the cell we are checking the sate of
        y: int y the y coordinate the cell we are checking the sate of
        n: int n if there are >= n cells arround the cell at (x,y) then it will be "crowded"
    Returns:
        bool crowded returns if the cell is crowded
"""
def crowded(b, x , y, n):
    print("TODO :)")