import config
from board_class import *
from people_class import *
from input import Get,input_to

M = Mario()
bd = Board(config._list_of_bricks)
getch = Get()

E = Enemy()
E.distanceFromStart = 70

