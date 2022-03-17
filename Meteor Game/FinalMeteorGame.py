#imports pygame and initiates all the pygame commands
import pygame
import time
import random

pygame.init()
#Sets pygame display
width=800
height=600
#256 colours, but since 0 is also included, max is 255
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Meteor Dodge')
clock = pygame.time.Clock()
SshipImg = pygame.image.load('assets/SSSSSHIP.png')
shipImg = pygame.transform.scale(SshipImg, (80,80)) #Changes dimensions of image
SspaceImg = pygame.image.load('assets/Back.png')

SspacerockImg = pygame.image.load('assets/SpaceRock.png')
spacerockImg = pygame.transform.scale(SspacerockImg, (100,100))

def score(n):
    font = pygame.font.Font(None,40)
    text = font.render('Score: '+str(n), True, white)
    win.blit(text,(10,10))


#mx=meteor x, my= meteor y, and so on: width, height
def meteor(mx,my):
    win.blit(spacerockImg,(mx, my))

def ship(x,y):
    win.blit(shipImg, (x,y))

def crash():
    font = pygame.font.Font(None, 115)
    text= font.render('You Crashed!', False, white)
    win.blit(text, (width/2-268,height/2-57))
    pygame.display.update()
    time.sleep(2)
    game_loop()

def game_loop():
    x=(width*0.45)
    y=(height*0.6)
    x_vel=0
    y_vel=0
    n=0
    shipd=80

    meteorx = random.randrange(0,width) # meteor comes from random x( from 0 to the end which is the width)
    meteory = -500
    meteorVel = 4
    meteorw = 100
    meteorh = 100

    gameExit = False#if car crashed, game closes

    while not gameExit:
        win.blit(SspaceImg,(0,0))
        
        #This goes through every Event in the list to see whats being done, such as clicking or pressing a key
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #This checks the event type, which is clicking=QUIT means the red X
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_a]:
                x_vel=-8
            elif keys[pygame.K_d]:
                x_vel=8
            else:
                x_vel=0
            if keys[pygame.K_w]:
                y_vel=-8
            elif keys[pygame.K_s]:
                y_vel=8
            else:
                y_vel=0

        #Controls boundaries

        x+=x_vel
        y+=y_vel
        # win.fill(white)
        # meteor(mx,my,mw,mh):
        meteory+=meteorVel
        meteor(meteorx, meteory)
        ship(x,y)
        score(n)
        
        if x<0 or x>width-shipd or y<0 or y>height-shipd:
            crash()

        if meteory>height:
            meteory= 0 - meteorh
            meteorx=random.randrange(0,width)
            n+=1
            if meteorVel<=14:
                meteorVel+=1

        if y>meteory and y<meteory+meteorh or y+shipd>meteory and  y+shipd<meteory+meteorh: #checks for any collision in the Y cords -- OR ACC, X AXIS
            if x>meteorx and x<meteorx+meteorw or x+shipd>meteorx and x+shipd<meteorx+meteorw: #checks for any collision in the X cords -- OR ACC, Y AXIS
                print("Collision")
                crash()
                
               
        pygame.display.update() #flip also works
        clock.tick(60) #Number in the parameter is the FPS of the game

game_loop()
pygame.quit() #this is like uninitiates the pygame
quit()