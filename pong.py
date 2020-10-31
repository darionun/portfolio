import pygame
import time
import random

pygame.init()
# Definicion de Variables

WIDTH = 900
HEIGHT = 600
BORDER = 10
VELOCITY = 1
WIDTH_paddle = 20
HEIGHT_paddle = 100

# Definicion de las clases

class Ball:
    
    RADIUS = 10

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def show(self, colour):
        global screen
        pygame.draw.circle(screen, colour, (self.x, self.y), self.RADIUS)
    
    def update(self):
        global bgcolor, fgcolor

        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER+self.RADIUS:
            self.vx = -self.vx

        elif newy < BORDER+self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy

        elif newx >= paddle.x and \
             newx <= paddle.x + paddle.WIDTH_paddle and\
             newy >= paddle.y and \
             newy <= paddle.y + paddle.HEIGHT_paddle:
                
            self.vx = -self.vx
            self.vy = -self.vy
        
        else:
            self.show(bgcolor)
            self.x += self.vx
            self.y += self.vy
            self.show(fgcolor)


class Paddle:
    
    WIDTH_paddle = 20
    HEIGHT_paddle = 100
    
    def __init__(self, y, x):
        self.y = y
        self.x = x
            
    def show(self, colour):
        global screen
        pygame.draw.rect(screen, colour, pygame.Rect(WIDTH-self.WIDTH_paddle, self.y, HEIGHT_paddle, HEIGHT_paddle))
    
    def update(self):
        self.show(bgcolor)
        self.y = pygame.mouse.get_pos()[1]
        self.show(fgcolor)

    

# Definicion de objetos


ballPlay = Ball(WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY)

paddle = Paddle(HEIGHT, WIDTH)


    
# Definicion del Escenario principal

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgcolor = pygame.Color("black")
fgcolor = pygame.Color("white")

pygame.draw.rect(screen, fgcolor, pygame.Rect((0, 0),(WIDTH, BORDER))) 
pygame.draw.rect(screen, fgcolor, pygame.Rect(0, 0, BORDER, HEIGHT))
pygame.draw.rect(screen, fgcolor, pygame.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))

ballPlay.show(fgcolor)
paddle.show(fgcolor)



while True:
    time.sleep(0)
    e=pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    

    ballPlay.update()
    paddle.update()
    pygame.display.flip()



pygame.quit()
