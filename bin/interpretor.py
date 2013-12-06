class Interpretor:
	""" 
	Change JSON str to svg diagram
	"""
	def __init__(self, json):
		self.json = json
		self.outputFileName = 'demo.svg'
		self.libPath = '../lib/'
		self.defaultTemplatePath = self.libPath+'templates/default/'

	"""
	Parse Json included in constructor to generate diagrams
	"""
	def generate (self):
		for obj in self.json:
			if obj['type'] == 'box':
				self.writeHeader()
				template = self.readFile(self.defaultTemplatePath+'svg/box.svg')
				template = template.replace('{{name}}', obj['name'])
				self.appendInFile(self.outputFileName, template)
		self.appendInFile(self.outputFileName, '</svg>')
		return

	"""
	Write <svg> tag and file description into svg file
	"""
	def writeHeader(self):
		# import os
		# print os.listdir("../lib/")
		self.outputFile = open(self.outputFileName, 'w')
		header = open(self.defaultTemplatePath+'svg/partials/header.tpl')
		self.outputFile.write(header.read())
		header.close()
		self.outputFile.close()
		return

	"""
	Close </svg> tag into generate svg file
	"""
	def writeFooter(self):
		print '</svg>'
		return

	"""
	Simple function to add content at the end of file
	@param filePath string path to the file
	@param content string content to write
	"""
	def appendInFile(self, filePath, content):
		tmp = open(filePath, 'a')
		tmp.write(content)
		tmp.close
		return

	"""
	Simple function to add content into the file.
	delete all previous content
	@param filePath string path to the file
	@param content string content to write
	"""
	def writeFile(self, filePath, content):
		tmp = open(filePath, 'w')
		tmp.write(content)
		tmp.close()
		return

	"""
	Simple function read file
	@param filePath string path to the file
	@return content of file
	"""
	def readFile (self, filePath):
		tmp = open(filePath)
		content = tmp.read()
		tmp.close()
		return content