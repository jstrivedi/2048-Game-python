# 2048-Game-python
How to use the game:
* The code is compiled in such a way that it can run on command prompt/terminal. 
* In order to choose action, you can choose any of the following actions: 
  * Keyboard key 'a': action Left, 
  * Keyboard key 'd': action Right,  
  * Keyboard key 'w': action UP, 
  * Keyboard key 's': action Down. 
  * If you choose incorrect input the game will end and you loose the game data as well!
* In order to play the game `cd` into the directory where `game.py` file is located and then do `python cypherd_jaldhir_2048.py` to start the game.
* In order to aide you, the repo includes a screengrab of a dryrun

Bugs to be fixed:
* The script doesn't check if the action is redundant or not. It accepts all 4 actions regardless of the state of the grid. i.e. if everything is in left doing a left action is redundant.
* The print statement is not optimized for two digit values. When you merge two 8's for the first time, you may see difference in length of one row with respect to others.
