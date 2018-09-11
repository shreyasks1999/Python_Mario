from colorama import Fore,Back

#player mario
temp  = [['(','o','o',')'],
		  ['/','M','M','\\'],
		  [' ','/','\\',' ']]

_mario = []
for i in range(len(temp)):
	_mario.append([])
	for j in range(len(temp[0])):
		_mario[i].append(Fore.GREEN + temp[i][j] + Fore.RESET)

#enemy facing left
temp =   [['<','(','o',')'],
		  [' ','(',' ',')'],
		  [' ','/',' ','\\']]

_enemy = []
for i in range(len(temp)):
	_enemy.append([])
	for j in range(len(temp[0])):
		_enemy[i].append(Fore.RED + temp[i][j] + Fore.RESET)


#enemy facing right
temp = 	  [['(','o',')','>'],
		   ['(',' ',')',' '],
		   ['/',' ','\\',' ']]

_enemy2 = []
for i in range(len(temp)):
	_enemy2.append([])
	for j in range(len(temp[0])):
		_enemy2[i].append(Fore.RED + temp[i][j] + Fore.RESET)

_enemy_empty = [[' ',' ',' ',' '],
				[' ',' ',' ',' '],
				[' ',' ',' ',' ']]


#BOSS villian
temp = 		   ["/\/\/\/\/\/\/\\",
				"  _/ \_/ \_   ",
				"  \|0   0|/   ",
				" _(_  ^  _)_  ",
				"/`\|V***V|/`\ ",
				"\  \_____/  / ",
				"/\   )=(   /\ ",
				"/ \_/\=/\_/  \\"]


_boss_enemy = []
for i in range(len(temp)):
	_boss_enemy.append([])
	for j in range(len(temp[0])):
		_boss_enemy[i].append(Fore.RED + temp[i][j] + Fore.RESET)




#board related info
_brick = [Fore.YELLOW + '[' + Fore.RESET,Fore.YELLOW + ']' + Fore.RESET]
_list_of_bricks = [10,93,145,185,231,290,334,391,430,474,480]
_list_of_enemies = [70,165,280,385]
_list_of_brickLengths = [10,12,14,16,18]



#clouds
temp = 	   ["          .-~~~-..-~~~-..-~~~-..-~~~-.            ", 
			"  .- ~ ~-(////////////////////////////)____       ",
			" ///////////////////////////////////////////~ -.  ",
			"|///////////////////////////////////////////////\ ",
			" \/////////////////////////////////////////////// ",
			"   \////////////////////////////////////////////  ",
			"    /  /  /  /  /  /  /  /  /  /  /  /  /  /  /   ",
			"     /  /  /  /  /  /  /  /  /  /  /  /  /  /     "]




_clouds = []
for i in range(len(temp)):
	_clouds.append([])
	for j in range(len(temp[0])):
		_clouds[i].append(Fore.BLUE + temp[i][j] + Fore.RESET)

#pipes
temp = ["[#####]",
		"[#####]",
		"[#####]",
		"[#####]",
		"[#####]"]

_pipe = []
for i in range(len(temp)):
	_pipe.append([])
	for j in range(len(temp[0])):
		_pipe[i].append(Fore.CYAN + temp[i][j] + Fore.RESET)




