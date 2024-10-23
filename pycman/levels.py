import os
from pycman.config import load_config

levels_path = "pycman/data/levels/"

class Levels():
	def __init__( self ):
		self._levels =  load_config( "level", levels_path, "level_", ".txt" )

	def set_level( self, key ):
		if key not in self._levels.data:
			raise ValueError( "Invalid level key" )
		self._levels.key = key

	def get_levels( self ):
		levels = []
		for level in self._levels.data.keys():
			levels.append( level )
		return levels

	def get_level( self, key ):
		if key not in self._levels.data:
			raise ValueError( "Invalid level key" )
		return self._levels.data[ key ]
