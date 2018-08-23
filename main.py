from os import system
import time
import sys
from init import *

# the main game loop
while True:
	inp = input_to(getch)
	if(M.distanceFromStart > bd.width - 80):
		level = 1
		break

	if(inp is 'q' or M.alive is 0):
		print("Game Over")
		break

	sys.stdout.flush()
	system('clear')
	
	for i in config._list_of_enemies:
		if(M.distanceFromStart + 50 == i):
			E.init_enemy(i)
	
	if(E.alive == 1):
		E.oscillate()
	if(abs(E.distanceFromStart - (M.distanceFromStart + M.x - 50)) < 5):
		if(M.y + 3 is E.y and not(M.jumping) and E.alive is 1):
			M.score += 1
			E.ch = config._enemy_empty
			E.alive = 0

		elif(abs(M.y - E.y) < 3 and E.alive is 1):
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

	print(return_string_from_frame(mat)+"Score: " + str(M.score)+'\n')
	time.sleep(0.009)

score = M.score
if(level is 1 and input("Continue to next leve?(y/n)") is 'y'):
	M = Mario()
	M.score = score
	while True:
		inp = input_to(getch)
		if(inp is 'q' or M.alive is 0):
			print("Game Over")
			break
		sys.stdout.flush()
		system('clear')
		
		if(M.distanceFromStart + 50 is 100 and not(isinstance(B,BossEnemy))):
			B = BossEnemy()

		if(isinstance(B,BossEnemy)):
			B.move(M)
			if(B.life is 0):
				print("You have won")
				break

		mat = bd1.return_frame(M,B)
		M.move(inp,mat)
		if(inp == 'w'):
			if(M.in_air == 0):
				M.jumping = 1
				M.in_air = 1
		if(M.jumping == 1):
			M.jump(mat)
		else:
			M.gravity(mat)

		dist_actual = M.distanceFromStart + M.x - 50

		if(dist_actual < B.distanceFromStart):
			if(abs(dist_actual - B.distanceFromStart) < 5):
				if(M.y + 3 == B.y and not(M.jumping)):
					B.life -= 1
					M.jumping = 1
					M.frames_in_air = 9
					M.score += 1
				elif(M.y + 3 > B.y):
					M.alive = 0

		else:
			if(abs(dist_actual - B.distanceFromStart) < 14):
				if(M.y + 3 == B.y and not(M.jumping)):
					B.life -= 1
					M.jumping = 1
					M.frames_in_air = 9
					M.score += 1

				elif(M.y + 3 > B.y):
					M.alive = 0


		print(return_string_from_frame(mat)+"Score: " + str(M.score)+'\n' + "Boss Life: " + str(B.life) + '\n')

		time.sleep(0.009)

else:
	pass

print("Mario final score: " + str(M.score))


# from subprocess import call
# call(["aplay", "/home/pi/file.wav"])




