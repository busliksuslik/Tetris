import pygame, random

colors = ('blue','red','green','yellow','violet','orange')

class Pile():
    def __init__(self):
        self.dots_array = []
        self.blocks_array = []
    def match(self,x,y):
        return (x,y) in self.dots_array
    def destr(self):
        count = 0
        for m in range(21):
            for k in range(11):
                if self.match(m*20,k*20):
                    count+=1
            if count >= 10:
                pr = m
        for i in range(len(self.dots_array)):
            for m in range(11):
                if self.dots_array[i] == (m*20, pr):
                    del self.dots_array[i]
                        
                    
                
                
                
        
class Tetramino_factory():
    def __init__(self):
        self.tetramino_array = []
    def add(self):
        ch = random.randint(0,1)
        if ch == 0:
            self.tetramino_array.append(Stick(sc))
        elif ch == 1:
            self.tetramino_array.append(Square(sc))
#        if ch = 2:
#            self.tetramino_array.append(Snake_right(sc))
#        if ch = 3:
#            self.tetramino_array.append(Snake_left(sc))
#        if ch = 4:
#            self.tetramino_array.append(Leg_right(sc))
#        if ch = 5:
#            self.tetramino_array.append(Leg_left(sc))
        fac.tetramino_array[-1].make()

class Block():
    def __init__(self, color, sc):
        self.color = color
        self.sc = sc
        self.block_surf = pygame.image.load('block_'+color+'.png')
        self.coord = (0,0)
        
    def draw(self):
        self.block_rect = self.block_surf.get_rect(topleft=(self.coord))
        sc.blit(self.block_surf, self.block_rect)
    
    def move_down(self):
        x,y = self.coord 
        self.coord = (x - 20 , y)
        
class Tetramino():
    def __init__(self,sc):
        self.move = True
        self.sc = sc
        self.make()
        self.position = 0
    def draw(self):
        for i in range(len(self.block_array)):
            self.block_array[i].draw()
    def make(self):
        pass
    def rotate(self):
        pass
    def move_down(self):
        if self.move:
            self.y +=20
            self.pos()
        for i in range(0,4):
            if self.block_array[i].coord in pile.dots_array:
                self.y -=20
                self.pos()
                self.stop()
                break
    def move_left(self):
        if self.move:
            self.x -=20
    def move_right(self):
        if self.move:
            self.x +=20
    def move_up (self):
        if self.move:
            self.y -=20
    def stop(self):
        self.move = False
        fac.add()
        for i in range(0,4):
            pile.dots_array.append(self.block_array[i].coord)
            pile.blocks_array.append(self.block_array)
class Stick(Tetramino):
    def make(self):
        self.color = 'blue'
        self.x = 80
        self.y = -80
        self.block_array = [Block(self.color,self.sc) for i in range(4)]
    def rotate(self):
        if self.move:
            self.position = (self.position + 1) % 2
    def pos(self):
        if self.position == 0:
            self.block_array[0].coord = (self.x,self.y-40)
            self.block_array[1].coord = (self.x,self.y-20)
            self.block_array[2].coord = (self.x,self.y)
            self.block_array[3].coord = (self.x,self.y+20)
            if self.y == 360:
                self.stop()
        elif self.position == 1:
            self.block_array[0].coord = (self.x - 40,self.y)
            self.block_array[1].coord = (self.x - 20,self.y)
            self.block_array[2].coord = (self.x,self.y)
            self.block_array[3].coord = (self.x + 20,self.y)
            if self.y == 400:
                self.stop()


class Square(Tetramino):
    def make(self):
        self.color = 'red'
        self.x = 80
        self.y = -40
        self.block_array = [Block(self.color,self.sc) for i in range(4)]
    def pos(self):
        self.block_array[0].coord = (self.x - 20, self.y-20)
        self.block_array[1].coord = (self.x,self.y-20)
        self.block_array[2].coord = (self.x - 20,self.y)
        self.block_array[3].coord = (self.x,self.y)
        if self.y == 400:
                self.stop()

class Snake_right(Tetramino):
    def make(self):
        self.color = 'green'
        self.x = 80
        self.y = -60
        self.block_array = [Block(self.color,self.sc) for i in range(4)]
        self.block_array[0].coord = (self.x - 20, self.y-20)
        self.block_array[1].coord = (self.x,self.y-20)
        self.block_array[2].coord = (self.x - 20,self.y)
        self.block_array[3].coord = (self.x,self.y)
            
    
            
        
        
 
FPS = 10
W = 200  # ширина экрана
H = 400  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

fac = Tetramino_factory()

fac.add()


pile = Pile()


while 1:
    sc.fill(WHITE)
    
    for i in range(len(fac.tetramino_array)):

        fac.tetramino_array[i].draw()
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                fac.tetramino_array[-1].move_left()
            elif i.key == pygame.K_RIGHT:
                fac.tetramino_array[-1].move_right()
            elif i.key == pygame.K_UP:
                fac.tetramino_array[-1].rotate()
    fac.tetramino_array[-1].pos()
    fac.tetramino_array[-1].move_down()
    pile.destr()

 
    clock.tick(FPS)