import os
from pacman.level_01 import level_01

WIDTH = 80
HEIGHT = 30

def start_pacman():
	print( "Welcome to the world of Pacman" )
	size = os.get_terminal_size()
	print( f"Your screen is {size.columns} x {size.lines}" )
	print_screen()


def print_screen():
	print( level_01 )
