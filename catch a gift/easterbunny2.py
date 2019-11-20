#pygamedemo1.py
#initialize window
import pygame
import time
import random

pygame.init()   
display_width=1280
display_height=853
card_width=200
size=(display_width,display_height)
white = pygame.image.load('background2.jpg')
screen = pygame.display.set_mode(size)
black = (0,0,0)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((display_width,display_height)) #window size

pygame.display.set_caption('Catch-a-Gift')   #window title

clock = pygame.time.Clock() #clock - imposes time

socks=pygame.image.load('sock1.png')
gift1=pygame.image.load('gift.png')
gift2=pygame.image.load('gift.png')
poop=pygame.image.load('poop.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 35)
    text = font.render('Gifts collected: '+str(count), True, black)
    gameDisplay.blit(text,(60,60))
#def thing(thingx, thingy, thingw, thingh, color):
    #pygame.draw.rect(gameDisplay, color,[thingx, thingy, thingw, thingh])
def thing(thingx, thingy, thingw, thingh):
    gameDisplay.blit(gift1,(thingx, thingy, thingw, thingh))
def thing2(thingx2, thingy2, thingw, thingh):
    gameDisplay.blit(gift2,(thingx2, thingy2, thingw, thingh))
def thing3(thingx3, thingy3, thingw, thingh):
    gameDisplay.blit(poop,(thingx3, thingy3, thingw, thingh))
def thing4(thingx4, thingy4, thingw, thingh):
    gameDisplay.blit(poop,(thingx4, thingy4, thingw, thingh))

def car(x,y):
    gameDisplay.blit(socks,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('Game Over')

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

def game_loop():    
    x = display_width * 0.45
    y = display_height * 0.7

    crashed = False
    x_change = 0

    
    thing_speed = 7
    thing_width = 76
    thing_height = 93
    dodged = 0
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_startx2 = random.randrange(0,display_width)
    thing_starty2 = -600
    thing_startx3 = random.randrange(0,display_width)
    thing_starty3 = -600
    thing_startx4 = random.randrange(0,display_width)
    thing_starty4 = -600

    
    while not crashed:
        for event in pygame.event.get(): #per frame
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                if event.key == pygame.K_RIGHT:
                    x_change = 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   x_change = 0
        x += x_change
        #gameDisplay.fill(white)
        #gameDsiplay.image
        screen.blit(white, [0,0]) 
        thing(thing_startx, thing_starty, thing_width, thing_height)
        thing2(thing_startx2, thing_starty2, thing_width, thing_height)
        thing3(thing_startx3, thing_starty3, thing_width, thing_height)
        thing4(thing_startx4, thing_starty4, thing_width, thing_height)
        thing_starty += thing_speed
        thing_starty2 += thing_speed
        thing_starty3 += thing_speed
        thing_starty4 += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - card_width or x < 0:
            crash()
        #random things
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
        if thing_starty2 > display_height:
            thing_starty2 = 0 - thing_height
            thing_startx2 = random.randrange(0, display_width)
        if thing_starty3 > display_height:
            thing_starty3 = 0 - thing_height
            thing_startx3 = random.randrange(0, display_width)
            thing_speed +=0.5
        if thing_starty4 > display_height:
            thing_starty4 = 0 - thing_height
            thing_startx4 = random.randrange(0, display_width)
            thing_speed +=0.5
        
        #collission detection
        if y < thing_starty + thing_height or y < thing_starty2 + thing_height or y < thing_starty3 + thing_height:
            if x > thing_startx and x < thing_startx + thing_width/2 or x + card_width > thing_startx and x + card_width < thing_startx + thing_width:
                dodged += 1
                thing_startx=-600
            elif x > thing_startx2 and x < thing_startx2 + thing_width/2 or x + card_width > thing_startx2 and x + card_width < thing_startx2 + thing_width:
                dodged += 1
                thing_startx2=-600
            elif x > thing_startx3 and x < thing_startx3 + thing_width/2 or x + card_width > thing_startx3 and x + card_width < thing_startx3 + thing_width/2:
                print ('x crossover')
                crash()
            elif x > thing_startx4 and x < thing_startx4 + thing_width/2 or x + card_width > thing_startx4 and x + card_width < thing_startx4 + thing_width/2:
                crash()
         
   
        pygame.display.update() #pygame.display.flip()-redrawing the image
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()
            
    
    
