import os
class Interpretor:
	""" 
	Change JSON str to svg diagram
	"""
	def __init__(self, json):
		self.json = json
		self.outputFileName = 'demo.svg'
		self.libPath = '../lib/'
		self.defaultTemplatePath = self.libPath+'templates/default/'
		self.element = os.listdir(self.defaultTemplatePath+'json')
		self.xBase = 202
		self.xMargin = 10
		self.xText = 102


	"""
	Parse Json included in constructor to generate diagrams
	"""
	def generate (self):
		i = 0
		self.writeHeader()
		for obj in self.json:
			if obj['type'] == 'box':
				template = self.readFile(self.defaultTemplatePath+'svg/box.svg')
				template = template.replace('{{name}}', obj['name'])
				template = template.replace('{{x}}', (self.xBase*i+self.xMargin*i).__str__())
				template = template.replace('{{xText}}', (self.xText+self.xBase*i+self.xMargin*i).__str__())
				self.appendInFile(self.outputFileName, template)
				i = i+1
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