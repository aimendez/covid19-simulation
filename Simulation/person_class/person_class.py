import numpy as np
import math
import random
import pygame
from config import *
from plot_config import *

class person:
	#global variables
	vmin , vmax = -5, 5
	r = 10
	white = pygame.Color('white')
	red = pygame.Color('red')
	green = pygame.Color('green')
 	
	transmission_rate = TRANS_RATE
	recovery_rate = random.randint(RECOV_RATE[0],RECOV_RATE[1])
	quarentine_rate = QUARENTINE_RATE
	quarentine_radius = QUARETNTINE_RADIUS

	def __init__(self, x, y, status):
		
		# Position
		self.x = x
		self.y = y

		#recovery day tracking
		self.recovery_count = 0

		# Random velocity
		self.vx, self.vy = np.random.randint(self.vmin, self.vmax),np.random.randint(self.vmin, self.vmax)

		# Status (S/I/R)
		self.status = status

		# quarentine flag
		self.quarentine = False

##################################################################
	def move(self):
		'''updates position of the object'''
		self.x += self.vx
		self.y += self.vy

	def check_wall_collision(self, surface):
		'''Check if object is in boundary of the surface. If not, change direction of velocity'''
		WINDOWWIDTH = surface.get_width() 
		WINDOWHEIGHT = WINDOWHEIGHT_1  
		MARGIN = MARGIN_1

		if (self.x + self.r) >= WINDOWWIDTH-MARGIN and self.vx>0:
			self.vx = -self.vx
		elif (self.x - self.r) <= 0+MARGIN and self.vx < 0:
			self.vx = -self.vx

		if (self.y + self.r) >= WINDOWHEIGHT - MARGIN and self.vy >0:
			self.vy = -self.vy
		elif (self.y - self.r) <= 0 + MARGIN and self.vy < 0:
			self.vy = -self.vy

##################################################################

	def check_recovery(self):
		if self.status == 'I':
			if self.recovery_count >= self.recovery_rate:
				self.status = 'R'
				if self.quarentine == True:
					self.quarentine = False
					self.vx, self.vy = np.random.randint(self.vmin, self.vmax),np.random.randint(self.vmin, self.vmax)

##################################################################

	def get_distance(self, person):
		'''get distance between current object and another one'''
		distance = math.sqrt( (self.x - person.x)**2 + (self.y - person.y)**2 )
		return distance

	def check_collision_other(self, person):
		'''Check if object collides with another '''
		collision = False
		distance = self.get_distance(person)
		if person.quarentine == False:
			if distance <= (self.r + person.r):
				collision = True
		elif person.quarentine == True:
			if distance <= (self.r + person.quarentine_radius):
				collision = True
		return collision

	def velocity_after_collision(self, person):
		if self.quarentine==False and person.quarentine==False: #if two persons are moving
			temp_vx, temp_vy = self.vx, self.vy
			self.vx, self.vy = person.vx, person.vy
			person.vx, person.vy = temp_vx, temp_vy

		if person.quarentine: #if the other is not moving for quarentine
			magV = math.sqrt( self.vx**2 + self.vy**2)
			tempV = np.array( [self.vx+(self.x - person.x), self.vy+(self.y - person.y)] )
			mag_tempV = math.sqrt(np.dot(tempV,tempV))
			norm_tempV = tempV/mag_tempV

			self.vx = int(norm_tempV[0]*magV)
			self.vy =  int(norm_tempV[1]*magV)


	def spread_virus(self, person):
		if self.status == 'S' and person.status == 'I':
			if person.quarentine == False: #transmit the virus only if is not in quarentine
				if random.uniform(0,1) <= self.transmission_rate:
					self.status = 'I'

		elif self.status == 'I' and person.status == 'S':
			if self.quarentine == False:
				if random.uniform(0,1) <= self.transmission_rate:
					person.status = 'I'

##################################################################

	def check_quarentine(self, surface):
		chance = random.uniform(0,1)
		if chance > self.quarentine_rate: #only a certain pct of people would go into quarentine
			self.vx, self.vy = 0, 0
			self.quarentine = True

##################################################################

	def update(self, surface, population):
			self.move()
			self.check_recovery()
			if self.status == 'I':
				self.recovery_count += 1
				#if self.recovery_count%5 == 0:
				#	self.check_quarentine(surface)  

			self.check_wall_collision(surface)
			for person in population:
				if self != person:
					collision = self.check_collision_other(person)
					if collision:
						self.velocity_after_collision(person)
						self.spread_virus(person)
		
##################################################################

	def display(self, surface):
		''' draw the circle in position x,y'''
		self.colour = self.white if self.status == 'S' else self.red if self.status == 'I' else self.green
		pygame.draw.circle(surface, self.colour, (self.x, self.y), self.r)

##################################################################
	def display_quarentine(self, surface):
		''' draw the quarentine boundary '''
		self.colour = self.white
		if self.quarentine == True:
			pygame.draw.circle(surface, self.colour, (self.x, self.y), self.quarentine_radius, 2)