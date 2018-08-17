import config
from board_class import *
from people_class import *
from input import Get,input_to
import os
import time

M = Mario()
# # M.y = 35
# # M.x = 0
# # M.distanceFromStart = 50

bd = Board()


# frame = RenderFrame(bd.return_matrix(),M)

# print(frame.return_string())


getch = Get()

while True:
	inp = input_to(getch)
	os.system('clear')
	mat = bd.return_frame(M)
	# M.move(inp,bd.return_matrix())
	if(inp == 'a'):
		M.move_left()
	if(inp == 'd'):
		M.move_right()
	if(inp == 'w'):
		M.in_air = 1
	# if(M.in_air == 1):
	# 	M.jump()
	if(inp == 'q'):
		break
	# print(RenderFrame(bd.return_matrix(),M).return_string())

	print(return_string_from_frame(mat))

	time.sleep(0.015)
