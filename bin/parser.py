import json
import re
import exception

class Parser:
	"""
	Read DIY language and transform it in JSON
	"""

	@staticmethod
	def parse (file):
		""""
		Parse file - a file object - to transform DIY language to JSONArray

		Args:
			file: file object containing DIY language
		Returns:
			the parsed input. JSONArray
		Raises:
			NotJSONException if input is not valid JSON input

		"""

		jsoned = []

		reElements = re.compile("(\w*)\((.*?)\)", re.S)
		reBlank = re.compile('\s*')

		# get only code between tag @diy: :yid@
		# get each element
		elements = reElements.findall(file)
		if len(elements) == 0:
			raise exception.NoElementFoundExeception()
		for element in elements:
			jsonElement = {}
			jsonElement['type'] = element[0]
			attributes = element[1].split(";")
			for couples in attributes:
				couple = couples.split(":")
				couple[0] = reBlank.sub("", couple[0].__str__())
				couple[1] = couple[1].__str__().strip()
				jsonElement[couple[0].__str__()] = couple[1].__str__()
			jsoned.append(jsonElement)



		return jsoned

	@staticmethod
	def load(file):
		jsoned = ""
		try:
			jsoned = json.loads(file)
		except Exception as e:
			raise exception.NotJSONException("")

		return jsoned

		

