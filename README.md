# Game of Hex
A game of life clone that runs in a hexagonal grid!

## Todo:
1. Implement the board management (reading, writing) - TTG
   1. For this we will need to figure out a coordinates system. **TODO**
      Coordinate system functions:
         - Board(x: int, y: int) generates the board with x amount of lines and y columns and returns the Board class
         - Board.state(x: int, y: int) returns the state of a given cell, True if alive and False is dead
         - Board.alive(x: int, y: int) returns the amount of alive cells around the requested cell(excluding itself), value is int between 0 and 6
         - Board.around(x: int, y: int) returns a list of the cells around the given cell(excluding itself), order is up, up-right, down-right, down, down-left, up-left
         - Board.write(x: int, y: int, state: bool) sets the state of a given cell to alive or dead, state accepts True for alive and False for dead
   2. Based on the coordinates system, make functions to:
      - Generate the board. **TODO**
      - Read and write **TODO**
      - Check agacent cells (number of alive cells) **TODO**
2. Implement the ruleset - BG
   1. Actualy write the basic rules
      - Make a clear way to set and edit basic rules (number of alives needed to spawn, die). **TODO**
      - Use variables or a settings file **TODO**
   2. Make the code easy to change to accomodate new, more complex, rules being added. 
      - Have a structure where you can just hook in new functions that are their own rules. **TODO**
3. Get input from the user:
   1. *In the futre:* using the GUI, get coordinates that will be passed at the start
   2. Pass through the cells that will be alive to the Board manager
4. Display the board! - Tommcn
    1. **Keep** rendering pipeline seperate from compute.
    2. Make platform specific rendering functions that can be quickly turned on and off.
       - Basic Command line rendering (working in either unix command line or windows) **TODO**
       - Numpy or equililant computer GUI rendering **TODO**
       - Numworks calculator rendering! (If we still feel like it) **TODO** 
5. Write tests - Super
   1. Make a checking system that is integrated with github actions - **TODO**
   2. Actualy write all the checks: - **TODO**
      - Make sure that the scripts have no syntax errors
      - Check to make sure board generates, can read, can write, dosent crash when writing ouside of range
      - Make sure there is a ruleset
      - Make sure the simulation follows the ruleset
