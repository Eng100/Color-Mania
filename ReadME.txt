README
Color-Mania

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
11. A diagnostic report is available based on the player's performance on a level in the end menu to give player additional feedback to their level score.
12. The user may customize their character for the game in the main menu and name their profile (Multiple characters/customization).
13. Dynamic difficulty is enabled so that when the player loses a life, an increasing number of arrows will appear to hint and help guide the player to gems and the exit.
14. Multiple levels have been implemented and vary in difficulty (difficulty is mainly varied by how many gems must be used and how large the level is). 
15. Each level is scrolled through to give the player an understanding of the layout and prevent confusion on where to go/begin.
16. There is a fully functional pause menu which allows the player to take a break and pick up where they left off.
17. End menu allows the player to go back to the main menu, restart, quit, and check diagnostics.
18. The settings menu allows the player to choose their character, enter a name, and turn volume on or off (User Modifiable Settings).


RECOGNIZED BUGS:
1. With the ghost gem, the player will fall through platforms as well as go through walls. 
2. The frame rate on a Mac computer is much slower, and hence the player moves slower. 
3. In the tutorial, instructional messages are based on the player’s location and what they have accomplished, assuming that player is following all rules. 


** Disclaimer: Image Initialization code uses functions used in discussion; however, because these are pygame functions the code is standard - almost none is purely pasted (all are typed by us see bottom for explination). 
Techniques used to develop game such as passing a vector of strings to create a level were adopted by observation of other games - almost no code was copied (see below for explination of copied code). 

** Dynamic Text: editing is a feature we wanted to implement, but because of time, needed to use a 3rd party file and code to allow for this to happen without sinking too much time into it. Because of this, we used a code called EZTEXT. It can be found here: http://www.pygame.org/project-EzText-920-.html and is written by pywiz32. This is the only instance of other code being used, as it is essentially handled like a library that pywiz32 never made into a library. This is the ONLY instance of reused code. 