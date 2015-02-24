import pygame, time
from pygame.locals import*
global screen
pygame.init()

Tile_Length = 70

View_Height = 600
View_Width = 800
Half_View_Height = (View_Height)/2
Half_View_Width = (View_Width)/2
View_Screen = (View_Width, View_Height)

class Image(pygame.sprite.Sprite):

    def __init__(self, color, filename, location, size):
 
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()

        self.image.set_colorkey(color) 
        self.rect = self.image.get_rect()
        if not(location[0] == 70) and not(location[1] == 70): 
            self.rect = self.rect.inflate(-10, -10)

        self.rect.x = location[0]
        self.rect.y = location[1]

class Window(object):
    def __init__(self, functionCall, width, height):
        self.functionCall = functionCall
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.functionCall(self.state, target.rect)

def complex_camera(camera, target_rect):
    j, k, _, _ = target_rect
    _, _, x, y = camera
    j, k, _, _ = -j+Half_View_Width, -k+Half_View_Height, x, y

    j = min(0, j)                          
    j = max(-(camera.width-View_Width), j)  
    k = max(-(camera.height-View_Height), k)
    k = min(0, k)                          
    return Rect(j, k, x, y)

def loading(name):
    image = pygame.image.load(name)
    return image

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
        self.imagesright = []
        self.imagesright.append(loading('p1_walk02.png'))
        self.imagesright.append(loading('p1_walk03.png'))
        self.imagesright.append(loading('p1_walk04.png'))
        self.imagesright.append(loading('p1_walk05.png'))
        self.imagesright.append(loading('p1_walk06.png'))
        self.imagesright.append(loading('p1_walk07.png'))
        self.imagesright.append(loading('p1_walk08.png'))
        self.imagesright.append(loading('p1_walk09.png'))
        self.imagesright.append(loading('p1_walk10.png'))
        # assuming both images are 64x64 pixels
        self.imagesleft = []
        self.imagesleft.append(loading('p1_walk12.png'))
        self.imagesleft.append(loading('p1_walk13.png'))
        self.imagesleft.append(loading('p1_walk14.png'))
        self.imagesleft.append(loading('p1_walk15.png'))
        self.imagesleft.append(loading('p1_walk16.png'))
        self.imagesleft.append(loading('p1_walk19.png'))
        self.imagesleft.append(loading('p1_walk17.png'))
        self.imagesleft.append(loading('p1_walk17.png'))
        self.imagesleft.append(loading('p1_walk18.png'))
        
        
        self.index = 0
        self.image = self.imagesright[self.index]
        self.x = 100
        self.y = 960
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-10, 0)
        self.xvel = 0 
        self.yvel = 0
        self.onGround = False
        self.gemsCollected = []
        self.lives = 3
        self.time = 0
        self.complete = False
    def update(self, up, down, left, right, platforms, gemActivate, gems, base_platforms, goals):
        isInvisibility = False
        if up: 
            if self.onGround: self.yvel -= 11
            if gemActivate: 
                if (self.gemsCollected[0].typeOfGem == "Jumping"): 
                    self.gemsCollected[0].time -= 1; 
                    if self.onGround: 
                        self.gemsCollected[0].Jumping(self)
        if down: 
            pass 
        if right:
            if (self.onGround): 
                self.index += 1
            self.xvel = 8
            if self.index >= len(self.imagesright):
                self.index = 0
            self.image = self.imagesright[self.index]
        if left:
            if (self.onGround): 
                self.index += 1
            self.xvel = -8
            if self.index >= len(self.imagesleft):
                self.index = 0
            self.image = self.imagesleft[self.index]
        if gemActivate: 
            self.gemsCollected[0].time -= 1
            if (self.gemsCollected[0].typeOfGem == "Invisibility"):  
                isInvisibility = True; 
        if not self.onGround: 
            self.yvel += 0.3
            if self.yvel > 100: self.yvel= 100
        if not(left or right): 
            self.xvel = 0
        
        self.rect.right += self.xvel 
        self.collide(self.xvel, 0, platforms, gems, isInvisibility, base_platforms, goals)
        
        self.rect.top += self.yvel
        self.onGround = False
        self.collide(0, self.yvel, platforms, gems, isInvisibility, base_platforms, goals)
        
    def loseLife(self):
        self.lives -=1
    def setTime(self, val):
        self.time =  val
        
    def getTime(self):
        return self.time          
    
    def collide (self, xvel, yvel, platforms, gems, isInvisibility, base_platforms, goals):
        if (isInvisibility): 
            for p in base_platforms: 
                if pygame.sprite.collide_rect(self, p):
                    if xvel > 0:
                        self.rect.right = p.rect.left
                    if xvel < 0:
                        self.rect.left = p.rect.right
                    if yvel >= 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 1
        else: 
            for p in platforms:
                if pygame.sprite.collide_rect(self, p):
                    if xvel > 0:
                        self.rect.right = p.rect.left
                    if xvel < 0:
                        self.rect.left = p.rect.right
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 1
        
                for g in gems: 
                    if pygame.sprite.collide_rect(self,g):
                        g.Collided()
                        if len(self.gemsCollected) > 0: 
                            self.gemsCollected[0] = g
                        else: 
                            self.gemsCollected.append(g)  
                        
    def victory(self, goals):
        for b in goals: 
            if pygame.sprite.collide_rect(self,b):
                self.complete = True
                return True
            
        
    def is_dead(self, level_height, spawn):
        if (self.rect.top >= level_height + 2): 
            return True
        if ((150 - self.time + spawn) <= 0 ): 
            return True
        return False
    
    def reset(self):
        player.x =  0
        player.y = 0
        player.rect.x = 0
        player.rect.y = 0
        

