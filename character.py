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

    def updateTime(self, val):
        self.time += val
        
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
        if ((TOTALTIME - self.time + spawn) <= 0 ): 
            return True
        return False
    
    def reset(self, loc):
        player.x =  loc[0]
        player.y = loc[1]
        player.rect.x = loc[0]
        player.rect.y = loc[1]