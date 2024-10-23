import os

from pycman.charset import Charset
from pycman.levels import Levels

WIDTH = 80
HEIGHT = 30

def start_pycman():
	print( "Welcome to the world of P@cman" )
	size = os.get_terminal_size()
	print( f"Your screen is {size.columns} x {size.lines}" )
	
	# Load and set Charset
	chars = Charset()
	charsets = chars.get_charsets()
	print( charsets )
	chars.set_charset( charsets[ 0 ] )

	# Load and set Level
	levels = Levels()
	level_keys = levels.get_levels()
	level = levels.get_level( level_keys[ 0 ] )
	formatted_level = chars.get_formatted_level( level )
	print_screen( formatted_level )


def print_screen( level ):
	print( level )
