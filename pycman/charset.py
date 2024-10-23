import os
from pycman.config import load_config

charset_path = "pycman/data/charsets/"

class Charset():
	def __init__( self ):
		self._charsets = load_config( "charset", charset_path, "charset_", ".txt" )
	
	def _get_char( self, c ):
		if c not in self._charsets.data[ self._charsets.key ]:
			return c
		return self._charsets.data[ self._charsets.key ][ c ]
	
	def get_formatted_level( self, level ):
		formatted_level = ""
		for c in level:
			c2 = self._get_char( c )
			formatted_level += c2
		return formatted_level

	def set_charset( self, key ):
		if key not in self._charsets.data:
			raise ValueError( "Invalid charset key" )
		self._charsets.key = key

	def get_charsets( self ):
		charsets = []
		for charset in self._charsets.data.keys():
			charsets.append( charset )
		return charsets
