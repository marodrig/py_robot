# Toy Robot:

## Required software
  - Python 3.5.x
  - unittest unit testing package for Python.

## Usage:

  This is a toy Robot simulator.  In order to run the code you will need Python 3.5.x or better.
  
  Once Python 3.5.X has been installed, the user can start the program by typing:
  
  ```
  python toy_handler.py 
  ```
  
  The program will read input from STDIN.
  
  Possible commands include:
  - PLACE X, X, {DirectionFaced}
  - MOVE
  - LEFT
  - RIGHT
  - REPORT
  
  Any other command will exit the program.
  The program will raise Errors when the robot could face damage by moving outside the 5x5 board.
  
## Testing:
    Test are found in the test directory.
  
