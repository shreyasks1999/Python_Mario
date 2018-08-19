import os
import time
from init import *

#the main game loop
while True:
	inp = input_to(getch)
	if(inp == 'q' or M.alive == 0):
		break
	os.system('clear')
	for i in config._list_of_enemies:
		if(M.distanceFromStart + 40 == i):
			E.distanceFromStart = i
			config._list_of_enemies.remove(i)
	E.oscillate()
	if(E.distanceFromStart == M.distanceFromStart + M.x - 50 + 3
	 and abs(E.y - M.y) < 4):
		M.alive = 0
	elif(E.distanceFromStart + 3 == M.distanceFromStart + M.x - 50 
		and abs(E.y - M.y) < 4):
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

	print(return_string_from_frame(mat))

	time.sleep(0.015)
	# time.sleep(0.2)


