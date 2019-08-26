# ABOUT THE GAME

# Description: Several bad guys fall from the top of the screen, and the user must avoid them. The player can be controlled with the arrow keys or more directly with the mouse. The longer the player lasts without being hit, the higher the score.

# Variations: Have enemies fall at different rates and be different sizes. Have enemies fall from more than one side of the game. Have power up pickups that grant invulnerability for a while, slow down bad guys, give the player a temporary "reverse bad guys" power, etc.


# Importing required packages

import pygame, random, sys
from pygame.locals import *


## Setting Up the Constant Variables since it is easier to change

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255,255,255)
BACKGROUNDCOLOR = (0,0,0)
FPS = 40

"""
The mainClock.tick() method call will slow the game down enough to be playable. You pass an integer to mainClock.tick() so that the function knows how long to pause the program. This integer (which you store in FPS) is the number of frames per second you want the game to run.

A “frame” is the drawing of graphics on the screen for a single iteration through the game loop. You can set FPS to 40, and always call mainClock.tick(FPS). Then you can change FPS to a higher value to have the game run faster or a lower value to slow the game down.
"""

BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6

"""
The above constant variables that will describe the falling baddies. The width and height of the baddies will be between BADDIEMINSIZE and BADDIEMAXSIZE. The rate at which the baddies fall down the screen will be between BADDIEMINSPEED and BADDIEMAXSPEED pixels per iteration through the game loop. And a new baddie will be added to the top of the window every ADDNEWBADDIERATE iterations through the game loop.

"""

PLAYERMOVERATE = 5

# The PLAYERMOVERATE will store the number of pixels the player’s character moves in the window on each iteration through the game loop if the character is moving. By increasing this number, you can increase the speed the character moves.

def terminate():
	pygame.quit()
	sys.exit()

# Pygame requires that you call both pygame.quit() and sys.exit(). Put them both into a function called terminate(). Now you only need to call terminate(), instead of both of the pygame.quit() and sys.exit() functions.

def waitForPlayerToPressKey():
	while True:
		for event in pygame.event.get(): # Sometimes you’ll want to pause the game until the player presses a key. Create a new function called waitForPlayerToPressKey(). Inside this function, there’s an infinite loop that only breaks when a KEYDOWN or QUIT event is received. At the start of the loop, pygame.event.get() to return a list of Event objects to check out.
			if event.type == QUIT:
				terminate() # If the player has closed the window while the program is waiting for the player to press a key, Pygame will generate a QUIT event. In that case, call the terminate() function 
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE: # pressing escape quits
						terminate()
					return # If you receive a KEYDOWN event, then you should first check if it is the ESC key that was pressed. If the player presses the ESC key, the program should terminate. If that wasn’t the case, then execution will skip the if-block on line 48 and go straight to the return statement, which exits the waitForPlayerToPressKey() function. If a QUIT or KEYDOWN event isn’t generated, then the code keeps looping. Since the loop does nothing, this will make it look like the game has frozen until the player presses a key.
					
def playHasHitBaddie(playerRect,baddies):
	for b in baddies:
		if playerRect.colliderect(b['rect']):
			return True
		return False
	
# The playerHasHitBaddie() function will return True if the player’s character has collided with one of the baddies. The baddies parameter is a list of “baddie” dictionary data structures. Each of these dictionaries has a 'rect' key, and the value for that key is a Rect object that represents the baddie’s size and location.

# playerRect is also a Rect object. Rect objects have a method named colliderect() that returns True if the Rect object has collided with the Rect object that is passed to it. Otherwise, colliderect() will return False.

# The for loop on line 53 iterates through each baddie dictionary in the baddies list. If any of these baddies collide with the player’s character, then playerHasHitBaddie() will return True. If the code manages to iterate through all the baddies in the baddies list without detecting a collision with any of them, it will return False.

def drawText(text,font,surface,x,y):
	textobj = font.render(text,1,TEXTCOLOR)
	textrect = textobj.get_rect()
	textobj.topleft = (x,y)
	surface.blit(textobj,textrect)
	
