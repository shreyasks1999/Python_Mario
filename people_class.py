import config

class People():
	def __init__(self,ch=[]):
		self.type = 'Lmao'
		self.ch = ch
		self.x = 0
		self.y = 35
		self.distanceFromStart = 50
		self.in_air = 0
		self.jumping = 0
		#keep track how long Mario has been airborne
		self.frames_in_air = 1

	def move(self,inp,mat):  
		if(inp == 'a'):
			if(self.x > 1):
				if(mat[self.y][self.x - 1] == ' '):
					if(mat[self.y + 1][self.x - 1] == ' '):
						if(mat[self.y + 2][self.x - 1] == ' '):
							self.x -= 1
		if(inp == 'd'):
			if(mat[self.y][self.x + 4] == ' '):
				if(mat[self.y + 1][self.x + 4] == ' '):
					if(mat[self.y + 2][self.x + 4] == ' '):
						if(self.x < 45):
							self.x += 1
						else:
							self.distanceFromStart += 1

class Mario(People):
	def __init__(self):
		People.__init__(self,config._mario)
		self.score = 5
		self.alive = 1

	def gravity(self,mat):
		if(mat[self.y + 3][self.x] == ' '):
			if(mat[self.y + 3][self.x + 1] == ' '):
				if(mat[self.y + 3][self.x + 2] == ' '):
					if(mat[self.y + 3][self.x + 3] == ' '):
						self.y += 1
						return
		self.in_air = 0

	def jump(self,mat):
		if(mat[self.y-1][self.x] == ' '):
			if(mat[self.y-1][self.x + 1] == ' '):
				if(mat[self.y-1][self.x + 2] == ' '):
					if(mat[self.y-1][self.x + 3] == ' '):
						if(self.frames_in_air < 13):
							self.y -= 1
							self.frames_in_air += 1

						else:
							self.jumping = 0
							self.frames_in_air = 0

						return

		self.jumping = 0

class Enemy(People):
	def __init__(self):
		People.__init__(self,config._enemy)
		self.steps = 0
		self.moving_left = 0

	def oscillate(self):
		if(self.steps < 10):
			self.distanceFromStart -= 1
			self.steps += 1
		elif(self.steps < 20):
			self.ch = config._enemy2
			self.distanceFromStart += 1
			self.steps += 1
		else:
			self.steps = 0
			self.ch = config._enemy







