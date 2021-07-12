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
		print("Dimension:",colDimension,rowDimension)
		print("Total Mines:",totalMines)
		print("Start:", self.currentX, self.currentY)
  
		self.w = [["-" for i in range(rowDimension)] for j in range(colDimension)]

		self.to_uncover = list()
		self.count = 0
		# self.visited = set()
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

		
	def getAction(self, number: int) -> "Action Object":
     
		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		print(self.currentX,self.currentY)
		self.w[self.currentY][self.currentX] = number

		if number == 0:
			# self.currentX = self.currentX-1 if self.currentX -1 > 0 else self.currentX
			# self.currentY = self.currentY-1 if self.currentY -1 > 0 else self.currentY
			if self.currentX > 0:
				if self.currentY > 0:
					self.to_uncover.append((self.currentX-1,self.currentY-1)) if (self.currentX-1,self.currentY-1) not in self.to_uncover else 0
					print("add",self.currentX-1,self.currentY-1)

				self.to_uncover.append((self.currentX-1,self.currentY)) if (self.currentX-1,self.currentY) not in self.to_uncover else 0
				print("add",self.currentX-1,self.currentY)

				if self.currentY+1 < self.rowDimension:
					self.to_uncover.append((self.currentX-1,self.currentY+1)) if (self.currentX-1,self.currentY+1) not in self.to_uncover else 0
					print("add",self.currentX-1,self.currentY+1)

			if self.currentY > 0:
				self.to_uncover.append((self.currentX,self.currentY-1)) if (self.currentX,self.currentY-1) not in self.to_uncover else 0
				print("add",self.currentX,self.currentY-1)

			if self.currentY+1 < self.rowDimension:
				self.to_uncover.append((self.currentX,self.currentY+1)) if (self.currentX,self.currentY+1) not in self.to_uncover else 0
				print("add",self.currentX,self.currentY+1)
			
			if self.currentX+1 < self.colDimension:
				if self.currentY > 0:
					self.to_uncover.append((self.currentX+1,self.currentY-1)) if (self.currentX+1,self.currentY-1) not in self.to_uncover else 0
					print("add",self.currentX+1,self.currentY-1)

				self.to_uncover.append((self.currentX+1,self.currentY)) if (self.currentX+1,self.currentY) not in self.to_uncover else 0
				print("add",self.currentX+1,self.currentY)

				if self.currentY+1 < self.rowDimension:
					self.to_uncover.append((self.currentX+1,self.currentY+1)) if (self.currentX+1,self.currentY+1) not in self.to_uncover else 0
					print("add",self.currentX+1,self.currentY+1)
		
		if len(self.to_uncover) > self.count:
			pair_to_uncover = self.to_uncover[self.count]
			self.count = self.count + 1
			# self.visited.append(pair_to_uncover)
			self.currentX = pair_to_uncover[0]
			self.currentY = pair_to_uncover[1]
			return Action(AI.Action.UNCOVER,self.currentX,self.currentY)
			# self.to_uncover.append(())


			# return Action(AI.Action.UNCOVER, self.currentX, self.currentY)
			# self.w[self.startY-1][self.startX-1] = number
		for y in range(len(self.w)):
			l = ""
			for x in range(len(self.w[y])):
				l = l + str(self.w[y][x]) + " "
			print(l)
		# print(self.currentX,self.currentY)
		# if number == 1:
		# 	print("do something!")
		# else:
		# 	print(number,"do somthing!")
		return Action(AI.Action.LEAVE)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
