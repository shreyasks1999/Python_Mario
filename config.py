#large mario
temp =		["  ▒▒▒▒▒      ",
			 "  ▒▒▒▒▒▒▒▒▒  ",
			 "  ▓▓▓░░▓░    ",
			 " ▓░▓░░░▓░░░  ",
			 " ▓░▓▓░░░▓░░░ ",
			 " ▓▓░░░░▓▓▓▓  ",
			 "  ░░░░░░░░   ",
			 "  ▓▓▒▓▓▓▒▓▓  ",
			 " ▓▓▓▒▓▓▓▒▓▓▓ ",
			 "▓▓▓▓▒▒▒▒▒▓▓▓▓",
			 "░░▓▒░▒▒▒░▒▓░░",
			 "░░░▒▒▒▒▒▒▒░░░",
			 "░░▒▒▒▒▒▒▒▒▒░░",
			 "  ▒▒▒   ▒▒▒  ",
			 "▓▓▓    ▓▓▓   ",
			 "▓▓▓▓    ▓▓▓▓ "]

large_mario = []
for i in range(len(temp)):
	large_mario.append([])
	for j in range(len(temp[0])):
		large_mario[i].append(temp[i][j])




#player mario
temp = ["(oo)",
		"|__|",
		" /\ "]
_mario = []
for i in range(len(temp)):
	_mario.append([])
	for j in range(len(temp[0])):
		_mario[i].append(temp[i][j])


#board related info
_brick = ['[',']']
_list_of_bricks = [10,93,145,185,231,290,334,391,430,474,480]
_list_of_pipes = [30,120]


temp = 	   ["          .-~~~-.	          ", 
			"  .- ~ ~-(///////)____       ",
			" //////////////////////~ -.  ",
			"|//////////////////////////\ ",
			" \////////////////////////// ",
			"   \///////////////////////  ",
			"     /  /  /  /  /  /  /     ",
			"     /  /  /  /  /  /  /     "]


_clouds = []
for i in range(len(temp)):
	_clouds.append([])
	for j in range(len(temp[0])):
		_clouds[i].append(temp[i][j])

