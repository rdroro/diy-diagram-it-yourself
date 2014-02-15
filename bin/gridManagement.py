
class GridManagement:

	"""
	GridManagement manage the position of elements.
	It may used to return pixel position from grid position.
	By default, a cell size is 200x100 px
	"""

	X_SIZE = 200
	Y_SIZE = 100

	@staticmethod
	def getPosition (x, y):
		try:
			x = int(x)
			y = int(y)
		except Exception, e:
			# Raise personnal exception
			print "X or Y aren't integer values"
			return;
		position = {}
		position['x'] = x*GridManagement.X_SIZE
		position['y'] = y*GridManagement.Y_SIZE
		return position