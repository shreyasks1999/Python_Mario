import random
import config
class Board:
	
	def __init__(self,listOfBricks,height = 42,width = 500):
		self.height = height
		self.width = width
		self.full_matrix = []
		self.listOfBRicks = listOfBricks

		for x in range(0, self.height):
		    self.full_matrix.append([])
		    for y in range(0, self.width):
		        self.full_matrix[x].append(' ')

		for y in range(self.height - 4, self.height):
			for x in range(0,width):
				self.full_matrix[y][x] = config._brick[x%2]

		for cord in self.listOfBRicks:
			rand_x = random.randint(5,14)
			rand_y = random.randint(2,3)
			for i in range(self.height - 11 - rand_y,self.height - 11):
				for j in range(cord,cord + rand_x):
					self.full_matrix[i][j] = '*'
		for k in range(25,500,105):
			for i in range(2,len(config._clouds) + 2):
				for j in range(len(config._clouds[0])):
					self.full_matrix[i][k+j] = config._clouds[i - 2][j]
		# for k in range(68,500,100):
		# 	for i in range(2,len(config._clouds) + 2):
		# 		for j in range(len(config._clouds[0])):
		# 			self.full_matrix[i][k+j] = config._clouds[i - 2][j]


	def return_frame(self,mario):
		xRef = mario.distanceFromStart
		mat = []
		for i in range(0,self.height):
			mat.append([])
			for j in range(xRef - 50,xRef + 50):
				mat[i].append(self.full_matrix[i][j])

		for i in range(mario.y,mario.y + 3):
			for j in range(mario.x,mario.x + 4):
				mat[i][j] = mario.ch[i - mario.y][j - mario.x]

		return mat

def return_string_from_frame(mat):
	stringBd = ''
	for y in range(0,len(mat)):
		for x in range(0,len(mat[0])):
			stringBd += mat[y][x]
		stringBd += '\n'

	stringBd += "Press q to quit \n:"
	return stringBd




