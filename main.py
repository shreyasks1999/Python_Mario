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

	#end loop
	if(inp is 'q' or M.life is 0):
		print("Game Over")
		system('afplay gameover.wav&')
		# system('aplay gameover.wav&')
		break

	sys.stdout.flush()
	system('clear')
	
	#see if enemy is in frame
	for i in config._list_of_enemies:
		if(M.distanceFromStart + 70 == i):
			E.init_enemy(i)
	
	if(E.alive == 1):
		E.oscillate()

	#detect enemy collision
	if(abs(E.distanceFromStart - (M.distanceFromStart + M.x - 50)) < 5):
		if(M.y + 3 is E.y and not(M.jumping) and E.alive is 1):
			M.score += 1
			E.ch = config._enemy_empty
			E.alive = 0
			system('afplay stomp.wav&')
			# system('aplay gameover.wav&')


		elif(abs(M.y - E.y) < 3 and E.alive is 1):
			M.life -= 1
			E.ch = config._enemy_empty
			E.alive = 0
			if(M.life):
				system('afplay died.wav&')
			# system('aplay died.wav&')

	#mat has 42 * 100 matrix of frame
	mat = bd.return_frame(M,E)
	M.move(inp,mat)

	#jump move
	if(inp == 'w'):
		if(M.in_air == 0):
			# system('aplay jump.wav&')
			system('afplay jump.wav&')
			M.jumping = 1
			M.in_air = 1

	if(M.jumping == 1):
		M.jump(mat)
	else:
		M.gravity(mat)

	print(return_string_from_frame(mat)+"Score: " + str(M.score)+'\n' + "Life: " + str(M.life) + '\n')
	time.sleep(0.009)

score = M.score
if(level is 1 and input("Continue to next leve?(y/n)") is 'y'):
	M = Mario()
	M.score = score

	while True:
		inp = input_to(getch)
		if(inp is 'q' or M.alive is 0):
			system('afplay gameover.wav&')
			# system('aplay gameover.wav&')
			print("Game Over")
			break
		sys.stdout.flush()
		system('clear')
		
		#first time initialize enemy
		if(M.distanceFromStart + 50 is 100 and not(isinstance(B,BossEnemy))):
			B = BossEnemy()

		#if boss exists,move him 
		if(isinstance(B,BossEnemy)):
			B.move(M)
			if(B.life is 0):
				print("You have won")
				# system('aplay b_stomp.wav&')
				system('afplay victory.wav&')
				break

		mat = bd1.return_frame(M,B)

		#mario movement
		M.move(inp,mat)

		#jump move
		if(inp == 'w'):
			if(M.in_air == 0):
				# system('aplay jump.wav&')
				system('afplay jump.wav&')
				M.jumping = 1
				M.in_air = 1

		if(M.jumping == 1):
			M.jump(mat)
		else:
			M.gravity(mat)

		dist_actual = M.distanceFromStart + M.x - 50

		#detect enemy collision
		if(dist_actual < B.distanceFromStart):
			if(abs(dist_actual - B.distanceFromStart) < 5):
				if(M.y + 3 == B.y and not(M.jumping)):
					B.life -= 1
					M.jumping = 1
					M.frames_in_air = 9
					M.score += 1
					B.move(M)
					B.move(M)
					# system('aplay b_stomp.wav&')
					system('afplay stomp.wav&')

				elif(M.y + 3 > B.y):
					M.alive = 0

		else:
			if(abs(dist_actual - B.distanceFromStart) < 14):
				if(M.y + 3 == B.y and not(M.jumping)):
					B.life -= 1
					M.jumping = 1
					M.frames_in_air = 9
					M.score += 1
					B.move(M)
					B.move(M)
					# system('aplay b_stomp.wav&')
					system('afplay stomp.wav&')

				elif(M.y + 3 > B.y):
					M.alive = 0


		print(return_string_from_frame(mat)+"Score: " + str(M.score)+'\n' + "Boss Life: " + str(B.life) + '\n')

		time.sleep(0.009)

else:
	pass

print("Mario final score: " + str(M.score))





