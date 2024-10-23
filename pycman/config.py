import os

class ConfigItem():
	def __init__( self ):
		self.key = ""
		self.data = {}

def load_config( config_type, config_path, prefix, postfix ):
	item = ConfigItem()

	# Get all level files from levels path
	files = []
	for filename in os.listdir( config_path ):
		if filename.startswith( prefix ) and filename.endswith( postfix ):
			files.append( filename )
	
	# A level file must be found
	if len( files ) == 0:
		raise FileNotFoundError( "No {config_type} files found." )
	
	# Sort the files to maintain order
	files = sorted( files )

	# Read the files
	for filename in files:
		filepath = os.path.join( config_path, filename )
		with open( filepath, "r" ) as file:
			content = file.read()
		lines = content.splitlines()
		if len( lines ) < 2:
			raise Exception(
				"Invalid format for {config_type} file {filename}. Must have more than 1 lines."
			)
		level_name = lines[ 0 ]
		if config_type == "charset":
			item.data[ level_name ] = {}
			for i in range( 1, len( lines ) ):
				line = lines[ i ]
				if len( line ) > 1:
					item.data[ level_name ][ line[ 0 ] ] = line[ 1 ]
		elif config_type == "level":
			item.data[ level_name ] = "\n".join( lines[ 1: ] )
	
	# Set the default to first item found
	item.key = list( item.data.keys() )[ 0 ]
	
	return item