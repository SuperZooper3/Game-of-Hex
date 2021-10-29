# Technical overview

## Main Program

This is the main program that runs the Game of Hex simulation.

### Methods

- simStep(stepping=False): This method is called every time the program loops. If the cell checking is not paused, it goes over each cell and performs a rule check and updates its age, unless that cell and all of it's adjacent cells are dead(this was implemented to save time when big portions of the board are dead/unfrozen). It also saves a screenshot of the screen if graphical rendering is chosen.
- clickHandler(pos): This function takes a tuple representing the position of a click on the board and flips the cell's state. This function is called when a cell on the board is clicked.
- togglepause(): This function inverts the paused state of the simulation. This function is called when the "Pause/Resume" button is pressed on the pygame window.
- clearBoard(): This function pauses the simulation, clears the saved images for the gif and clears the board. This function is called when the "Clear" button is pressed on the pygame window.
- step(): This function simulates a step of the simulation and renders the board. This function is called when the "Step" button is pressed on the pygame window.
- outlineSC(): This function takes 2 timestamped screenshots of the board: the first one with the outline of the clusters of alive cells and the second one with the outline and grid of alive cells. THis function is called when the "Outline SC" button is pressed on the pygame window.

### Pipeline

First, the arguments that were passed, if any, are parsed and the settings are defined.

Afterwards, both Board objects are defined, the saved gifs are cleared and the screen is defined if the graphical display is chosen.

Finally, the program enters a never-ending loop that will handle events from pygame if the graphical display is chosen, and that will simulate steps and render the board until the pygame window is closed if or Ctrl+C is pressed.

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

gif.py is used to take screenshots, save them to a gif, and create outlines of the cells.

### Methods

- clearImg() -> None: Clears the screenshots take to make gifs (`img/sc/sfsc*png`). This is used when the "Clear" button is pressed and on starting the program.
- screenshot(screen, path="img/sc/sfsc") -> None: Takes a screenshot of the screen and saves it to a file. This happens at every step of the simulation and is used when creating the gif.
- compileGif() -> None: Compiles the screenshots taken to make a gif. This is used when the "Gif" button is pressed. Also opens the image if you are running windows

## Rule Management

rules.py is where rules for the board are defined.

### Methods

- freeze(b: Board, x: int, y: int) -> bool: Takes as arguments a Board, and the x and y position of the cell to check, and returns a boolean value corresponding to the cell's new state after the application of the rule. This rule allows cells to die/unfreeze.
- eternalFreeze(b: Board, x: int, y: int) -> bool: Takes as arguments a Board, and the x and y position of the cell to check, and returns a boolean value corresponding to the cell's new state after the application of the rule. This rule doesn't allow cells to die/unfreeze.