def display_box(screen, message, x, y, lives):
    font = pygame.font.SysFont("Courier New", 20)
    if(lives == 0):
        font = pygame.font.SysFont("Courier New", 36)
        prompt = font.render(message, 1, [0, 0, 255])
    elif(lives == 4):
        prompt = font.render(message, 1, [0, 0, 255])
    else:
        prompt = font.render(message % lives, 1, [0, 0, 255])
    screen.blit(prompt, (x, y))  
        
class Gem(pygame.sprite.Sprite):
    def __init__(self, color, filename, location, typeOfGem):
        # call parent class constructor
        pygame.sprite.Sprite.__init__(self)
        
        # load the image, converting the pixel format for optimization
        self.image = pygame.image.load(filename).convert_alpha()
        # make 'color' transparent on the image
        self.image.set_colorkey(color) 
        # set the rectangle defined for this image for collision detection
      
        # position the image
        if (filename == "ghost.png"): 
            self.image = pygame.transform.scale(self.image, (50, 60))
        
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
        self.typeOfGem = typeOfGem
        self.exist = True
        
        if (self.typeOfGem == "Invisibility"): 
            self.type = "Invisibility"
            self.checkCollision = False
            self.time = 7 * 60
        if (self.typeOfGem == "Jumping"): 
            self.type = "Jumping"
            self.yvel = 4
            self.time = 15 * 60 
    
    def Jumping(self, Character): 
        Character.yvel -= 4
        
    def Collided (self):
        self.exist = False
        self.rect = (0, 0, 0 , 0)
        self.kill()
        


class Menu(pygame.sprite.Sprite):
    def __init__(self,color, filename, location, types):
        # call parent class constructor
        pygame.sprite.Sprite.__init__(self)
        
        # load the image, converting the pixel format for optimization
        self.image = pygame.image.load(filename).convert_alpha()
        # make 'color' transparent on the image
        self.image.set_colorkey(color) 
        # set the rectangle defined for this image for collision detection
      
        # position the image
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
        self.type = types
    
    
def CheckOutofBounds(Character, level_height, level_width):
    if (Character.rect.left <= 0): 
        Character.rect.left = 0
    if (Character.rect.right >= level_width): 
        Character.rect.right = level_width
    if (Character.rect.top <= 0): 
        Character.rect.top = 0
        Character.yvel = 1

def Music_Play(music_file, repetitions): 
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(repetitions)
    
