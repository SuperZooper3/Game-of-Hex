from typing import List, Tuple

cellsAroundEven = [[0, -1], [1, -1], [1, 0], [0, 1], [-1, 0], [-1, -1]]
cellsAroundOdd = [[0, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

"""
Cell class: the cell of a board
"""
class Cell:

    """
    Cell(x, y, state = False, age = 0): creates a cell
    Args:
        x: int the x coordinate of the cell
        y: int the y coordiante of the cell
        state: bool if the cell is alive or not OPTIONAL
        age: the age of the cell OPTIONAL
    Returns:
        Cell
    """
    def __init__(self,x, y, state = False, age = 0):
        self.x = x
        self.y = y
        self.state = state
        self.age = age

"""
Board class: stores hexagonal board
"""
class Board:
    """
    Board(x: int, y: int): generates the board with x amount of lines and y columns and returns the instance of Board
    Args:
        x: int width of the board
        y: int height of the board
    
    Returns:
        Board
    """
    def __init__(self, x: int, y: int):
        self.grid = [[Cell(_x,_y) for _y in range(y)] for _x in range(x)]
        self.x = x
        self.y = y
    
    """
    Board.genAlive(*aliveCells: Tuple[list], x: int, y:int): classmethod that generates a board with the given cell coordinates alive and returns the board
    Args:
        *aliveCells: Tuple[list] the list of cells to be alive when the board is generated, format [cellX, cellY]
        x: int width of the board
        y: int height of the board
    
    Returns:
        Board
    """
    @classmethod
    def genAlive(cls, aliveCells: Tuple[list], x: int, y:int):
        board = cls(x, y)
        for cell in aliveCells:
            board.write(cell[0], cell[1], True)
        return board
    
    """
    for cell in Board: Allows iteration through the board, moves downwards then rightwards, returns each cell as a dict containing it'S state, x coordinate and y coordinate
    Returns:
        a generator that returns a dict per cell
    """
    def __iter__(self):
        for x in self.grid:
            for cell in x:
                yield cell

    """
    Board.state(x: int, y: int) -> bool: returns the state of a given cell
    Args:
        x: int x coordinate of the cell to check
        y: int y coordinate of the cell to check
    
    Returns:
        bool the state of the cell, True if alive, False if dead and None if the cell is out of the grid
    """
    def state(self, x: int, y: int) -> bool:
        if (x < 0 or x >= self.x) or (y < 0 or y >= self.y):
            return None
        return self.grid[x][y].state

    """
    Board.alive(x: int, y: int) -> int: returns the amount of alive cells around the requested cell(excluding itself)
    Args:
        x: int x coordinate of the cell to check
        y: int y coordinate of the cell to check
    
    Returns:
        int the amount of alive cells around the cell, velues range from 0-6
    """
    def alive(self, x: int, y: int) -> int:
        count = 0
        if x % 2 == 0:
            cellsAround = cellsAroundEven
        else:
            cellsAround = cellsAroundOdd
        for xOffset, yOffset in cellsAround:
            if self.state(x + xOffset, y + yOffset) == True:
                count += 1
        return count

    """
    Board.around(x: int, y: int) -> list[bool]: returns a list of the cells around the given cell(excluding itself)
    Args:
        x: int x coordinate of the cell to check
        y: int y coordinate of the cell to check
    
    Returns:
        list[bool] the state of the cells around the checked cell, order is up, up-right, down-right, down, down-left, up-left
    """
    def around(self, x: int, y: int) -> List[bool]:
        cells = []
        if x % 2 == 0:
            cellsAround = cellsAroundEven
        else:
            cellsAround = cellsAroundOdd
        for xOffset, yOffset in cellsAround:
            cells.append(self.state(x + xOffset, y + yOffset))
        return cells

    """
    Board.write(x: int, y: int, state: bool) -> bool: changes the state of a cell
    Args:
        x: int x coordinate of the cell to edit
        y: int y coordinate of the cell to edit
        state:bool the state to give to the cell, True for alive and False for dead
    
    Returns:
        bool the state given to the cell
    """
    def write(self, x: int, y: int, state: bool, age: int = None) -> bool:
        if (x < 0 or x >= self.x) or (y < 0 or y >= self.y) or not (state == True or state == False):
            return None
        self.grid[x][y].state = state
        if not age == None:
            self.grid[x][y].age = age # If an age is passed, add it
        return state
    
    """
    Board.clear(): Clears/resets the board
    """
    def clear(self):
        self.grid = [[Cell(_x,_y) for _y in range(self.y)] for _x in range(self.x)]


    def __str__(self):
        string = ""
        colors = True
        for y in range(self.y):
            if y%2 != 0:
                string += " "
            for x in range(self.x):
                if int(self.state(x, y)) == 1:
                    if colors:
                        string += "\33[34m" + str(int(self.state(x, y))) + " " + "\033[0m"
                    else:
                        string += str(int(self.state(x, y))) + " "
                else:
                    string += str(int(self.state(x, y))) + " "
            string += "\n"
        return string