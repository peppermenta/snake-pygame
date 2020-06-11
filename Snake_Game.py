
from random import randint
import pygame

pygame.init()
ScreenWidth=500
ScreenHeight=500
win = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("Snake")
run = True
score=0
scoreFont=pygame.font.SysFont('comicsans',40)


#images-------------------------------------------------------------------------------------------
bg = pygame.image.load('Snake_Images/Bg.png')
rabbitImage= pygame.image.load('Snake_Images/Rabbit.png')
rightHead= pygame.image.load('Snake_Images/Snake_2.png')
leftHead=pygame.image.load('Snake_Images/Snake_4.png')
upHead=pygame.image.load('Snake_Images/Snake_1.png')
downHead=pygame.image.load('Snake_Images/Snake_3.png')
horizontalBody=pygame.image.load('Snake_Images/Snake_14.png')
verticalBody=pygame.image.load('Snake_Images/Snake_13.png')
topRight=pygame.image.load('Snake_Images/Snake_9.png')
topLeft=pygame.image.load('Snake_Images/Snake_12.png')
bottomRight=pygame.image.load('Snake_Images/Snake_10.png')
bottomLeft=pygame.image.load('Snake_Images/Snake_11.png')
tailLeft=pygame.image.load('Snake_Images/Snake_8.png')
tailRight=pygame.image.load('Snake_Images/Snake_6.png')
tailUp=pygame.image.load('Snake_Images/Snake_5.png')
tailDown=pygame.image.load('Snake_Images/Snake_7.png')
#endimages-------------------------------------------------------------------------------------------------

columns = ScreenWidth//16#making the windows into a grid
rows = ScreenHeight//16#making the windows into a grid
class snake(object):

    def __init__(self):
        self.width=16
        self.height=16
        self.v =16
        self.length=3
        self.x=[0,16,32] 
        self.y=[0,0,0]
        
    def draw(self):
        headDir=[self.x[0]-self.x[1],self.y[0]-self.y[1]]
        if(headDir==[16,0]):
            win.blit(rightHead,(self.x[0],self.y[0]))
        elif(headDir==[-16,0]):
            win.blit(leftHead,(self.x[0],self.y[0]))
        elif(headDir==[0,16]):
            win.blit(downHead,(self.x[0],self.y[0]))
        elif(headDir==[0,-16]):
            win.blit(upHead,(self.x[0],self.y[0]))

        for i in range (1,self.length-1):
            dif1=(self.x[i]-self.x[i-1],self.y[i]-self.y[i-1])
            dif2=(self.x[i]-self.x[i+1],self.y[i]-self.y[i+1])
            if(dif1==(0,16)):
                if(dif2==(16,0)):
                    win.blit(topLeft,(self.x[i],self.y[i]))
                    
                elif(dif2==(-16,0)):
                    win.blit(topRight,(self.x[i],self.y[i]))
                    
                elif(dif2==(0,-16)):
                    win.blit(verticalBody,(self.x[i],self.y[i]))
                    
            elif(dif1==(-16,0)):
                if(dif2==(0,-16)):
                    win.blit(bottomRight,(self.x[i],self.y[i]))
                    
                elif(dif2==(16,0)):
                    win.blit(horizontalBody,(self.x[i],self.y[i]))
                    
                elif(dif2==(0,16)):
                    win.blit(topRight,(self.x[i],self.y[i]))
                    
            elif(dif1==(0,-16)):
                if(dif2==(16,0)):
                    win.blit(bottomLeft,(self.x[i],self.y[i]))
                    
                elif(dif2==(0,16)):
                    win.blit(verticalBody,(self.x[i],self.y[i]))
                    
                elif(dif2==(-16,0)):
                    win.blit(bottomRight,(self.x[i],self.y[i]))
                    
            elif(dif1==(16,0)):
                if(dif2==(0,16)):
                    win.blit(topLeft,(self.x[i],self.y[i]))
                    
                elif(dif2==(-16,0)):
                    win.blit(horizontalBody,(self.x[i],self.y[i]))
                    
                elif(dif2==(0,-16)):
                    win.blit(bottomLeft,(self.x[i],self.y[i]))
                    

            tailDir=(self.x[-2]-self.x[-1],self.y[-2]-self.y[-1])
            if(tailDir==(16,0)):
                win.blit(tailRight,(self.x[-1],self.y[-1]))
            elif(tailDir==(0,16)):
                win.blit(tailDown,(self.x[-1],self.y[-1]))
            elif(tailDir==(-16,0)):
                win.blit(tailLeft,(self.x[-1],self.y[-1]))
            elif(tailDir==(0,-16)):
                win.blit(tailUp,(self.x[-1],self.y[-1]))
    def rePos(self,x,y):
        i=self.length-1
        while(i>=1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
            i-=1
        self.x[0]+=x
        self.y[0]+=y
            
    def grow(self):
        newX = -(self.x[-1]-self.x[-2])
        newY = -(self.y[-1]-self.y[-2])
        self.x.append(self.x[-1]+newX)
        self.y.append(self.y[-1]+newY)
        self.length +=1

class food:
    def __init__(self):
       
       self.x = (columns//2)*16
       self.y= (rows//2)*16

    def draw(self):
        win.blit(rabbitImage,(self.x,self.y))

    def rePos(self,x,y):
        self.x=x
        self.y=y
        

foodCount=0
s = snake()
rabbit = food()
def drawGame():
    win.blit(bg,(0,0))
    s.draw()
    rabbit.draw()
    scoreText = scoreFont.render("Score:"+str(score),True,(0,0,255))
    win.blit(scoreText,(350,10))
    pygame.display.update()


while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] and s.x[0]>s.v and s.x[0]-s.v!=s.x[1]):
        s.rePos(-s.v,0)
    if(keys[pygame.K_RIGHT] and s.x[0]+s.v+s.width<ScreenWidth and s.x[0]+s.v!=s.x[1]):
        s.rePos(s.v,0)
    if(keys[pygame.K_UP] and s.y[0]>s.v and s.y[0]-s.v!=s.y[1]):
        s.rePos(0,-s.v)
    if(keys[pygame.K_DOWN] and s.y[0]+s.v+s.height<ScreenHeight and s.y[0]+s.v!=s.y[1]):
        s.rePos(0,s.v)
    
    if(s.x[0]==rabbit.x and s.y[0]==rabbit.y):
        rabbit.rePos(randint(1,columns-1)*16,randint(1,rows-1)*16)
        score+= (5*(s.length//5))
        
        s.grow()

    
        
    drawGame()
    
pygame.quit() 
 
