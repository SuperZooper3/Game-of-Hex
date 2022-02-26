# Todo

1. Implement the board management (reading, writing) - TTG
   1. For this we will need to figure out a coordinates system. **DONE**
   2. Based on the coordinates system, make functions to:
      - Generate the board. **DONE**
      - Read and write **DONE**
      - Check agacent cells (number of alive cells) **DONE**
2. Implement the ruleset - BG
   1. Actualy write the basic rules
      - Make a clear way to set and edit basic rules (number of alives needed to spawn, die). **DONE**
      - Use variables or a settings file **DONE**
   2. Make the code easy to change to accomodate new, more complex, rules being added. 
      - Have a structure where you can just hook in new functions that are their own rules. **DONE**
3. Get input from the user:
   1. *In the futre:* using the GUI, get coordinates that will be passed at the start
   2. Pass through the cells that will be alive to the Board manager
4. Display the board! - Tommcn
    1. **Keep** rendering pipeline seperate from compute. - **DONE**
    2. Make platform specific rendering functions that can be quickly turned on and off.
       - Basic Command line rendering (working in either unix command line or windows) **DONE**
       - Numpy or equililant computer GUI rendering **DONE**
       - Numworks calculator rendering! (If we still feel like it) **TODO** 
5. Write tests - Super - Abandoned
   1. Make a checking system that is integrated with github actions - **TODO**
   2. Actualy write all the checks: - **TODO**
      - Make sure that the scripts have no syntax errors
      - Check to make sure board generates, can read, can write, dosent crash when writing ouside of range
      - Make sure there is a ruleset
      - Make sure the simulation follows the ruleset
