# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

import random
from AI import AI
from Action import Action


class MyAI( AI ):

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		self.rowDimension = rowDimension
		self.colDimension = colDimension
		self.totalMines = totalMines
		self.currentX = startX
		self.currentY = startY
		# print("Dimension:",colDimension,rowDimension)
		# print("Total Mines:",totalMines)
		# print("Start:", self.currentX, self.currentY)
  
		self.w = [["-" for i in range(colDimension)] for j in range(rowDimension)]

		self.to_flaged = list()
		self.to_uncover = list()
		self.count = 0
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

		
	def getAction(self, number: int) -> "Action Object":
   
		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		# print(self.currentX,self.currentY)
		if number >= 0:
			self.w[self.currentY][self.currentX] = number

		# print the current world
		# self.print_world()

		if self.totalMines < 0:
			return Action(AI.Action.LEAVE)

		if len(self.to_flaged) != 0:
			pop = self.to_flaged.pop(0)
			self.w[pop[1]][pop[0]] = "?"
			self.currentX = pop[0]
			self.currentY = pop[1]
			self.totalMines -= 1
			return Action(AI.Action.FLAG, pop[0], pop[1])

		if number == 0:
			around_coordinates = self.get_around_coordinates(self.currentX, self.currentY)
			for i in range(len(around_coordinates)):
				if around_coordinates[i] not in self.to_uncover:
					self.to_uncover.append(around_coordinates[i])
		
		if len(self.to_uncover) > self.count:
			pair_to_uncover = self.to_uncover[self.count]
			self.count = self.count + 1
			self.currentX = pair_to_uncover[0]
			self.currentY = pair_to_uncover[1]
			return Action(AI.Action.UNCOVER,self.currentX,self.currentY)

		# store the unmarked_coords and flaged_coords for guessing
		unmarked_coords = []
		flaged_coords = []
		num = 0


		for y in range(len(self.w)):
			for x in range(len(self.w[y])):

				if self.w[y][x] in {1,2,3,4,5,6,7,8}:
					num = self.w[y][x]
					coords = self.get_around_coordinates(x,y)
					unmarked_coords = []
					flaged_coords = []

					# count the unmarked coordinates
					for i in range(len(coords)):
						if self.w[coords[i][1]][coords[i][0]] == "-":
							unmarked_coords.append(coords[i])
						if self.w[coords[i][1]][coords[i][0]] == "?":
							flaged_coords.append(coords[i])
					
					if num == len(flaged_coords):
						if len(unmarked_coords) >= 1:
							self.to_uncover += unmarked_coords[1:]
							self.currentX = unmarked_coords[0][0]
							self.currentY = unmarked_coords[0][1]
							return Action(AI.Action.UNCOVER,unmarked_coords[0][0],unmarked_coords[0][1])


					if len(unmarked_coords) == num - len(flaged_coords):
						if len(unmarked_coords) >= 1:
							self.to_flaged += unmarked_coords

							pop = self.to_flaged.pop(0)
							self.w[pop[1]][pop[0]] = "?"
							self.currentX = pop[0]
							self.currentY = pop[1]
							self.totalMines -= 1
							return Action(AI.Action.FLAG, pop[0], pop[1])

		# start guessing -------------------------

		# if len(unmarked_coords) > num - len(flaged_coords):
		# 	pop = unmarked_coords[random.randrange(len(unmarked_coords))]
		# 	self.currentX = pop[0]
		# 	self.currentY = pop[1]
		# 	return Action(AI.Action.FLAG, pop[0], pop[1])

		for y in range(len(self.w)):
			for x in range(len(self.w[y])):
				if self.w[y][x] in {1,2,3,4,5,6,7,8}:
					num = self.w[y][x]
					coords = self.get_around_coordinates(x,y)
					unmarked_coords = []
					flaged_coords = []

					# count the unmarked coordinates
					for i in range(len(coords)):
						if self.w[coords[i][1]][coords[i][0]] == "-":
							unmarked_coords.append(coords[i])
						if self.w[coords[i][1]][coords[i][0]] == "?":
							flaged_coords.append(coords[i])
					
					if len(unmarked_coords) > num - len(flaged_coords):
						pop = unmarked_coords[random.randrange(len(unmarked_coords))]
						self.currentX = pop[0]
						self.currentY = pop[1]
						return Action(AI.Action.UNCOVER, pop[0], pop[1])


		# self.print_world()

		return Action(AI.Action.LEAVE)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
	def get_around_coordinates(self,x,y):
		around_coordinates = []
		if x > 0:
			if y > 0:
				around_coordinates.append((x-1,y-1)) #if (x-1,y-1) not in around_coordinates else 0
				# print("add",x-1,y-1)

			around_coordinates.append((x-1,y)) #if (x-1,y) not in around_coordinates else 0
			# print("add",x-1,y)

			if y+1 < self.rowDimension:
				around_coordinates.append((x-1,y+1)) #if (x-1,y+1) not in around_coordinates else 0
				# print("add",x-1,y+1)

		if y > 0:
			around_coordinates.append((x,y-1)) #if (x,y-1) not in around_coordinates else 0
			# print("add",x,y-1)

		if y+1 < self.rowDimension:
			around_coordinates.append((x,y+1)) #if (x,y+1) not in around_coordinates else 0
			# print("add",x,y+1)
		
		if x+1 < self.colDimension:
			if y > 0:
				around_coordinates.append((x+1,y-1)) #if (x+1,y-1) not in around_coordinates else 0
				# print("add",x+1,y-1)

			around_coordinates.append((x+1,y)) #if (x+1,y) not in around_coordinates else 0
			# print("add",x+1,y)

			if y+1 < self.rowDimension:
				around_coordinates.append((x+1,y+1))# if (x+1,y+1) not in around_coordinates else 0
				# print("add",x+1,y+1)
		
		return around_coordinates

	def print_world(self):
		for y in range(len(self.w)):
			l = ""
			for x in range(len(self.w[y])):
				l = l + str(self.w[y][x]) + " "
			print(l)
