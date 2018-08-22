from os import system
import time
import sys
from init import *

#the main game loop
while True:
	inp = input_to(getch)
	if(inp == 'q' or M.alive == 0):
		break
	# os.system('clear')
	sys.stdout.flush()
	try:
		system('clear')
	except: BaseException:
		system('cls')

	for i in config._list_of_enemies:
		if(M.distanceFromStart + 40 == i):
			E.alive = 1
			E.steps = 0
			E.ch = config._enemy 
			E.distanceFromStart = i
			config._list_of_enemies.remove(i)
	
	if(E.alive == 1):
		E.oscillate()
	if(abs(E.distanceFromStart - (M.distanceFromStart + M.x - 50)) < 5):
		if(M.y + 4 == E.y and not(M.jumping)):
			M.score += 1
			E.ch = config._enemy_empty
			E.alive = 0

		elif(abs(M.y - E.y) < 3 and E.alive == 1):
			M.alive = 0

	mat = bd.return_frame(M,E)
	M.move(inp,mat)
	if(inp == 'w'):
		if(M.in_air == 0):
			M.jumping = 1
			M.in_air = 1
	if(M.jumping == 1):
		M.jump(mat)
	else:
		M.gravity(mat)

	print(return_string_from_frame(mat)+str(M.distanceFromStart)+'\n')

	time.sleep(0.009)
	# time.sleep(0.2)


