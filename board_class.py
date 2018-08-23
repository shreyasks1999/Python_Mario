import random
from colorama import Back
import config

#main board class
class Board:
	
	def __init__(self,height = 42,width = 500):
		self.height = height
		self.width = width
		self.full_matrix = []

		#make empty map
		for x in range(0, self.height):
		    self.full_matrix.append([])
		    for y in range(0, self.width):
		        self.full_matrix[x].append(' ')

		#making the ground
		for y in range(self.height - 4, self.height):
			for x in range(0,self.width):
				self.full_matrix[y][x] = config._brick[x%2]

		#making clouds
		for k in range(25,self.width - 60,110):
			for i in range(3,len(config._clouds) + 3):
				for j in range(len(config._clouds[0])):
					self.full_matrix[i][k+j] = config._clouds[i - 3][j]




	def board_level(self):

		#making platforms
		for cord in config._list_of_bricks:
			p = random.randint(0,3)
			rand_x = config._list_of_brickLengths[p]			
			for i in range(self.height - 11 - 2,self.height - 11):
				for j in range(cord,cord + rand_x):
					self.full_matrix[i][j] = config._brick[(j - cord)%2]


		#making pipes
		for i in config._list_of_enemies:
			for y in range(len(config._pipe)):
				for x in range(len(config._pipe[0])):
					self.full_matrix[y + self.height - 4 - len(config._pipe)][x + i - 27] = config._pipe[y][x]
					self.full_matrix[y + self.height - 4 - len(config._pipe)][x + i + 4] = config._pipe[y][x]


	# def board_boss(self):
		








	#return a matrix of size 42 * 100, with mario.distanceFromStart as mid pointer
	def return_frame(self,mario,enem):
		xRef = mario.distanceFromStart
		mat = []
		if(enem is not None):
			for y in range(len(enem.ch)):
				for x in range(len(enem.ch[0])):
					self.full_matrix[enem.y + y][(enem.distanceFromStart + x)%self.width] = enem.ch[y][x]

		for i in range(self.height):
			mat.append([])
			for j in range(xRef - 50,xRef + 50):
				mat[i].append(self.full_matrix[i][j%self.width])

		for i in range(mario.y,mario.y + 3):
			for j in range(mario.x,mario.x + 4):
				mat[i][j] = mario.ch[i - mario.y][j - mario.x]

		if(enem is not None):
			for y in range(len(enem.ch)):
				for x in range(len(enem.ch[0])):
					self.full_matrix[enem.y + y][(enem.distanceFromStart + x)%self.width] = ' '
		return mat

#function to make a string given a matrix
def return_string_from_frame(mat):
	stringBd = ''
	for y in range(0,len(mat)):
		for x in range(0,len(mat[0])):
			stringBd += mat[y][x]
		stringBd += '\n'

	stringBd += "Press q to quit \n\n"
	stringBd += "Quitting is for losers you wimp\n\n"

	return stringBd



