#character of people

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
temp = ["(**)",
		"|  |",
		" /\ "]
_mario = []
for i in range(len(temp)):
	_mario.append([])
	for j in range(len(temp[0])):
		_mario[i].append(temp[i][j])



