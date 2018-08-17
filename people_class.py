import config
class People():
	def __init__(self,ch=[]):
		self.type = 'Lmao'
		self.ch = ch
		self.x = 0
		self.y = 35



class Mario(People):
	def __init__(self):
		People.__init__(self,config._mario)
		self.distanceFromStart = 50
		self.score = 0
		self.life = 1
		self.in_air = 0
		#keep track how long Mario has been airborne
		self.frames_in_air = 1


	def move(self,inp,bd):
		x_cord = self.x + self.distanceFromStart - 50 #x cord with global frame 
		if(inp == 'a'):
			if(self.x > 1):
				if(bd[self.y][x_cord - 1] == ' '):
					if(bd[self.y + 1][x_cord - 1] == ' '):
						if(bd[self.y + 2][x_cord - 1] == ' '):
							if(bd[self.y + 4][x_cord - 1] == ' '):
								self.x -= 1
		if(inp == 'd'):
			if(self.x > 1):
				if(bd[self.y][x_cord + 4] == ' '):
					if(bd[self.y + 1][x_cord + 4] == ' '):
						if(bd[self.y + 2][x_cord + 4] == ' '):
							if(bd[self.y + 4][x_cord + 4] == ' '):
								self.x += 1

	def move_right(self):
		if(self.x < 45):
			self.x += 1
		else:
			self.distanceFromStart += 1

	def move_left(self):
		if(self.x > 1):
			self.x -= 1
		else:
			pass

	# def jump(self):
	# 	if(self.frames_in_air >= 14):
	# 		self.in_air = 0
	# 		self.frames_in_air = 0
	# 	# if(self.y < 0):
	# 	# 	self.in_air = 0
	# 	# 	self.frames_in_air = 0

	# 	if(self.frames_in_air < 7):
	# 		self.y -= 1
	# 		self.frames_in_air += 1

	# 	else:
	# 		self.y += 1
	# 		self.frames_in_air += 1