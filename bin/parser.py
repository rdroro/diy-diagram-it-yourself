import json
from interpretor import Interpretor

class Parser:
	"""
	Read DIY language and transform it in JSON
	"""
	def __init__ (self, str):
		self.str = str

	def parse (self):
		# Transform self.str to json
		# For the test, self.str is already json
		self.json = json.load(self.str)
		self.transform()

	def transform (self):
		interpretor = Interpretor (self.json)
		interpretor.generate()

		

