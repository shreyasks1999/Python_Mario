import config
from board_class import *
from people_class import *
from input import Get,input_to

M = Mario()
bd = Board(42,500)
bd.board_level()

bd1 = Board(42,200)

getch = Get()

E = Enemy()
E.distanceFromStart = 70

B = None
level = 0
