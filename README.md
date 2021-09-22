# Game of Hex
A game of life clone that runs in a hexagonal grid!

## Todo:
1. Implement the board management (reading, writing)
   1. For this we will need to figure out a coordinates system. **TODO**
   2. Based on the coordinates system, make functions to:
      - Generate the board. **TODO**
      - Read and write **TODO**
      - Check agacent cells (number of alive cells) **TODO**
2. Implement the ruleset
   1. Actualy write the basic rules
      - Make a clear way to set and edit basic rules (number of alives needed to spawn, die). **TODO**
      - Use variables or a settings file **TODO**
   2. Make the code easy to change to accomodate new, more complex, rules being added. 
      -   Have a structure where you can just hook in new functions that are their own rules. **TODO**
3. Display the board!
    1. **Keep** rendering pipeline seperate from compute.
    2. Make platform specific rendering functions that can be quickly turned on and off.
       - Basic Command line rendering (working in either unix command line or windows) **TODO**
       - Numpy or equililant computer GUI rendering **TODO**
       - Numworks calculator rendering! (If we still feel like it) **TODO** 