# Drawing text on the window involves a few steps. First, the render() method call on line 65 creates a Surface object that has the text rendered in a specific font on it.

#Next, you need to know the size and location of the Surface object. You can get a Rect object with this information from the get_rect() Surface method.

# The Rect object returned on line 66 from get_rect() has a copy of the width and height information from the Surface object. Line 67 changes the location of the Rect object by setting a new tuple value for its topleft attribute.

# Finally, line 68 blits the Surface object of the rendered text onto the Surface object that was passed to the drawText() function. Displaying text in Pygame take a few more steps than simply calling the print() function. But if you put this code into a single function named drawText(), then you only need to call this function to display text on the screen.

###################

# Initializing Pygame and Setting Up the Window

# Now that the constant variables and functions are finished, start calling the Pygame functions that set up the window and clock.
	
	
# setting up pygame,mouse and the cursor

pygame.init()
mainClock = pygame.time.Clock()

# Line 87 sets up the Pygame by calling the pygame.init() function. Line 88 creates a pygame.time.Clock() object and stores it in the mainClock variable. This object will help us keep the program from running too fast.

windowSurface = pygame.display.set_mode(WINDOWWIDTH,WINDOWHEIGHT)

# Line 92 creates a new Surface object which is used for the window displayed on the screen. You can specify the width and height of this Surface object (and the window) by passing a tuple with the WINDOWWIDTH and WINDOWHEIGHT constant variables. Notice that there’s only one argument passed to pygame.display.set_mode(): a tuple. The arguments for pygame.display.set_mode() are not two integers but one tuple of two integers.

pygame.display.set_caption('Dodger') # Setting the caption for the window

pygame.mouse.set_visible(False)
# In Dodger, the mouse cursor shouldn’t be visible. This is because you want the mouse to be able to move the player’s character around the screen, but the mouse cursor would get in the way of the character’s image on the screen. Calling pygame.mouse.set_visible(False) will tell Pygame to make the cursor not visible.

###########################################

# Fullscreen Mode
# The pygame.display.set_mode() function has a second, optional parameter. You can pass the pygame.FULLSCREEN constant to make the window take up the entire screen instead of being in a window. Look at this modification to line 92:

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)

# It will still be WINDOWWIDTH and WINDOWHEIGHT in size for the windows width and height, but the image will be stretched larger to fit the screen. Try running the program wiuth and without fullscreen mode

# Setting up fonts
font = pygame.font.SysFont(None, 48)
# The above creates a Font object to use by calling pygame.font.SysFont(). Passing None uses the default font. Passing 48 makes the font have a size of 48 points.

# Setting up sounds
gameOverSound = pygame.mixer.Sound('audio/gameover-1.wav')
pygame.mixer.music.load('background.mp3')

# Next, create the Sound objects and set up the background music. The background music will constantly be playing during the game, but Sound objects will only be played when the player loses the game.

# The pygame.mixer.Sound() constructor function creates a new Sound object and stores a reference to this object in the gameOverSound variable. In your own games, you can create as many Sound objects as you like, each with a different sound file.

# The pygame.mixer.music.load() function loads a sound file to play for the background music. This function doesn’t return any objects, and only one background sound file can be loaded at a time.

