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
		self.alive = 1
		#keep track how long Mario has been airborne
		self.frames_in_air = 1

	def move(self,inp,mat):  
		if(inp == 'a'):
			if(self.x > 1):
				if(mat[self.y][self.x - 1] == ' '):
					if(mat[self.y + 1][self.x - 1] == ' '):
						if(mat[self.y + 2][self.x - 1] == ' '):
							self.x -= 1
							return 1
		if(inp == 'd'):
			if(mat[self.y][self.x + 4] == ' '):
				if(mat[self.y + 1][self.x + 4] == ' '):
					if(mat[self.y + 2][self.x + 4] == ' '):
						if(self.x < 45):
							self.x += 1
						else:
							self.distanceFromStart += 1
							return 1

		return 0



class Mario(People):
	def __init__(self):
		People.__init__(self,config._mario)
		self.score = 0
		self.life = 3

	#checks for 4 cells beneath mario character
	def gravity(self,mat):
		if(mat[self.y + 3][self.x] == ' '):
			if(mat[self.y + 3][self.x + 1] == ' '):
				if(mat[self.y + 3][self.x + 2] == ' '):
					if(mat[self.y + 3][self.x + 3] == ' '):
						self.y += 1
						return
		self.in_air = 0

	#jumps to height 13
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
		#if it colided with a block
		self.jumping = 0

class Enemy(People):
	def __init__(self):
		People.__init__(self,config._enemy)
		self.steps = 0
		self.moving_left = 0

	#make an enemy at i
	def init_enemy(self,i):
		self.alive = 1
		self.steps = 0
		self.distanceFromStart = i
		config._list_of_enemies.remove(i)

	#left and right motion
	def oscillate(self):
		if(self.steps < 20):
			self.distanceFromStart -= 1
			self.steps += 1
		elif(self.steps < 40):
			self.ch = config._enemy2
			self.distanceFromStart += 1
			self.steps += 1
		else:
			self.steps = 0
			self.ch = config._enemy

#smart enemy
class BossEnemy(People):
	def __init__(self):
		People.__init__(self,config._boss_enemy)
		self.steps = 0
		self.distanceFromStart = 130
		self.moving_left = 1
		self.y = 42 - 4 - len(self.ch)
		self.life = 5

	#detects mario and moves towards him 
	def move(self,M):
		if(self.distanceFromStart <= M.distanceFromStart + M.x - 50 - len(self.ch[0]) - 11 and (self.moving_left)):
			self.moving_left = 0
		if(self.distanceFromStart >= M.distanceFromStart + M.x - 50 + 15 and not(self.moving_left)):
			self.moving_left = 1

		if(self.moving_left):
			self.distanceFromStart -= 1
		else:
			self.distanceFromStart += 1




