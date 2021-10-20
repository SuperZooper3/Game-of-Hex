from typing import List, Tuple

cellsAroundEven = [[0, -1], [1, -1], [1, 0], [0, 1], [-1, 0], [-1, -1]]
cellsAroundOdd = [[0, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

"""
Cell class: the cell of a board
"""


class Cell:
    """
    Cell(x: int, y: int, alive: bool = False, age: int = 0): creates a cell and returns it
    Args:
        x: int the x coordinate of the cell
        y: int the y coordiante of the cell
        alive?: bool if the cell is alive or not
        age?: int?None the age of the cell, None if dead
    Returns:
        Cell
    """

    def __init__(self, x: int, y: int, alive: bool = False, age=None):
        self.x = x
        self.y = y
        self.alive = alive
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
        self.grid = [[Cell(_x, _y) for _y in range(y)] for _x in range(x)]
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
    def genAlive(cls, aliveCells: Tuple[list], x: int, y: int):
        board = cls(x, y)
        for cell in aliveCells:
            board.write(cell[0], cell[1], True, 1)
        return board

    """
    for cell in Board: Allows iteration through the board, moves downwards then rightwards, returns each cell as a Cell
    Returns:
        a generator that returns a dict per cell
    """

    def __iter__(self):
        for x in self.grid:
            for cell in x:
                yield cell

    """
    Board.alive(x: int, y: int) -> bool: returns the state of a given cell
    Args:
        x: int x coordinate of the cell to check
        y: int y coordinate of the cell to check
    
    Returns:
        bool the state of the cell, True if alive, False if dead and None if the cell is out of the grid
    """

    def alive(self, x: int, y: int) -> bool:
        if (x < 0 or x >= self.x) or (y < 0 or y >= self.y):
            return None
        return self.grid[x][y].alive

    """
    Board.age(x: int, y: int) -> bool: returns the age of a given cell
    Args:
        x: int x coordinate of the cell to check
        y: int y coordinate of the cell to check
    
    Returns:
        bool: the age of the cell
    """

    def age(self, x: int, y: int) -> bool:
        if (x < 0 or x >= self.x) or (y < 0 or y >= self.y):
            return None
        return self.grid[x][y].age

    """
    Board.aliveAround(x: int, y: int) -> int: returns the amount of alive cells around the requested cell(excluding itself)
    Args:
        x: int x coordinate of the cell to check
        y: int y coordinate of the cell to check
    
    Returns:
        int the amount of alive cells around the cell, velues range from 0-6
    """

    def aliveAround(self, x: int, y: int) -> int:
        count = 0
        if x % 2 == 0:
            cellsAround = cellsAroundEven
        else:
            cellsAround = cellsAroundOdd
        for xOffset, yOffset in cellsAround:
            if self.alive(x + xOffset, y + yOffset) == True:
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
            cells.append(self.alive(x + xOffset, y + yOffset))
        return cells

    """
    Board.write(x: int, y: int, alive: bool) -> bool: changes the state of a cell
    Args:
        x: int x coordinate of the cell to edit
        y: int y coordinate of the cell to edit
        alive: bool the state to give to the cell, True for alive and False for dead
    
    Returns:
        bool the state given to the cell
    """

    def write(self, x: int, y: int, alive: bool, age: int = None) -> bool:
        if (
            (x < 0 or x >= self.x)
            or (y < 0 or y >= self.y)
            or not (alive == True or alive == False)
        ):
            return None
        self.grid[x][y].alive = alive
        if age is not None:
            self.grid[x][y].age = age  # If an age is passed, add it
        return alive

    """
    Board.clear() -> None: Clears/resets the board
    Returns:
        None
    """

    def clear(self) -> None:
        self.grid = [
            [Cell(_x, _y, alive=False, age=None) for _y in range(self.y)]
            for _x in range(self.x)
        ]

    """
    str(Board): Returns the board as a string
    Returns:
        str The board as a string
    """

    def __str__(self) -> str:
        string = ""
        colors = True
        for y in range(self.y):
            if y % 2 != 0:
                string += " "
            for x in range(self.x):
                dis = 0 if self.age(x, y) is None else self.age(x, y)
                if int(self.alive(x, y)) == True:
                    if colors:
                        string += "\33[34m" + str(dis) + " " + "\033[0m"
                    else:
                        string += str(dis) + " "
                else:
                    string += str(dis) + " "
            string += "\n"
        return string
