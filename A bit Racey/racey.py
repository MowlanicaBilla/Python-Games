import pygame
import time
import random

# Instantiating the pygame
pygame.init()

display_width = 800
display_height = 600


black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

car_width = 73

#Creating a window
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

# Defining a clock
clock = pygame.time.Clock()
# Simple enough, this is a our game clock. We use this to track time within the game, and this is mostly used for FPS, or "frames per second." While somewhat trivial seeming, FPS is very important, and can be tweaked as we will see later. For the most part, the average human eye can see ~30 FPS.

crash = False

carImg = pygame.image.load('racecar.png')

## Pygame Score
def things_dodged(count):
	font = pygame.font.SysFont(None,25)
	text = font.render("Dodged:"+str(count),True,black)
	gameDisplay.blit(text,(0,0))

######
## Creating Obstracles

def things(thingx, thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

######

def car(x,y):
	gameDisplay.blit(carImg,(x,y))
	
"""
msg: What do you want the button to say on it.

x: The x location of the top left coordinate of the button box.

y: The y location of the top left coordinate of the button box.

w: Button width.

h: Button height.

ic: Inactive color (when a mouse is not hovering).

ac: Active color (when a mouse is hovering).


"""

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def text_objects(text,font):
	textSurface = font.render(text,True,black)
	return textSurface,textSurface.get_rect()
	
def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',100)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	
	pygame.display.update()
	
	time.sleep(2)
	
	game_loop()
	
	
def crash():
	message_display('Ohh no..!! You crashed..!!')
	
	
def quitgame():
    pygame.quit()
    quit()
	
	
## Creating a Game menu
def game_intro():
	
	intro = True
	
	while intro:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		gameDisplay.fill(white)
		largeText = pygame.font.SysFont('comicsansms',100)
		TextSurf,TextRect = text_objects("A bit Racey",largeText)
		TextRect.center = ((display_width/2,(display_height/2)))
		gameDisplay.blit(TextSurf,TextRect)
		
		
		button("GO!",150,450,100,50,green,bright_green,game_loop)
		button("QUIT!",550,450,100,50,red,bright_red,quitgame)
		
		'''
		mouse = pygame.mouse.get_pos()
		
		#pygame.draw.rect(gameDisplay,green,(150,450,100,500))
		#pygame.draw.rect(gameDisplay,red,(550,450,100,50))
		
		if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
			pygame.draw.rect(gameDisplay,bright_green,(150,450,100,50))
			
		else:
			pygame.draw.rect(gameDisplay,green,(150,450,100,50))
		
		
		smallText = pygame.font.Font('freesansbold.ttf',20)
		textSurf ,textRect = text_objects("GO..!!",smallText)
		textRect.center = ((150+(100/2)),(450+(50/2)))
		gameDisplay.blit(textSurf,textRect)
		
		pygame.draw.rect(gameDisplay,red,(550,450,100,50))
		
		'''
		
		pygame.display.update()
		clock.tick(15)
		
	
def game_loop():	
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x_change = 0
	
	######
	
	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed = 7 
	thing_width = 100
	thing_height = 100
	
	dodged = 0
	
	gameExit = False


	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
			#############################
			# Moving the image around
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
			##############################
		x += x_change # "x" is used to position our car image in the car function.
		
		gameDisplay.fill(white)
		######
		things(thing_startx,thing_starty,thing_width,thing_height,block_color)
		thing_starty += thing_speed
			
		######		
		car(x,y)
		
		things_dodged(dodged)
		
		if x > display_width - car_width or x < 0:
			crash()
			
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			dodged += 1
			thing_speed += 1
			thing_width += (dodged * 1.2)
			
		#####
		if y < thing_starty+thing_height:
			print('y crossover')
			
			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
				print('x crossover')
				crash()
		
		#####
			
			
		pygame.display.update()
		clock.tick(60)
	
game_intro()
game_loop()
pygame.quit()
quit()