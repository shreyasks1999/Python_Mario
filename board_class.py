class Board:
	# def __init__(self,listOfBRicks):
	def __init__(self,height = 42,width = 500):
		self.height = height
		self.width = width
		self.matrix = []
		self.listOfBRicks = [10,40]#later take as input in init
								# for seperate levels

		# self.listOfBRicks = listOfBRicks
		for x in range(0, self.height):
		    self.matrix.append([])
		    for y in range(0, self.width):
		        self.matrix[x].append(' ')

		for y in range(self.height - 4, self.height):
			for x in range(0,width):
				self.matrix[y][x] = '#'

		for cord in self.listOfBRicks:
			for i in range(self.height - 14,self.height - 11):
				for j in range(cord,cord + 5):
					self.matrix[i][j] = '#'

	def return_matrix(self):
		for cord in self.listOfBRicks:
			for i in range(self.height - 14,self.height - 11):
				for j in range(cord,cord + 5):
					self.matrix[i][j] = '#'

		return self.matrix

	def return_frame(self,mario):
		xRef = mario.distanceFromStart
		mat = []
		for i in range(0,self.height):
			mat.append([])
			for j in range(xRef - 50,xRef + 50):
				mat[i].append(self.matrix[i][j])

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

# class RenderFrame:

# 	def __init__(self,mat,mario):
# 		self.height = 42
# 		self.mat = []
# 		for x in range(0, self.height):
# 		    self.mat.append([])
# 		    for y in range(0, 500):
# 		        self.mat[x].append(' ')

# 		for x in range(0, self.height):
# 		    for y in range(0, 500):
# 		        self.mat[x][y] = mat[x][y]



# 		self.mario = mario 
# 		self.xRef = self.mario.distanceFromStart#xRef is pointer of frame within board
# 		for i in range(self.mario.y,self.mario.y+3):
# 			for j in range(self.mario.x + self.mario.distanceFromStart - 50 , self.mario.x + self.mario.distanceFromStart - 46):
# 				self.mat[i][j] = self.mario.ch[i - self.mario.y][j - self.mario.x - self.mario.distanceFromStart + 50]


# 	def return_string(self):
# 		self.stringBd = ''
# 		for y in range(0,self.height):
# 			for x in range(self.xRef - 50,self.xRef + 50):
# 				self.stringBd += self.mat[y][x]
# 			self.stringBd += '\n'

# 		self.stringBd += "Press q to quit \n:"
# 		self.stringBd += "Quitting is for wimps"
# 		return self.stringBd 




