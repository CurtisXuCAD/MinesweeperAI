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
		self.startX = startX
		self.startY = startY
  
		self.w = [[-5 for i in range(rowDimension)] for j in range(colDimension)]
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

		
	def getAction(self, number: int) -> "Action Object":
     
		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################


		if number == 0:
			self.w[self.startY][self.startX] = number
            for y in range(len(self.w)):
				l = ""
				for x in range(len(self.w[y])):
					l = l + str(self.w[y][x]) + " "
				print(l)
            print(startX,startY)
			# return
  
  
  
  

		return Action(AI.Action.LEAVE)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
