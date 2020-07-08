import numpy as np
from person_class import person_class
import pygame
import random
import sys
from pygame.locals import *
from config import *
from plot_config import *

import plot_model

pygame.init()
FPS = 20
fpsClock = pygame.time.Clock()

#######################################################################

# WINDOW 
WINDOWWIDTH = WINDOWWIDTH # size of window's width in pixels 
WINDOWHEIGHT = WINDOWHEIGHT # size of windows' height in pixels
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
SURF_COLOUR = pygame.Color(SURF_COLOUR)


myfont = pygame.font.SysFont('Arial', 30)

########################################################################

# INITIAL CONDITION OF POPULATION
S_pop, R_pop, I_pop = [], [], []
Total_Population = []
x_plot = 0
######################################################################

#Spawning Susceptible Population
for i in range(S):
	if i==0:
		x = np.random.randint(MARGIN_1,WINDOWWIDTH - MARGIN_1)
		y = np.random.randint(MARGIN_1, WINDOWHEIGHT_1 - MARGIN_1)
		person = person_class.person(x, y, 'S')
	else:
		collision = True
		while collision:
			x = np.random.randint(MARGIN_1,WINDOWWIDTH - MARGIN_1)
			y = np.random.randint(MARGIN_1,WINDOWHEIGHT_1 - MARGIN_1)
			person = person_class.person(x, y, 'S')
			for other_person in Total_Population:
				collision = person.check_collision_other(other_person)
				if collision == True:
					break

	Total_Population.append(person)



#Spawning Infected Population
for i in range(I):
	if i==0:
		x = np.random.randint(MARGIN_1, WINDOWWIDTH - MARGIN_1)
		y = np.random.randint(MARGIN_1, WINDOWHEIGHT_1 - MARGIN_1)
		person = person_class.person(x, y, 'I')
	else:
		collision = True
		while collision:
			x = np.random.randint(MARGIN_1, WINDOWWIDTH - MARGIN_1)
			y = np.random.randint(MARGIN_1, WINDOWHEIGHT_1 - MARGIN_1)
			person = person_class.person(x, y, 'I')
			for other_person in Total_Population:
				collision = person.check_collision_other(other_person)
				if collision == True:
					break

	Total_Population.append(person)

######################################################################

S_pop = [S]
I_pop = [I]
R_pop = [R]


######################################################################
#MAIN LOOP
while True: # Main Simulation Loop
	S_count = 0
	I_count = 0
	R_count = 0

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			#plot_model.make_plot(S_pop, I_pop, R_pop)
			sys.exit()
	###################################################
	#update 
	for person in Total_Population:
		person.update(DISPLAYSURF, Total_Population)
		if person.status == 'S':
			S_count += 1
		elif person.status == 'I':
			I_count += 1
		elif person.status == 'R':
			R_count += 1

	S_pop.append(S_count)
	I_pop.append(I_count)
	R_pop.append(R_count)
	###################################################
	#display simulation
	DISPLAYSURF.fill(SURF_COLOUR, (0, 0, WINDOWWIDTH, WINDOWHEIGHT_1))
	for person in Total_Population:
		person.display(DISPLAYSURF)
		person.display_quarentine(DISPLAYSURF)
	pygame.display.flip()

	###################################################
	#display plot
	TICK_WIDTH = plot_model.update_colour_plot(DISPLAYSURF, S_pop, I_pop, R_pop, x_plot)
	x_plot += TICK_WIDTH

	###################################################
	#display text
	box_height = 4*myfont.size( 'N: 100' )[1] + 5
	pygame.draw.rect(DISPLAYSURF, pygame.Color('black'), (WINDOWWIDTH - 85 , WINDOWHEIGHT_1 , 85, box_height ))
	pygame.draw.rect(DISPLAYSURF, pygame.Color('white'), (WINDOWWIDTH - 85 , WINDOWHEIGHT_1 , 85, box_height ), 2)

	text_height = box_height = myfont.size( 'N: 100' )[1]
	text_N = myfont.render(f'N: {S_count+I_count+R_count}', True, pygame.Color('white') , pygame.Color('black'))
	text_S = myfont.render(f'S: {S_count}', True, pygame.Color('white') , pygame.Color('black'))
	text_I = myfont.render(f'I: {I_count}', True, pygame.Color('white') , pygame.Color('black'))
	text_R = myfont.render(f'R: {R_count}', True, pygame.Color('white') , pygame.Color('black'))
	DISPLAYSURF.blit(text_N,(WINDOWWIDTH - 80 , WINDOWHEIGHT_1 + 2) )
	DISPLAYSURF.blit(text_S,(WINDOWWIDTH - 80 , WINDOWHEIGHT_1+ 2 + text_height))
	DISPLAYSURF.blit(text_I,(WINDOWWIDTH - 80 , WINDOWHEIGHT_1+ 2 + (2*text_height)))
	DISPLAYSURF.blit(text_R,(WINDOWWIDTH - 80 , WINDOWHEIGHT_1+ 2 + (3*text_height)))
	
	###################################################
	#fps
	pygame.display.update()
	fpsClock.tick(FPS)

######################################################################

