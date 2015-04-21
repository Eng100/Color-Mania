README
Color-Mania

HOW TO OPEN WITH ECLIPSE:
1. Open ColorManiaBeta.py in Eclipse 
2. Make sure all assets are NOT in a resources folder!
3. Run

HOW TO OPEN WITH TERMINAL:
1. Go to the terminal and set your scope to the folder given to you
2.1. If you are on a PC, type in "ColorManiaBeta.py" (without the quotes) and enter to run the game
2.2. If you are on a Mac, type in "python ColorMania.py" (without the quotes) and enter to run the game

***Esc will pause and un-pause the game if in game and not scrolling, or quit the game if in a menu

Objective:
The objective of the game is to reach the Exit Sign located on the far right of the game map. This will be accomplished by avoiding obstacles using either gems or platforms.

In each level, the player will have approx. 150 seconds and 3 lives to reach the Exit Sign. If either value runs out, the game will be over and the screen will display a message.

The first level of the game is not impossible to win, but if the gem power-ups are used too soon, it will become extremely difficult. 

Gems:
Gems will modify the player's ability and make the level easier and quicker to complete. Gems will be necessary to use to finish the nearly every level. Gems' abilities are active for a certain amount of time dependent on the gem. Currently, there are several gems available: Invisibility, Jumping, Sprinting, Shrinking, Flying, and Traction.

Controls: 
Arrow Key Up: Jump
Arrow Key Left: Move Left
Arrow Key Right: Move Right
Arrow Key Down: Moving Down - Only activated during flyng
Number Keys 1, 2, 3: Activate gem (time varies for each gem)
ESC: Paus in game and quit in menus

FEATURES TO NOTE:
1. Dynamic camera that moves with a map bigger than the window shown to the player at a given time
2. Initial Menu which contains four buttons. When pressed, the tutorial button will bring the player to a tutorial level. Settings allows for changing game options.
3. There is a sound effect every time the player jumps, player loses a life, and activates a gem.
4. There are three lives which decrease every time the player dies. 
5. There is a time dependent score which is displayed to the user at the end of the level. The score is dependent on performance across all levels, so there is a larger goal past just getting across one more level. 
6. There is complex interaction between a player and the object(Gem), as the object modifies the player’s ability. There are several gems - flying, invisibility, shrinking, high-jumping and speed. 
7. Gems: picking up a gem will put the power in the player's arsenal. They can then activate the gem for a certain amount of time by pressing the number key that corresponds to the gem in the heads up display.
8. Physics, Gravity is enabled in the game, the y velocity accelerates till it reaches a max, and the player’s y velocity adjusts if there is a collision detected from the top (in other words forces in certain directions do impact velocity (follows Newton’s laws). 
9. The player is not supposed to collide with smiling bushes (serve as part of background).
10. There is a heads up display which allows the player to easily see his/her lives, time remaining, and arsenal of gems.
11. DIAGNOSTICS: See section below for in depth explanation
12. The user may customize their character for the game in the main menu and name their profile (Multiple characters/customization).
13. Dynamic difficulty is enabled so that when the player loses a life, an increasing number of arrows will appear to hint and help guide the player to gems and the exit. In the final release, up and left arrows were added to better guide the player. 
14. Multiple levels have been implemented and vary in difficulty (difficulty is mainly varied by how many gems must be used and how large the level is). 
15. Each level is scrolled through to give the player an understanding of the layout and prevent confusion on where to go/begin.
16. There is a fully functional pause menu which allows the player to take a break and pick up where they left off.
17. End menu allows the player to go back to the main menu, restart, quit, and check diagnostics.
18. The settings menu allows the player to choose their character, enter a name, and turn volume on or off (User Modifiable Settings).
19. With the ghost gem, the player will fall through platforms as well as go through walls. 
20. CHEAT CODES: "Chesney" will provide unlimited time and "Noah" will provide unlimited lives. Both cannot be used at the same time
21. The graphics for the gems were revamped. Jetpack and Sprinting were made in-house, the rest were held constant.
22. More levels were added to the game, some of which were made to be incredibly hard once the player has mastered the skills of the game.

DIAGNOSTICS:
1. Checkpoints are made throughout the game. They are invisible to the player, but the game will track his/her progress behind the scenes.
2. Once the game is over, either by being beaten or losing all lives, the diagnostics button is available to see the diagnostics.
3. Diagnostics is in depth and analyzes the number of levels completed without hints a long with other metrics
4. Color-Mania feels this is a very rich feature within our game. 

RECOGNIZED BUGS:
1. The frame rate on a Mac computer is much slower, and hence the player moves slower. 

** Disclaimer: Image Initialization code uses functions used in discussion; however, because these are pygame functions the code is standard - almost none is purely pasted (all are typed by us see bottom for explanation). 
Techniques used to develop game such as passing a vector of strings to create a level were adopted by observation of other games - no code was copied

** Dynamic Text: Unlike previous versions our dynamic text, colortext was developed in-house