def Tutorial(gemActivate, Character):
    if Character.rect.x > 0 and Character.rect.x < 2030: #if the player is within the starting section, display these words
        display_box(screen, "Welcome! To move, use the up or side arrow keys.", View_Width/6, View_Height/3, 4)
        display_box(screen, "Walk right to continue.",View_Width/3,View_Height/2.5,4)
    else: #else display the next section
        if (gemActivate == False and Character.rect.x > 2030 and Character.rect.x < 3500):
            display_box(screen, "Walk over the ghost gem to collect it.",View_Width/4,View_Height/3,4)
            display_box(screen, "Press SPACEBAR to activate gem.",View_Width/3,View_Height/2.5,4)
        elif(gemActivate == True and Character.gemsCollected[0].type == "Jumping"): 
            display_box(screen, "Jump over the wall using your elevated jumping abilities",View_Width/3 - 190,View_Height/3,4)
            display_box(screen, "Hit the exit sign to reach the menu again",View_Width/6,View_Height/2.5,4)
        elif gemActivate == False and Character.rect.x > 3700 and Character.rect.x < 5500: 
            display_box(screen, "Walk over the Jumping gem to collect it.",View_Width/4,View_Height/3,4)
            display_box(screen, "Press SPACEBAR to activate gem.",View_Width/3,View_Height/2.5,4)
        else: 
            if (Character.rect.x < 3700):
                display_box(screen, "You can walk through everything for 7 seconds.",View_Width/5.3,View_Height/3,4)
                display_box(screen, "Walk through the wall on the right to continue.",View_Width/6,View_Height/2.5,4)
    
        pygame.display.update()
    
def Level_Screens(platforms, gems, allSprites, base_platforms, player, level, background, player_sprite_vec, goals):
    first_level_height = len(level) * 70
    first_level_length = len(level[0]) * 70
    camera = Window(complex_camera, first_level_length, first_level_height)
    
    timer = pygame.time.Clock()
    gemActivate = False
    active = True
    up = down = left = right = False
    spawn = time.clock()
    while active:
        timer.tick(60)
        start = time.clock()
        player.setTime(start)
        #pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                raise SystemExit
                active = False
                return 
            if event.type == KEYDOWN and event.key == K_UP:
                up = True
                Music_Play("Char Jump.wav", 0)
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYDOWN and event.key == K_SPACE:
                if (len(player.gemsCollected) > 0):  
                    gemActivate = True
                    if (player.gemsCollected[0].typeOfGem == "Invisibility"): 
                        Music_Play("Gem1 GhostInvis.wav", 0)   
            if event.type == KEYUP and event.key == K_UP:
                up = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                left = False
    
        if (gemActivate): 
            if (player.gemsCollected[0].time <= 0): 
                gemActivate = False
                del player.gemsCollected[:]
                #player.gemsCollected.remove(Gem)
 
        for k in range(15):
            screen.blit(sky, [400, k * 70])
        for k in range(15):
            screen.blit(sky, [0, k * 70])
        for k in range(15):
            screen.blit(sky, [200, k * 70])
        for k in range(15):
            screen.blit(sky, [600, k * 70])
            
        camera.update(player)
        CheckOutofBounds(player, first_level_height, first_level_length)

        if(player.is_dead(first_level_height, spawn)):
            player.loseLife()
            return 0; 
        
        if (player.victory(goals)):
            return 5; 
        
        player.update(up, down, left, right, platforms, gemActivate, gems, base_platforms, goals)
        for sprite in allSprites: 
            screen.blit(sprite.image, camera.apply(sprite))
        for p in player_sprite_vec: 
            screen.blit(p.image, camera.apply(p))
        if(player.lives > 0): 
            if (not(gamestate == 4)):
                display_box(screen, "Lives: %d", 20, 10, player.lives)
            display_box(screen, "Time: %d seconds", 20, 40, 150 - start + spawn)
            
        if (gamestate == 4):
            Tutorial(gemActivate, player)
    
        pygame.display.update()
        
