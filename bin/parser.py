import json

class Parser:
	"""
	Read DIY language and transform it in JSON
	"""

	@staticmethod
	def parse (file):
		# Transform self.str to json
		# For the test, self.str is already json
		jsoned = json.load(file)
		return jsoned

		

