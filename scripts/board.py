cellsAround = [[0, -1], [1, -1], [1, 0], [0, 1], [-1, 1], [-1, 0]]

class Board:
    def __init__(self, x: int, y: int):
        self.grid = [[False for _ in range(x)] for _ in range(y)]
        self.x = x
        self.y = y
    
    @classmethod
    def genAlive(cls, *aliveCells: list, x: int, y:int):
        board = cls(x, y)
        for cell in aliveCells:
            board.write(cell[0], cell[1], True)
        return board

    def state(self, x: int, y: int) -> bool:
        if (x < 0 or x >= self.x) or (y < 0 or y >= self.y):
            return None
        return self.grid[y][x]

    def alive(self, x: int, y: int) -> int:
        count = 0
        for xOffset, yOffset in cellsAround:
            if self.state(x + xOffset, y + yOffset) == True:
                count += 1
        return count

    def around(self, x: int, y: int) -> list[bool]:
        cells = []
        for xOffset, yOffset in cellsAround:
            cells.append(self.state(x + xOffset, y + yOffset))
        return cells

    def write(self, x: int, y: int, state: bool) -> bool:
        if (x < 0 or x >= self.x) or (y < 0 or y >= self.y) or not (state == True or state == False):
            return None
        self.grid[y][x] = state
        return state
    
    def __str__(self):
        string = ""
        for y in range(self.y):
            if y%2 != 0:
                string += " "
            for x in range(self.x):
                string += str(int(self.state(x, y))) + " "
            string += "\n"
        return string