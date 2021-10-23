# Technical overview

## Board class

The Board class stores a hexagonal board. Having the board in a class instead of an array makes it easier to create methods for the board.

### Methods

- Board(x: int, y: int) -> Board: Generates a Board object with a given size
- Board.genAlive(aliveCells: List\[list\], x: int, y: int) -> Board: A classmethod that generates a Board object with a given size and with specified cells alive. This is used when we want to generate a board with cells that already are alive.
- for x in Board: Returns a Generator that iterates over the board and returns each cell. It goes through the cells downwards then rightwards. This is used mainly to iterate over the cells when applying the rules.
- Board.alive(x: int, y: int) -> bool: Returns the state of a given cell as a bool or returns None if the cell is out of the grid. This is used by many functions to check the state of a cell.
- Board.age(x: int, y: int) -> int: Returns the age of a given cell, or None if the cell is out of the grid. This is used when drawing the board to determine the colour that will be used.
- Board.aliveAround(x: int, y: int) -> int: Returns the amount of adjacent alive cells for a given cell. This is used mainly when applying rules.
- Board.around(x: int, y: int) -> List\[bool\]: returns a list of boolean values representing the state of the cells surrounding the cell. This is mainly used when drawing the outline of the alive cells.
- Board.write(x: int, y: int, alive: bool, age: int = None) -> bool: Writes to a specific cell and returns the state written to the cell. This is mainly used when giving a new state to a cell after applying the rules to it.
- Board.clear() -> None: Clears the board. This is used when the "Clear" button is pressed.
- str(Board) -> str: Returns a string representing the board. This is used when the text output is selected.

## Cell class

Stores the cell of a board. Having each cell as a class is useful because it makes it easier to store data about the cell.

### Methods

- Cell(x: int, y: int, alive: bool = False, age = None) -> Cell: Generates a Cell object with its position, state and age

## Rendering

These functions are used when rendering the board with a GUI.

- closest(lst, K): Returns the closest value to a given value in a list. This is used to find the colour to give cells when they're rendered.
- getHexCoords(radius, position): Returns a list of coords for the corners of a hexagon at a given potision and with a given radius
- drawHex(screen, pos, alive, age, board=None, grid=DOGRID, outl=OUTLINE): Draws a hex on a given screen, at a given position and with a given age. This is used when the program iterates over each cell to render it.
- handleEvents( onclick=None, onchangepause=None, onclear=None, onstep=None, ongif=None, onoutline=None): Handles click events from pygame, each argument has to be a function.
- renderBoard(screen, board, text=False, grid=DOGRID, outl=OUTLINE): Renders the board according to set grid and outline parameters.
- renderDebug(screen): Renders the butons and the FPS counter on the side of the screen.

## Gif and Outline

Gif.py is used to take screenshots, save them to a gif, and create outlines of the cells.

### Methods

- clearImg() -> None: Clears the screenshots take to make gifs (`img/sc/sfsc*png`). This is used when the "Clear" button is pressed and on starting the program.
- screenshot(screen, path="img/sc/sfsc") -> None: Takes a screenshot of the screen and saves it to a file. This happens at every step of the simulation and is used when creating the gif.
- compileGif() -> None: Compiles the screenshots taken to make a gif. This is used when the "Gif" button is pressed. Also opens the image if you are running windows