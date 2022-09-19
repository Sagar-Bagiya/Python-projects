import pygame

pygame.init()

# CREATING CANVAS
screen = pygame.display.set_mode((800, 500))
# TITLE OF CANVAS
pygame.display.set_caption("My Board")

MicImg = pygame.image.load('mic3.png') 
micSize = 10
micPosx = 200
micPosy=400
mod = False
K_LEFT = False
K_RIGHT = False
K_UP = False
K_DOWN = False

def micAnimation (micSize,micPosx,micPosy):
	newMicImg = pygame.transform.scale(MicImg,(micSize,micSize))
	screen.blit(newMicImg,(micPosx,micPosy))
	
def fillscreen():
	screen.fill((0,0,0))

exit = False
while not exit:

	fillscreen()
	
	if micSize>=100 or micSize<=0:
		mod = not mod
	if mod is True:
		micSize-=0.05
	else:
		micSize+=0.05
	
	if micPosx>=790 or micPosx<=0 :
		micPosx=0
	
	if micPosy>=500 or micPosy<=0 :
		micPosy=0

	if K_LEFT:
		micPosx-=.1
	if K_RIGHT:
		micPosx+=.1
	if K_UP:
		micPosy-=.1
	if K_DOWN:
		micPosy+=.1

	micAnimation(micSize,micPosx,micPosy)	

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit = True
	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				K_LEFT = True
				
			if event.key == pygame.K_RIGHT:
				K_RIGHT = True
		
			if event.key == pygame.K_UP:
				K_UP = True
		
			if event.key == pygame.K_DOWN:
				K_DOWN = True
		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				K_LEFT = False

			if event.key == pygame.K_RIGHT:
				K_RIGHT = False

			if event.key == pygame.K_UP:
				K_UP = False

			if event.key == pygame.K_DOWN:
				K_DOWN = False
		
	pygame.display.update()
