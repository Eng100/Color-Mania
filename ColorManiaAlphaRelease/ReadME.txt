README
Color-Mania

Objective:
The objective of the game is to reach the Exit Sign located on the far right of the game map. This will be accomplished by avoiding obstacles using either gems or platforms.

On the first level, the player will have 120 seconds and 3 lives to reach the Exit Sign. If either value runs out, the game will be over and the screen will display a message.

Once the Exit Sign is reached, the player’s score will be displayed based on the time remaining in the level. 

The first level of the game is not impossible to win, but if the gem power-ups are used too soon, it will become extremely difficult. 

Gems:
Gems will modify the player's ability and make the level easier and quicker to complete. Gems will be necessary to use to finish the first level. Gems' abilities are active for a certain amount of time dependent on the gem. Currently, there are two gems: an Invisibility Gem that lets the player walk through walls and a Jumping Gem that lets the player jump higher. 

Controls: 
Arrow Key Up: Jump
Arrow Key Left: Move Left
Arrow Key Right: Move Right
Spacebar: Use gem (will last 7 seconds for Invisibility Gem and last 15 seconds for Jumping Gem)

FEATURES TO NOTE:
1. Dynamic camera that moves with a map bigger than the window shown to the player at a given time
2. Initial Menu which contains four buttons. When pressed, the tutorial button will bring the player to a tutorial level. When any other button is pressed, the player will be taken to the level (beginning of the game).
3. There is a sound effect every time the player jumps. 
4. There are three lives which decrease every time the player dies. 
5. There is a time dependent score which is displayed to the user at the end of the level. 
6. There is complex interaction between a player and the object(Gem), as the object modifies the player’s ability. 
7. Gems, picking up a gem will put the power in the player's arsenal. They can then activate the gem for 7 seconds by pressing spacebar. Currently, the two gems are a "ghost" ability, where the player can move through walls, and "jumping" ability, where the player can jump higher.
8. Gravity is enabled in the game.
9. The player is not supposed to collide with smiling bushes (serve as part of background). 

RECOGNIZED BUGS:
1. With the ghost gem, the player will fall through platforms as well as go through walls. 
2. The frame rate on a Mac computer is much slower, and hence the player moves slower. 
3. The Settings and Customize Menu options lead to game play. 
4. The instructional messages are based on the player’s location, assuming that player is following all rules. 


** Disclaimer: Image Initialization code uses functions used in discussion; however, because these are pygame functions the code is standard - none is purely pasted (all are typed by us). 
Techniques used to develop game such as passing a vector of strings to create a level were adopted by observation of other games - no code was copied. 