# Setting up images
playerImage = pygame.image.load('images/horngirl.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('images/Rock.png')


#######################################

# Display the Start Screen

# When the game first starts, display the “Dodger” name on the screen. You also want to instruct the player that they can start the game by pushing any key. This screen appears so that the player has time to get ready to start playing after running the program.

# Show the "Start" screen
drawText('Dodger',font, windowSurface,(WINDOWWIDTH / 3),(WINDOWHEIGHT / 3))
drawText('Press a key to Start.', font,windowSurface,(WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

"""
On lines 144 and 145, call the drawText() function and pass it five arguments:

1)     The string of the text you want to appear.

2)     The font that you want the string to appear in.

3)     The Surface object onto which to render the text.

4)     The X coordinate on the Surface object to draw the text at.

5)     The Y coordinate on the Surface object to draw the text at.

This may seem like many arguments to pass for a function call, but keep in mind that this function call replaces five lines of code each time you call it. This shortens the program and makes it easier to find bugs since there’s less code to check.

The waitForPlayerToPressKey() function will pause the game by looping until a KEYDOWN event is generated. Then the execution breaks out of the loop and the program continues to run.
"""


## START OF THE MAIN GAME CODE 

topScore = 0
while True:
	# The value in the topScore variable starts at 0 when the program first runs. Whenever the player loses and has a score larger than the current top score, the top score is replaced with this larger score.
	# The infinite loop started on line 171 is technically not the “game loop”. The game loop handles events and drawing the window while the game is running. Instead, this while loop will iterate each time the player starts a new game. When the player loses and the game resets, the program’s execution will loop back to line 171.
	# set up the start of the game
	baddies = []
	score = 0
	#At the beginning, you want to set baddies to an empty list. The baddies variable is a list of dictionary objects with the following keys:
	#'rect' - The Rect object that describes where and what size the baddie is.
	#'speed' - How fast the baddie falls down the screen. This integer represents pixels per iteration through the game loop.
	#'surface' - The Surface object that has the scaled baddie image drawn on it. This is the Surface object that is blitted to the Surface object returned by pygame.display.set_mode().
	
	# 176 resets the player's score to 0
	playerRect.topleft = (WINDOWWIDTH / 2 , WINDOWHEIGHT - 50)
	#The starting location of the player is in the center of the screen and 50 pixels up from the bottom. The first item in line 187’s tuple is the X-coordinate of the left edge. The second item in the tuple is the Y-coordinate of the top edge.
	moveLeft = moveRight = moveUp = moveDown = False
	reverseCheat = slowCheat = False
	baddieAddCounter = 0	
	# The movement variables moveLeft, moveRight, moveUp, and moveDown are set to False. The reverseCheat and slowCheat variables are also set to False. They will be set to True only when the player enables these cheats by holding down the “z” and “x” keys, respectively.
	
	# The baddieAddCounter variable is a counter to tell the program when to add a new baddie at the top of the screen. The value in baddieAddCounter increments by one each time the game loop iterates.
	
	#When baddieAddCounter is equal to ADDNEWBADDIERATE, then the baddieAddCounter counter resets to 0 and a new baddie is added to the top of the screen.
	pygame.mixer.music.play(-1,0,0)
	
	# The background music starts playing on line 197 with a call to pygame.mixer.music.play(). The first argument is the number of times the music should repeat itself. -1 is a special value that tells Pygame you want the music to repeat endlessly.The second argument is a float that says how many seconds into the music you want it to start playing. Passing 0.0 means the music starts playing from the beginning.
	
	# GAME LOOP
	# The game loop’s code constantly updates the state of the game world by changing the position of the player and baddies, handling events generated by Pygame, and drawing the game world on the screen. All of this happens several dozen times a second, which makes it run in “real time”.
	while True: # the game loop runs while the game part is playing
	    score +=1 # increase score
		#Line 203 is the start of the main game loop. Line 204 increases the player’s score on each iteration of the game loop. The longer the player can go without losing, the higher their score. The loop will only exit when the player either loses the game or quits the program.
		
		# EVENT HANDLING 
		
		# There are four different types of events the program will handle: QUIT, KEYDOWN, KEYUP, and MOUSEMOTION.
        for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
		# Line 211 is the start of the event-handling code. It calls pygame.event.get(), which returns a list of Event objects. Each Event object represents an event that has happened since the last call to pygame.event.get(). The code will check the type attribute of the event object to see what type of event it is, and handle the event accordingly.
		
		#If the type attribute of the Event object is equal to QUIT, then the user has closed the program. The QUIT constant variable was imported from the pygame.locals module.
		    if event.type == KEYDOWN:
				if event.key == ord('z'):
				    reverseCheat = True
				if event.key == ord('x'):
					slowCheat = True
					
				# If the event’s type is KEYDOWN, the player has pressed down a key. The Event object for keyboard events will also have a key attribute that is set to the integer ordinal value of the key pressed. The ord() function will return the ordinal value of the letter passed to it.
				# For example, line 218 checks if the event describes the “z” key being pressed down with event.key == ord('z'). If this condition is True, set the reverseCheat variable to True to indicate that the reverse cheat has been activated. Line 220 checks if the “x” key has been pressed to activate the slow cheat.
				# Pygame’s keyboard events always use the ordinal values of lowercase letters, not uppercase. Always use event.key == ord('z') instead of event.key == ord('Z'). Otherwise, your program may act as though the key wasn’t pressed.
				if event.key == K_LEFT or event.key == ord('a'):
					moveRight = False
					moveLeft = True
				if event.key == K_RIGHT or event.key == ord('d'):
					moveLeft = False
					moveRight = True
				if event.key == K_UP or event.key == ord('w'):
					moveDown = False
					moveUp = True
				if event.key == K_DOWN or event.key == ord('s'):
					moveUp = False
					moveDown = True
					# Lines 226 to 237 check if the event was generated by the player pressing one of the arrow or WASD keys. There isn’t an ordinal value for every key on the keyboard, such as the arrow keys or the ESC key. Instead, the pygame.locals module provides constant variables to use instead.
					# Line 226 checks if the player has pressed the left arrow key with event.key == K_LEFT. Notice that pressing down on one of the arrow keys not only sets a movement variable to True, but it also sets the movement variable in the opposite direction to False.
					# For example, if the left arrow key is pushed down, then the code on line 228 sets moveLeft to True, but it also sets moveRight to False. This prevents the player from confusing the program into thinking that the player’s character should move in two opposite directions at the same time.
				if event.type == KEYUP:
					if event.key == ord('z'):
						reverseCheat = False
						score = 0
					if event.key == ord('x'):
						slowCheat = False
						score = 0
					# The KEYUP event is created whenever the player stops pressing down on a keyboard key and releases it. Event objects with a type of KEYUP also have a key attribute just like KEYDOWN events.
					# Line 242 checks if the player has released the “z” key, which will deactivate the reverse cheat. In that case, line 106 sets reverseCheat to False and line 244 resets the score to 0. The score reset is to discourage the player for using the cheats.
					# Lines 245 to 247 do the same thing for the “x” key and the slow cheat. When the “x” key is released, slowCheat is set to False and the player’s score is reset to 0.
					if event.key == K_ESCAPE:
						terminate()
						# At any time during the game, the player can press the ESC key on the keyboard to quit. Line 39 checks if the key that was released was the ESC key by checking event.key == K_ESCAPE. If so, line 252 calls the terminate() function to exit the program.
					if event.key == K_LEFT or event.key == ord('a'):
						moveLeft = False 
					if event.key == K_RIGHT or event.key == ord('d'):
						moveRight = False
					if event.key == K_UP or event.key == ord('w'):
						moveUp = False
					if event.key == K_DOWN or event.key == ord('s'):
						moveDown = False
					# Lines 254 to 261 check if the player has stopped holding down one of the arrow or WASD keys. In that case, the code sets the corresponding movement variable to False.
					# For example, if the player was holding down the left arrow key, then the moveLeft would have been set to True on line 228. When they release it, the condition on line 254 will evaluate to True, and the moveLeft variable will be set to False.
				
				## The move_ip() Method
				if event.type == MOUSEMOTION:
					## if the mouse moves,move the player where the cursor is
					playerRect.move_ip(event.pos[0] - playerRect.centerx , event.pos[1] -  playerRect.centery)
				
				#Now that you’ve handled the keyboard events, let’s handle any mouse events that may have been generated. The Dodger game doesn’t do anything if the player has clicked a mouse button, but it does respond when the player moves the mouse. This gives the player two ways of controlling the player character in the game: the keyboard or the mouse.
				#The MOUSEMOTION event is generated whenever the mouse is moved. Event objects with a type set to MOUSEMOTION also have an attribute named pos for the position of the mouse event. The pos attribute stores a tuple of the X- and Y-coordinates of where the mouse cursor moved in the window. If the event’s type is MOUSEMOTION, the player’s character moves to the position of the mouse cursor.
				#The move_ip() method for Rect objects will move the location of the Rect object horizontally or vertically by a number of pixels. For example, playerRect.move_ip(10, 20) would move the Rect object 10 pixels to the right and 20 pixels down. To move the Rect object left or up, pass negative values. For example, playerRect.move_ip(-5, -15) will move the Rect object left by 5 pixels and up 15 pixels.
				#The “ip” at the end of move_ip() stands for “in place”. This is because the method changes the Rect object itself, rather than return a new Rect object with the changes. There is also a move() method which doesn’t change the Rect object, but instead creates and returns a new Rect object in the new location.
			
			## Adding New Baddies
			# add the baddies at the top of the screen, if needed
			if not reverseCheat and not slowCheat:
				baddieAddCounter += 1
			# On each iteration of the game loop, increment the baddieAddCounter variable by one. This only happens if the cheats are not enabled. Remember that reverseCheat and slowCheat are set to True as long as the “z” and “x” keys are being held down, respectively.
			# And while those keys are being held down, baddieAddCounter isn’t incremented. Therefore, no new baddies will appear at the top of the screen.
			
			if baddieAddCounter == ADDNEWBADDIERATE:
				baddieAddCounter = 0
				baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
				newBaddie = {'rect': pygame.Rect(random.randint(0,WINDOWWIDTH- baddieSize), 0 - baddieSize,baddieSize,baddieSize),'speed':random.randint(BADDIEMINSPEED,BADDIEMAXSPEED),'surface':pygame.transform.scale(baddieImage,(baddieSize,baddieSize))}
				# When the baddieAddCounter reaches the value in ADDNEWBADDIERATE, it is time to add a new baddie to the top of the screen. First, the baddieAddCounter counter is reset back to 0.
				# Line 284 generates a size for the baddie in pixels. The size will be a random integer between BADDIEMINSIZE and BADDIEMAXSIZE, which are constants set to 10 and 40 #Line 285 is where a new baddie data structure is created. Remember, the data structure for baddies is simply a dictionary with keys 'rect', 'speed', and 'surface'. The 'rect' key holds a reference to a Rect object which stores the location and size of the baddie. The call to the pygame.Rect() constructor function has four parameters: the X-coordinate of the top edge of the area, the Y-coordinate of the left edge of the area, the width in pixels, and the height in pixels.
				#The baddie needs to appear randomly across the top of the window, so pass random.randint(0, WINDOWWIDTH-baddieSize) for the X-coordinate of the left edge. The reason you pass WINDOWWIDTH-baddieSize instead of WINDOWWIDTH is because this value is for the left edge of the baddie. If the left edge of the baddie is too far on the right side of the screen, then part of the baddie will be off the edge of the window and not visible.
				# The bottom edge of the baddie should be just above the top edge of the window. The Y-coordinate of the top edge of the window is 0. To put the baddie’s bottom edge there, set the top edge to 0 - baddieSize.
				#The baddie’s width and height should be the same (the image is a square), so pass baddieSize for the third and fourth argument.The rate of speed that the baddie moves down the screen is set in the 'speed' key. Set it to a random integer between BADDIEMINSPEED and BADDIEMAXSPEED.
				baddies.append(newBaddie)
				# Line 291 will add the newly created baddie data structure to the list of baddie data structures. The program will use this list to check if the player has collided with any of the baddies, and to know where to draw baddies on the window.
			
			# Moving the Player's character
			# Move the player around
			if moveLeft and playerRect.left > 0:
				playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
				# The four movement variables moveLeft, moveRight, moveUp and moveDown are set to True and False when Pygame generates the KEYDOWN and KEYUP events, respectively.
				# If the player’s character is moving left and the left edge of the player’s character is greater than 0 (which is the left edge of the window), then playerRect should be moved to the left.
				#You’ll always move the playerRect object by the number of pixels in PLAYERMOVERATE. To get the negative form of an integer, multiple it by -1. On line 297, since 5 is stored in PLAYERMOVERATE, the expression -1 * PLAYERMOVERATE evaluates to -5.
				# Therefore, calling playerRect.move_ip(-1 * PLAYERMOVERATE, 0) will change the location of playerRect by 5 pixels to the left of its current location.
			if moveRight and playerRect.right < WINDOWWIDTH:
				playerRect.move_ip(PLAYERMOVERATE,0)
			if moveUp and playerRect.top>0:
				playerRect.move_ip(0,-1 * PLAYERMOVERATE)
			if moveDown and playerRect.bottom < WINDOWHEIGHT:
				playerRect.move_ip(0,PLAYERMOVERATE)
			# Lines 302 to 307 do the same thing for the other three directions: right, up, and down. Each of the three if statements in lines 302 to 307 checks that their movement variable is set to True and that the edge of the Rect object of the player is inside the window. Then it calls move_ip() to move the Rect object.
			
			# The pygame.mouse.set_pos() Function
			# Move the mouse cursor to match the player
			pygame.mouse.set_pos(playerRect.centerx,playerRect.centery)
			
			# Line 312 moves the mouse cursor to the same position as the player’s character. The pygame.mouse.set_pos() function moves the mouse cursor to the X- and Y-coordinates you pass it. This is so that the mouse cursor and player’s character are always in the same place.
			# Specifically, the cursor will be right in the middle of the character’s Rect object because you passed the centerx and centery attributes of playerRect for the coordinates. The mouse cursor still exists and can be moved, even though it is invisible because of the pygame.mouse.set_visible(False) call on line 105
			
			# Moving the baddies down
			for b in baddies:
				# Now loop through each baddie data structure in the baddies list to move them down a little.
				if not reverseCheat and not slowCheat:
					b['rect'].move_ip(0,b['speed'])
				# If neither of the cheats have been activated, then move the baddie’s location down a number of pixels equal to its speed, which is stored in the 'speed' key.
				
				# IMPLEMENTING THE CHEAT CODES
				elif reverseCheat:
					b['rect'].move_ip(0,-5)
				# If the reverse cheat is activated, then the baddie should move up by five pixels. Passing -5 for the second argument to move_ip() will move the Rect object upwards by five pixels.
				elif slowCheat:
					b['rect'].move_ip(0,1)
				# If the slow cheat has been activated, then the baddie should move downwards, but only by the slow speed of one pixel per iteration through the game loop. The baddie’s normal speed (which is stored in the 'speed' key of the baddie’s data structure) is ignored while the slow cheat is activated.
			# Removing the buddies i.e,Delete baddies that have fallen past the bottom.
			for b in baddies[:]:
				# Any baddies that fell below the bottom edge of the window should be removed from the baddies list. Remember that while iterating through a list, do not modify the contents of the list by adding or removing items. So instead of iterating through the baddies list with the for loop, iterate through a copy of the baddies list. This copy is made with the blank slicing operator [:].
				#The for loop on line 163 uses a variable b for the current item in the iteration through baddies[:].
				if b['rect'].top > WINDOWHEIGHT:
					baddies.remove(b)
					# Let’s evaluate the expression b['rect'].top. b is the current baddie data structure from the baddies[:] list. Each baddie data structure in the list is a dictionary with a 'rect' key, which stores a Rect object. So b['rect'] is the Rect object for the baddie.
					#Finally, the top attribute is the Y-coordinate of the top edge of the rectangular area. Remember that the Y-coordinates increase going down. So b['rect'].top > WINDOWHEIGHT will check if the top edge of the baddie is below the bottom of the window.
			
			##Drawing the Window
			#After all the data structures have been updated, the game world should be drawn using Pygame’s image functions. Because the game loop is executed several times a second, drawing the baddies and player in new positions makes their movement look smooth and natural.If this condition is True, then line 165 removes the baddie data structure from the baddies list.
			
			# Draw the game world on the window
			windowSurface.fill(BACKGROUNDCOLOR)
			
			# First, before drawing anything else, line 344 blacks out the entire screen to erase anything drawn on it previously.Remember that the Surface object in windowSurface is the special Surface object because it was the one returned by pygame.display.set_mode(). Therefore, anything drawn on that Surface object will appear on the screen after pygame.display.update() is called.
			
			#Drawing the Player’s Score
			# Draw the score and top score
			drawText('Score: %s' % (score),font,windowSurface,10,0)
			drawText('High Score: %s' % (topscore), font, windowSurface, 10,40)
			# Lines 350 and 351 render the text for the score and top score to the top left corner of the window. The 'Score: %s' % (score) expression uses string interpolation to insert the value in the score variable into the string.
			#Pass this string, the Font object stored in the font variable, the Surface object on which to draw the text on, and the X- and Y-coordinates of where the text should be placed. The drawText() will handle the call to the render() and blit() methods.
			#For the top score, do the same thing. Pass 40 for the Y-coordinate instead of 0 so that the top score text appears beneath the score text.
			
			# Drawing the Player's character
			# Draw the player's rectangle
			windowSurface.blit(playerImage,playerRect)
			
			# The information about the player is kept in two different variables. playerImage is a Surface object that contains all the colored pixels that make up the player’s character’s image. playerRect is a Rect object that stores the information about the size and location of the player’s character.
			#The blit() method draws the player character’s image (in playerImage) on windowSurface at the location in playerRect.
			
			# Draw each baddie
			for b in baddies:
				windowSurface.blit(b['surface'],b['rect'])
				# Line 365’s for loop draws every baddie on the windowSurface object. Each item in the baddies list is a dictionary. The dictionaries’ 'surface' and 'rect' keys contain the Surface object with the baddie image and the Rect object with the position and size information, respectively.
			pygame.display.update()
			# Now that everything has been drawn to windowSurface, draw this Surface object to the screen by calling pygame.display.update()
			
			# Collision Detection
			
			# check if any of the baddies have hit the player
			if playHasHitBaddie(playerRect,baddies):
				if score > topScore:
					topScore = score # set the new top score
				break
				# Lines 373 checks if the player has collided with any baddies by calling playerHasHitBaddie(). This function will return True if the player’s character has collided with any of the baddies in the baddies list. Otherwise, the function will return False.If the player’s character has hit a baddie, lines 374 and 375 update the top score if the current score is greater than it. Then the execution breaks out of the game loop at line 187. The program’s execution will move to line 383.	
			
			mainClock.tick(FPS)
			# To keep the computer from running through the game loop as fast as possible (which would be much too fast for the player to keep up with), call mainClock.tick() to pause for a brief amount of time. The pause will be long enough to ensure that about 40 (the value stored inside the FPS variable) iterations through the game loop occur each second.
			
		#The Game Over Screen
		# Stop the game and show the "Game Over" screen
		pygame.mixer.music.stop()
		gameOverSound.play()
		# When the player loses, the game stops playing the background music and plays the “game over” sound effect. Line 384 calls the stop() function in the pygame.mixer.music module to stop the background music. Line 385 calls the play() method on the Sound object stored in gameOverSound.
		drawText('GAME OVER..!!',font, windowSurface,(WINDOWWIDTH / 3),(WINDOWHEIGHT / 3))
		drawText('Press a key to play Again..',font,windowSurface,(WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
		pygame.display.update()
		waitForPlayerToPressKey()
		# Lines 387 and 390 call the drawText() function to draw the “game over” text to the windowSurface object. Line 197 calls pygame.display.update() to draw this Surface object to the screen. After displaying this text, the game stops until the player presses a key by calling the waitForPlayerToPressKey() function.
		gameOverSound.stop()
		# After the player presses a key, the program execution will return from the waitForPlayerToPressKey() call on line 390. Depending on how long the player takes to press a key, the “game over” sound effect may or may not still be playing. To stop this sound effect before a new game starts, line 392 calls gameOverSound.stop()