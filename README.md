# Game of Hex
A game of life clone that runs in a hexagonal grid!

## Todo:
1. Implement the board management (reading, writing) - TTG
   1. For this we will need to figure out a coordinates system. **TODO**
      Coordinate system functions:
         - Board(x: int, y: int) generates the board with x amount of lines and y columns and returns the Board class
         - Board.genWithAlive(*aliveCells: list, x: int, y:int) classmethod that generates a board with the given cell coordinates alive, example: Board.genWithAlive([1, 1], [2, 2], [1, 2], x=5, y=5)
         - Board.state(x: int, y: int) -> bool: returns the state of a given cell, True if alive and False is dead
         - Board.alive(x: int, y: int) -> int: returns the amount of alive cells around the requested cell(excluding itself), value is between 0 and 6
         - Board.around(x: int, y: int) -> list\[bool\]: returns a list of the cells around the given cell(excluding itself), order is up, up-right, down-right, down, down-left, up-left
         - Board.write(x: int, y: int, state: bool) -> bool: sets the state of a given cell to alive or dead, state accepts True for alive and False for dead and returns the new value of the cell
   2. Based on the coordinates system, make functions to:
      - Generate the board. **TODO**
      - Read and write **TODO**
      - Check agacent cells (number of alive cells) **TODO**
2. Implement the ruleset
   1. Actualy write the basic rules
      - Make a clear way to set and edit basic rules (number of alives needed to spawn, die). **TODO**
      - Use variables or a settings file **TODO**
   2. Make the code easy to change to accomodate new, more complex, rules being added. 
      - Have a structure where you can just hook in new functions that are their own rules. **TODO**
3. Display the board!
    1. **Keep** rendering pipeline seperate from compute.
    2. Make platform specific rendering functions that can be quickly turned on and off.
       - Basic Command line rendering (working in either unix command line or windows) **TODO**
       - Numpy or equililant computer GUI rendering **TODO**
       - Numworks calculator rendering! (If we still feel like it) **TODO** 