def Level_Vector_Creations(level_one):
    
    platforms = []
    gems = []
    allSprites = pygame.sprite.Group()
    base_platforms = []
    goal = []
    x = 0
    y = 0
    
    for row in level_one: 
        for col in row:
            if col == "M": 
                Mid_Platform = Image((255,255,255),"grassMid.png", (x,y), (70, 70))
                platforms.append(Mid_Platform)
                allSprites.add(Mid_Platform)
                if (y == 1260): 
                    base_platforms.append(Mid_Platform)
            if col == "L": 
                Start_Platform = Image((255,255,255),"grassLeft.png", (x,y), (70, 70))
                platforms.append(Start_Platform)
                allSprites.add(Start_Platform)
                if (y == 1260): 
                    base_platforms.append(Start_Platform)
            if col == "R": 
                End_Platform = Image((255,255,255),"grassRight.png", (x,y), (70, 70))
                platforms.append(End_Platform)
                allSprites.add(End_Platform)
                if (y == 1260): 
                    base_platforms.append(End_Platform)
            if col == "C": 
                Start_Ledge = Image((255,255,255),"grassCliffLeft.png", (x,y), (63,40))
                platforms.append(Start_Ledge)
                allSprites.add(Start_Ledge)
            if col == "D": 
                End_Ledge = Image((255,255,255),"grassCliffRight.png", (x,y), (63,40))
                platforms.append(End_Ledge)
                allSprites.add(End_Ledge)
            if col == "B": 
                Box = Image((255,255,255),"box.png", (x,y), (70, 70))
                platforms.append(Box)
                allSprites.add(Box)
            if col == "F": 
                Sign = Image((255,255,255),"signExit.png", (x,y), (70, 70))
                goal.append(Sign)
                allSprites.add(Sign)
            if col == "G": 
                InvisGem = Gem((255,255,255), "ghost.png", (x,y), "Invisibility")
                gems.append(InvisGem)
                allSprites.add(InvisGem)
            if col == "H": 
                Sign = Image((255,255,255),"hill_small.png", (x,y - 36), (48, 106))
                allSprites.add(Sign)
            if col == "S": 
                JumpGem = Gem((255,255,255),"springboardUp.png", (x,y), "Jumping")     
                gems.append(JumpGem)
                allSprites.add(JumpGem)    
            x += 70; 
        y += 70;
        x = 0;  
    return (platforms, gems, allSprites, base_platforms, goal)

screen = pygame.display.set_mode(View_Screen)

level_tutorial= [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X                            B                    B                                      X",
        "X                            B                    B                                      X",
        "X                            B            CMMMMMD B                                      X",
        "X                            B                    B                                      X",
        "X                            B         CMD        B                                      X",
        "X                            B                    B                                      X",
        "X                            B                    B                                      X",
        "X                   CMMMD    B              CMMMMMBMMD                       B           X",
        "X                            B    CMMMMD          B                          B           X",
        "X                            B                    B                          B           X",
        "X        CMMMMMMMMD          B                    B                          B           X",
        "X                            B           CMMMD    B               S          B           X",
        "X                            B                    B              CMMMMMD     B           X",
        "X                    CMMD    B                    B                          B           X",
        "X            CMMMD           B     CMMMMD    BB   B       CMMD               B           X",  
        "X                                            BB   B                          B           X", 
        "X                                 G          BB   B                          B           X",
        "LMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR",
        ]

platforms_tutorial, gems_tutorial, allSprites_tutorial, base_platforms_tutorial, goals_tutorial = Level_Vector_Creations(level_tutorial)

