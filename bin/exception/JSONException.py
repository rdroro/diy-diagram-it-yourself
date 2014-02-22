
class NotJSONException (Exception):
	"""docstring for NotJSONException """
	def __init__(self, arg):
		
		self.arg = arg

	def __str__(self):
		return repr(self.value)
		