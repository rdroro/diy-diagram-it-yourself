import json
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
		jsoned = ""
		try:
			jsoned = json.load(file)
		except Exception:
			raise exception.NotJSONException("")

		return jsoned

		

