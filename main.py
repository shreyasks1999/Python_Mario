import os
import time
from input import input_to
from init import *

#the main game loop
while True:
	inp = input_to(getch)
	if(inp == 'q'):
		break
	os.system('clear')
	mat = bd.return_frame(M)
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
