README
Color-Mania

HOW TO OPEN WITH ECLIPSE:
1. Open ColorMania.py in Eclipse 
2. Make sure all assets are NOT in a resources folder!
3. Run

HOW TO OPEN WITH TERMINAL:
1. Go to the terminal and set your scope to the folder given to you
2.1. If you are on a PC, type in "ColorMania.py" (without the quotes) and enter to run the game
2.2. If you are on a Mac, type in "python ColorMania.py" (without the quotes) and enter to run the game

***Esc will pause and un-pause the game if in game and not scrolling, or quit the game if in a menu

Objective:
The objective of the game is to reach the Exit Sign located on the far right of the game map. This will be accomplished by avoiding obstacles using either gems or platforms.

In each level, the player will have approx. 150 seconds and 3 lives to reach the Exit Sign. If either value runs out, the game will be over and the screen will display a message.

The first level of the game is not impossible to win, but if the gem power-ups are used too soon, it will become extremely difficult. 

Gems:
Gems will modify the player's ability and make the level easier and quicker to complete. Gems will be necessary to use to finish the nearly every level. Gems' abilities are active for a certain amount of time dependent on the gem. Currently, there are several gems available: Invisibility, Jumping, Sprinting, Shrinking, Flying.

Controls: 
Arrow Key Up: Jump
Arrow Key Left: Move Left
Arrow Key Right: Move Right
Arrow Key Down: Moving Down - Only activated during flyng
Number Keys 1, 2, 3: Activate gem (time varies for each gem)
ESC: Pause in game and quit in menus

FEATURES TO NOTE:
1. Sound: There is a sound effect every time the player jumps, player loses a life, and activates a gem.
2. Graphics: There is a heads up display which allows the player to easily see his/her lives, time remaining, and arsenal of gems.
3. Physics: Gravity is enabled in the game, the y velocity accelerates till it reaches a max, and the player’s y velocity adjusts if there is a collision detected from the top (in other words forces in certain directions do impact velocity (follows Newton’s laws). 
4. Multiple Levels or Difficulties: Multiple levels have been implemented and vary in difficulty (difficulty is mainly varied by how many gems must be used and how large the level is). 
5. Complex Interactions between players and other objects: There is complex interaction between a player and the object(Gem), as the object modifies the player’s ability. There are several gems - flying, invisibility, shrinking, high-jumping and speed. 
6. Complex Properties of Player: Picking up a gem will put the power in the player's arsenal. They can then activate the gem for a certain amount of time by pressing the number key that corresponds to the gem in the heads up display. The player also has 3 total lives and 150 seconds to complete each level. 
7. Universe Bigger than Screen: Dynamic camera that moves with a map bigger than the window shown to the player at a given time
8. Other: Each level is scrolled through to give the player an understanding of the layout and prevent confusion on where to go/begin. Diagnostics Features were implemented (for diagnstoics see section below.) There is a fully functional pause menu which allows the player to take a break and pick up where they left off. 

1. Too Hard or Too Easy? Color Mania's Levels have been tested by others and there is a clear progression in difficulty. New players can easily clear level one, two and three. Level four and five become slightly more difficulty and Level Six and Seven demand more from the user. Each level is passable and has been passed by members not part of this team. 
3. Rate of Feedback: The player hears an unpleasant noise if he dies, and recieves a full diagnostics report about his play. Read about diagnostics in the section below to find out more. 
4. Larger Gameplay goals past single level: There is a time dependent score which is displayed to the user at the end of the level. The score is dependent on performance across all levels, so there is a larger goal past just getting across one more level. 
6. Dynamic Difficulty Adjustment: Dynamic difficulty is enabled so that when the player loses a life, an increasing number of arrows will appear to hint and help guide the player to gems and the exit. There are up and right arrows to better guide the player. 
7. Availability of Cheat Codes: "Chesney" will provide 10000 seconds of time and "Noah" will provide 100 lives. Both cannot be used at the same time

2. Goals are Understood, well integrated and rewarding: Each player must pass levels in 150 seconds and have three lives in total. The faster they pass and the less lives they lose their score goes up. Moreover, the better they do also helps them earn a higher grade for their overall critical thinking score. 
3. Feedback informs player of what is important: If player loses a life a sound is played to let them know of an unfavorable outcome. If levels are cleared slowly, the score is also lower. Furthermore, a diagnostics section is implemented to let users know statistics and information about their playing ability/critical thinking. 
4. User Modifiable Settings: The settings menu allows the player to choose their character, enter a name, and turn volume on or off (User Modifiable Settings).
5. Menu Functionality and thoughtfulness to user: Initial Menu which contains four buttons. When pressed, the tutorial button will bring the player to a tutorial level. Settings allows for changing game options.End menu allows the player to go back to the main menu, restart, quit, and check diagnostics.

More Features: 
The player is not supposed to collide with smiling bushes (serve as part of background).
There are three lives which decrease every time the player dies. 
With the ghost gem, the player will fall through platforms as well as go through walls. When ghost gem is activated player cannot land on elevated platforms and pick up other gems. This is intentional.  
If the player is invisible and then collides with a box wall after the gem powers end, he is automatically transported upwards till there is a place he can properly stand. This is intentional. 
For the level selector button, the levels reachable are the only ones that the player has passed so far. 

DIAGNOSTICS:
1. Checkpoints are made throughout the game. They are invisible to the player, but the game will track his/her progress behind the scenes.
2. Once the game is over, either by being beaten or losing all lives, the diagnostics button is available to see the diagnostics.
3. Diagnostics is in depth and analyzes the number of levels completed without hints, average passing time for check-points, and average compltion time. 
4. Color-Mania feels this is a very rich feature within our game which provides a great amount of feedback. 

How Color Mania Addresses Autism?
Color-Mania aims to target the critical thinking in a time-senstive environment of children with ASD. 
Some gems in Color-Mania has a cost and a benefit, therefore the player must think twice about using these gems. 
For Example: 
Ghost Gem - Pro: Walk through Walls Con: Cannot Collect any other gems and cannot jump on higher elevated platforms
Shrinking Gem - Pro: Fit through small spaces Con: Travel less distance
Moreover, there are under-the-hood functions in the game that test and analyze the player's critical thinking ability and break it down in the Diagnostics Section. This helps identify what the player may be good at or bad at and a parent or guardian can use this to further make more decisions. 
This was presented in class and accepted by the audience. 

NOTE:
1. The frame rate on a Mac computer is slower than that on a PC, and hence the player moves slower. The solution for framerate is already implmented in the code but Macs are inherently slow.

** Disclaimer: Image Initialization code uses functions used in discussion; however, because these are pygame functions the code is standard - almost none is purely pasted (all are typed by us see bottom for explanation). 
Techniques used to develop game such as passing a vector of strings to create a level were adopted by observation of other games - no code was copied

** Dynamic Text: Unlike previous versions our dynamic text, colortext was developed in-house