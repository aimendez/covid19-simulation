import matplotlib.pyplot as plt
from plot_config import *
from config import *
import pygame

def make_plot(S_pop, I_pop, R_pop):
	fig,ax = plt.subplots()
	x_axis = range(len(S_pop))
	ax.plot(x_axis, S_pop)
	ax.plot(x_axis, I_pop)
	ax.plot(x_axis, R_pop)
	plt.show()


def update_line_plot(DISPLAYSURF, S_pop, I_pop, R_pop, x_plot):
	MARKER_WIDTH = 1
	MARKER_HEIGHT = 1

	S_COLOUR = pygame.Color('white')
	y_plot_S = WINDOWHEIGHT - ( MARGIN_2	+ (S_pop[-1] * (WINDOWHEIGHT_2 - 2*MARGIN_2) )/S_pop[0]  )
	pygame.draw.rect(DISPLAYSURF, S_COLOUR, (x_plot, y_plot_S , MARKER_WIDTH,  MARKER_HEIGHT )) 

	R_COLOUR = pygame.Color('green')
	y_plot_R = WINDOWHEIGHT - ( MARGIN_2	+ (R_pop[-1] * (WINDOWHEIGHT_2 - 2*MARGIN_2) )/S_pop[0] )
	pygame.draw.rect(DISPLAYSURF, R_COLOUR, (x_plot, y_plot_R , MARKER_WIDTH,  MARKER_HEIGHT )) 

	I_COLOUR = pygame.Color('red')
	y_plot_I =WINDOWHEIGHT - ( MARGIN_2	+ (I_pop[-1] * (WINDOWHEIGHT_2 - 2*MARGIN_2) )/S_pop[0] )
	pygame.draw.rect(DISPLAYSURF, I_COLOUR, (x_plot, y_plot_I , MARKER_WIDTH,  MARKER_HEIGHT )) 

	return MARKER_WIDTH


def update_colour_plot(DISPLAYSURF, S_pop, I_pop, R_pop, x_plot):
	TICK_WIDTH = 2

	S_COLOUR = pygame.Color('white')
	MARKER_HEIGHT =  WINDOWHEIGHT_2
	y_plot_S = WINDOWHEIGHT_1 
	pygame.draw.rect(DISPLAYSURF, S_COLOUR, (x_plot, y_plot_S , TICK_WIDTH,  MARKER_HEIGHT ))

	R_COLOUR = pygame.Color('green')
	MARKER_HEIGHT =  (R_pop[-1] * (WINDOWHEIGHT_2) )/N
	y_plot_R = WINDOWHEIGHT_1 
	pygame.draw.rect(DISPLAYSURF, R_COLOUR, (x_plot, y_plot_R , TICK_WIDTH,  MARKER_HEIGHT )) 

	I_COLOUR = pygame.Color('red')
	y_plot_I = WINDOWHEIGHT - ((I_pop[-1] * (WINDOWHEIGHT_2) )/N )
	MARKER_HEIGHT = (I_pop[-1] * (WINDOWHEIGHT_2 ) )/S_pop[0] + 1
	pygame.draw.rect(DISPLAYSURF, I_COLOUR, (x_plot, y_plot_I , TICK_WIDTH,  MARKER_HEIGHT )) 

	return TICK_WIDTH