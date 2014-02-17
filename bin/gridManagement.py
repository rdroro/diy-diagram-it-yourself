
class GridManagement:

	"""
	GridManagement manage the position of elements.
	It used to return pixel position from grid position.
	By default, a cell size is 200x100 px
	"""

	X_SIZE = 200
	Y_SIZE = 100

	VERTICAL_TOP_ALIGN=0
	HORIZONTAL_LEFT_ALIGN=0

	"""
	Static method which convert grid position (x, y) to pixel position.
	Use GridManagement.X_SIZE and GridManagement.Y_SIZE to determine the default
	cell size. You can also manage the vertical and horizontal alignement.
	Vertical psossible alignement values are "top", "middle", "bottom".
	Horizontal psossible alignement values are "left", "middle", "right".

	x -- The horizontal postion in a grid
	y -- The vertical position in a grid
	verticalAlignement -- The vertical position in a cell
	horizontalAlignement -- The horizontal position in a cell
	"""
	@staticmethod
	def getPosition (element):
		x = element['x']
		y = element['y'] 
		verticalAlignement = element['vertical-align'] 
		horizontalAlignement = element['horizontal-align']
		try:
			x = int(x)
			y = int(y)
		except Exception, e:
			# Raise personnal exception
			print "X or Y aren't integer values"
			return;

		# Default alignement is top, top
		verticalAlign = GridManagement.VERTICAL_TOP_ALIGN
		horizontalAlign = GridManagement.HORIZONTAL_LEFT_ALIGN

		if verticalAlignement == "middle":
			verticalAlign = element['vertical-middle']
		if verticalAlignement == "bottom":
			verticalAlign = element['vertical-bottom']

		if horizontalAlignement == "middle":
			horizontalAlign = element['horizontal-middle']
		if horizontalAlignement == "right":
			horizontalAlign = element['horizontal-right']

		position = {}
		position['x'] = x*GridManagement.X_SIZE+horizontalAlign
		position['y'] = y*GridManagement.Y_SIZE+verticalAlign
		return position