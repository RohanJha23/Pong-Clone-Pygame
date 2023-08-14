import pygame

pygame.init()

running = True
# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
# Used to adjust the frame rate
clock = pygame.time.Clock()
FPS = 30

class Striker:

    def _init_(self,posx,posy,width,height,speed,colour):
        self.posx=posx
        self.posy=posy
        self.width=width
        self.height=height
        self.speed=speed
        self.colour=colour

        #Create Rectangle to display on screen
        self.Rectangle= pygame.Rect(posx,posy,width,height)
        #blit on screen or draw on screen//creation only
        self.RectDraw= pygame.draw.rect(screen,self.colour,self.Rectangle)

        def display(self):
            #function to actually draw on screen
            self.RectDraw= pygame.draw.rect(screen,self.colour,self.Rectangle)

        def update(self,yFac):
            #for updating after key movement!
            self.posy=self.posy +self.speed*yFac


            #restricting to window limits
            if self.posy<=0:
                self.posy=0

            #lower level restriction
            elif self.posy + self.height >=HEIGHT:
                self.posy =HEIGHT-self.height
            
            #draw new rectangle by updating
            self.Rectangle = (self.posx,self.posy,self.width,self.height)


        def ScoreDisp(self,text,score,x,y,colour);
            text = font20.render(text+str(score), True, color)
            textRect = text.get_rect()
            textRect.center = (x, y)
 
            screen.blit(text, textRect)

        def getRect(self):
            return self.Rectangle
        



