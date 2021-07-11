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

class position:
	def __init__(self, posiX, posiY, rowDim, colDim):
		self.px = posiX
		self.py = posiY
		self.dx = rowDim
		self.dy = colDim

		#Default position: normal
		self.position = 1
		#Position at cornor: mark it as -1
		if (self.px == 0 and self.py == 0) or (self.px == 0 and self.py == self.dy) or (self.px == self.dx and self.py == 0) or (self.px == self.dx and self.py == self.dy):
			self.position = -1
		#Position on side but not corner: mark it as 0
		if self.px == 0 or self.px == self.dx:
			if self.py != 0 and self.py != self.dy:
				self.position = 0
		if self.py == 0 or self.py == self.dx:
			if self.px != 0 and self.px != self.dx:
				self.position = 0



class MyAI( AI ):

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		

		#Basic Implementation
		self.rows = rowDimension - 1
		self.cols = colDimension - 1
		self.num_mine = totalMines
		self.startX = startX
		self.startY = startY
		self.position = 1

		#Marking all positions based on corner, side, or normal
		for r in range(self.rows):
			for c in range(self.cols):
				position(r, c, colDimension, rowDimension)
		

		#Psuedo Code
		'''
		&   0   1   2   3   4

		0   X				X

		1   

		2	

		3

		4	X				X
		
		
		
		
		
		at (StartX, StartY), uncover the position
		if num_mine_adjacent (after uncovering) == 0:
			start loop the world at (0, 0) by recursively check each square
		else:
			if self.position == -1: (at corner)
				if (StartX, StartY) == (0,0):
					#mine must be at (0, 1), (1, 0), (1, 1)
					Uncover (0, 2), (1, 2), (2, 2), (2, 1), (2, 0)
					at (2, 2), if num_mine_adjacent == 0:
						Uncover (1, 2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (1,0)
						else:
							SOLVE: MINE AT (0,1)
					else:
						SOLVE: Mine AT (1,1)
				
				elif (StartX, StartY) == (0,self.cols):
					#mine must be at (0, self.cols-1), (1, self.cols-1), (1, self.cols)
					Uncover (0, self.cols-2), (1, self.cols-2), (2, self.cols-2), (2, self.cols-1), (2, self.cols)
					at (2, self.cols-2), if num_mine_adjacent == 0:
						Uncover (1, self.cols-2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (1, self.cols)
						else:
							SOLVE: MINE AT (0, self.cols-1)
					else:
						SOLVE: Mine AT (1, self.cols-1)
				
				elif (StartX, StartY) == (self.rows, 0):
					#mine must be at (self.rows-1, 0), (self.rows-1, 1), (self.rows, 1)
					Uncover (self.rows-2, 0), (self.rows-2, 1), (self.rows-2, 2), (self.rows-1, 2), (self.rows, 2)
					at (self.rows-2, 2), if num_mine_adjacent == 0:
						Uncover (self.rows-2, 1), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, 1)
						else:
							SOLVE: MINE AT (self.rows-1, 0)
					else:
						SOLVE: Mine AT (self.rows-1, 1)
				
				else: #(StartX, StartY) == (self.rows, self.cols):
					#mine must be at (self.rows-1, self.cols), (self.rows-1, self.cols-1), (self.rows, self.cols-1)
					Uncover (self.rows-2, self.cols), (self.rows-2, self.cols-1), (self.rows-2, self.cols-2), (self.rows-1, self.cols-2), (self.rows, self.cols-2)
					at (self.rows-2, self.cols-2), if num_mine_adjacent == 0:
						Uncover (self.rows-2, self.cols-1), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows-1, self.cols)
						else:
							SOLVE: MINE AT (self.rows, self.cols-1)
					else:
						SOLVE: Mine AT (self.rows-1, self.cols-1)
			elif self.position == -1: (on side)
			

		&   0   1   2   3   4

		0   ?   X	?   C

		1   ?	?  	?   C

		2	C   C   C   C

		3

		4
			
			
				if (StartX, StartY) == (0, 1):
					#Mine must be at ?, and check C correspondingly
					Uncover (2,0), (2,1), (2,2), (2,3), (1,3), (0,3)
					at (2,0), if num_mine_adjacent == 0:
						at (0,3), if num_mine_adjacent == 0:
							SOLVE: MINE AT (0, 0)
						else:
							at (2, 3), if num_mine_adjacent == 0:
								SOLVE: MINE AT (0, 2)
							else:
								SOLVE: MINE AT (1, 2)
					else:
						at (2,2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (1, 0)
						else:
							SOLVE: MINE AT (1, 1)
		
		&   0   1   2   3   4

		0       C   ?   X	?

		1   	C	?	?	?

		2		C	C	C	C

		3

		4
			
			
				if (StartX, StartY) == (0, self.cols-1):
					#Mine must be at ?, and check C correspondingly
					Uncover (2,self.cols), (2,self.cols-1), (2,self.cols-2), (2,self.cols-3), (1,self.cols-3), (0,self.cols-3)
					at (2,self.cols), if num_mine_adjacent == 0:
						at (0,self.cols-3), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, self.cols)
						else:
							at (2,self.cols-3), if num_mine_adjacent == 0:
								SOLVE: MINE AT (0, self.cols-2)
							else:
								SOLVE: MINE AT (1, self.cols-2)
					else:
						at (2,self.cols-2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (1, self.cols)
						else:
							SOLVE: MINE AT (1, self.cols-1)
		
		&   0   1   2   3   4

		0 

		1 

		2	C	C	C	C

		3	?	?	?	C

		4	?	X	?	C
			
			
				if (StartX, StartY) == (self.rows, 1):
					#Mine must be at ?, and check C correspondingly
					Uncover (self.rows-2, 0), (self.rows-2, 1), (self.rows-2, 2), (self.rows-2, 3), (self.rows-1, 3), (self.rows, 3)
					at (self.rows-2, 0), if num_mine_adjacent == 0:
						at (self.rows, 3), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, 0)
						else:
							at (self.rows-2,3), if num_mine_adjacent == 0:
								SOLVE: MINE AT (self.rows, 2)
							else:
								SOLVE: MINE AT (self.rows-1, 2)
					else:
						at (self.rows-2,2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows-1, 0)
						else:
							SOLVE: MINE AT (self.rows-1, 1)
		
		&   0   1   2   3   4

		0 

		1 

		2		C	C	C	C

		3		C	?	?	?

		4		C	?	X	?
			
			
				if (StartX, StartY) == (self.rows, self.cols-1):
					#Mine must be at ?, and check C correspondingly
					Uncover (self.rows-2, self.cols), (self.rows-2, self.cols-1), (self.rows-2, self.cols-2), (self.rows-2, self.cols-3), (self.rows-1, self.cols-3), (self.rows, self.cols-3)
					at (self.rows-2, self.cols), if num_mine_adjacent == 0:
						at (self.rows, self.cols-3), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, self.cols)
						else:
							at (self.rows-2,self.cols-3), if num_mine_adjacent == 0:
								SOLVE: MINE AT (self.rows, self.cols-2)
							else:
								SOLVE: MINE AT (self.rows-1, self.cols-2)
					else:
						at (self.rows-2,self.cols-2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows-1, self.cols)
						else:
							SOLVE: MINE AT (self.rows-1, self.cols-1)
		
		&   0   1   2   3   4

		0 	?	?	C

		1 	X	?	C

		2	?	?	C

		3	C	C	C

		4	
			
			
				if (StartX, StartY) == (1, 0):
					#Mine must be at ?, and check C correspondingly
					Uncover (3,0), (3,1), (3,2), (2,3), (1,3), (0,3)
					at (0,2), if num_mine_adjacent == 0:
						at (3,0), if num_mine_adjacent == 0:
						SOLVE: MINE AT (0, 0)
						else:
							at (3, 2), if num_mine_adjacent == 0:
								SOLVE: MINE AT (2, 0)
							else:
								SOLVE: MINE AT (2, 1)
					else:
						at (2,2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (0, 1)
						else:
							SOLVE: MINE AT (1, 1)
		
		&   0   1   2   3   4

		0          	C   ?	?

		1   		C	?	X

		2			C	?	?

		3			C	C	C

		4
			
			
				if (StartX, StartY) == (1, self.cols):
					#Mine must be at ?, and check C correspondingly
					Uncover (3,self.cols), (3,self.cols-1), (3,self.cols-2), (2,self.cols-2), (1,self.cols-2), (0,self.cols-2)
					at (0,self.cols-2), if num_mine_adjacent == 0:
						at (3,self.cols), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, self.cols)
						else:
							at (3,self.cols-2), if num_mine_adjacent == 0:
								SOLVE: MINE AT (2, self.cols)
							else:
								SOLVE: MINE AT (2, self.cols-1)
					else:
						at (2,self.cols-2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (0, self.cols-1)
						else:
							SOLVE: MINE AT (1, self.cols-1)
		
		&   0   1   2   3   4

		0 

		1 	C	C	C

		2	?	?	C	

		3	X	?	C	

		4	?	?	C	
			
			
				if (StartX, StartY) == (self.rows-1, 0):
					#Mine must be at ?, and check C correspondingly
					Uncover (self.rows-3, 0), (self.rows-3, 1), (self.rows-3, 2), (self.rows-2, 2), (self.rows-2, 1), (self.rows-2, 0)
					at (self.rows, 2), if num_mine_adjacent == 0:
						at (self.rows-3, 0), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, 0)
						else:
							at (self.rows-3,2), if num_mine_adjacent == 0:
								SOLVE: MINE AT (self.rows-2, 0)
							else:
								SOLVE: MINE AT (self.rows-2, 1)
					else:
						at (self.rows-2,2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, 1)
						else:
							SOLVE: MINE AT (self.rows-1, 1)
		
		&   0   1   2   3   4

		0 

		1 			C	C	C

		2			C	?	?

		3			C	?	X

		4			C	?	?
			
			
				if (StartX, StartY) == (self.rows-1, self.cols):
					#Mine must be at ?, and check C correspondingly
					Uncover (self.rows-3, self.cols), (self.rows-3, self.cols-1), (self.rows-3, self.cols-2), (self.rows-2, self.cols-2), (self.rows-1, self.cols-2), (self.rows, self.cols-2)
					at (self.rows, self.cols-2), if num_mine_adjacent == 0:
						at (self.rows-3, self.cols), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, self.cols)
						else:
							at (self.rows-3,self.cols-2), if num_mine_adjacent == 0:
								SOLVE: MINE AT (self.rows-2, self.cols)
							else:
								SOLVE: MINE AT (self.rows-2, self.cols-1)
					else:
						at (self.rows-2,self.cols-2), if num_mine_adjacent == 0:
							SOLVE: MINE AT (self.rows, self.cols-1)
						else:
							SOLVE: MINE AT (self.rows-1, self.cols-1)
		
		&   0   1   2   3   4

		0 	C	?	X	?	C

		1  		?	?	?	

		2	C	C	C	C	C

		3

		4
			
				
			
						







				



					


	
	
		'''



		
		



		






		pass
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

		
	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		return Action(AI.Action.LEAVE)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