level_one= [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X                                                                                                                                       X",
        "X                                                                          CMMMMMD                                                      X",
        "X     CMMMMMD                                CMMMMMD                                    CMD                                             X",
        "X                                                                                                  CMD                                  X",
        "X                      CMMMD          CMD                                                                                               X",
        "X                                                                           CMD            CMD                                          X",
        "X                                                      H                                             S   H                     B        X",
        "X               H                CMMMMD               CMMMMD                                        CMMMMD                     B        X",
        "X            CMMMMMMMMMMD                                                       B       H                                      B        X",
        "X                                                                          CMD  B      CMMMMMD                                 B        X",
        "X                                                                               B                                              B        X",
        "X  CMMMMD                               CMMMD              B        CMD         B                 CMMD                    CMD  B        X",
        "X                B                                         B                    B            H                                 B        X",
        "X         G      B   CMMD                         CMMMMD   B              CMD   B          CMMMD                               B        X",
        "X      CMMMD     B                CMMMMD                   B                    B                                      CMD     B        X",  
        "X                B           B                H            B         CMMD       B    CMD                          BB           B        X", 
        "X                B   H  H    B               CMMMMD        B    H               B             H        H         BBB           B       FX",
        "LMMMMMMR   LMMMMMMMMMMMMMMMMMMMMMR                   LMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR",
        ]


gamestate = 1

title = Menu( (255,255,255), "TITLE.png", (30, 50), 0)
menus = []
menus.append(Menu( (255,255,255),"PLAY.png", (150,200), 0))
menus.append(Menu( (255,255,255),"Setting.png", (450,200), 0))
menus.append(Menu( (255,255,255),"Customize.png", (150,350), 0))
menus.append(Menu( (255,255,255),"Instructions.png", (450,350), 4))

end_men = []
end_men.append((Menu( (255,255,255),"MainMenu.png", (150,360), 1)) )
end_men.append((Menu( (255,255,255),"QUIT.png", (450,360), -1)) )

sky = pygame.image.load('bg.png').convert()
player_tutorial_sprite_vec = pygame.sprite.Group()
player_tutorial = Character()
player_tutorial_sprite_vec.add(player_tutorial)
pygame.mixer.init()

player_sprite_vec = pygame.sprite.Group()
player = Character()
player_sprite_vec.add(player)
pygame.mixer.init()

done = False

main_men = pygame.display.set_mode([800, 600])
while (not done):
    quit_game = False

    if (gamestate == -1):
        done = True
    elif (gamestate == 0):
        platforms_l1, gems_l1, allSprites_l1, base_platforms_l1, goal_l1 = Level_Vector_Creations(level_one)
        gamestate = Level_Screens(platforms_l1, gems_l1, allSprites_l1, base_platforms_l1, player, level_one, sky, player_sprite_vec, goal_l1)

        if (player.lives > 0):
            player.reset()
        else:
            gamestate = 5

    elif (gamestate == 1):
        main_men.fill([208,244,247]) 
        main_men.blit(title.image, title)
        for menu_item in menus:
            main_men.blit(menu_item.image, menu_item)
        ev = pygame.event.get()
        for event in ev:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                for menu_item in menus:
                    if menu_item.rect.collidepoint(pos):
                        gamestate = menu_item.type
            elif (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                gamestate = -1
        pygame.display.update()
    elif (gamestate == 2):
        #Change this to settings page
        gamestate = 0
    elif(gamestate == 3):
        #Change this to customization page
        gamestate = 0
    elif (gamestate == 4):
        #Change this to Instructions page
        platforms_tutorial, gems_tutorial, allSprites_tutorial, base_platforms_tutorial, goals_tutorial = Level_Vector_Creations(level_tutorial)
        gamestate = Level_Screens(platforms_tutorial, gems_tutorial, allSprites_tutorial, base_platforms_tutorial, player_tutorial, level_tutorial, sky, player_tutorial_sprite_vec, goals_tutorial)
        gamestate = 1
    elif (gamestate == 5):
        #End of game score, etc
        end_screen = pygame.display.set_mode([800, 600])
        
        score = player.getTime() * 10
        
        end_screen.fill([208,244,247])
        
        if (player.complete): 
            display_box(end_screen, "Great Job! Level Completed!", 150, 210, 0)
            display_box(end_screen, "Score: %d", 325, 270, score)
        else: 
            display_box(end_screen, "Better Luck Next Time!", 150, 250, 0)
        
        for men in end_men:
            end_screen.blit(men.image, men)
               
        pygame.display.update()

        ev = pygame.event.get()
        for event in ev:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                for men in end_men:
                    if men.rect.collidepoint(pos):
                        gamestate = men.type
            elif (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                gamestate = -1
