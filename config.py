#large mario
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

temp =   [['<','(','o',')'],
		  [' ','(',' ',')'],
		  [' ','/',' ','\\']]

_enemy = []
for i in range(len(temp)):
	_enemy.append([])
	for j in range(len(temp[0])):
		_enemy[i].append(Fore.RED + temp[i][j] + Fore.RESET)


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
# _list_of_pipes = [52,75,120,190,302,399,]
_list_of_pipes = [53 - 10,74,155 - 7 - 10,169,270 - 7 - 10,284,375 - 7 - 10,389]
_list_of_enemies = [70,165,280,385]
_list_of_brickLengths = [10,12,14,16,18]




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




