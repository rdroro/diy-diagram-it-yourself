class Interpretor:
	""" 
	Change JSON str to svg diagram
	"""
	def __init__(self, json):
		self.json = json
		self.outputFileName = 'demo.svg'
		self.libPath = '../lib/'

	def generate (self):
		for obj in self.json:
			if obj['type'] == 'box':
				self.writeHeader()
				template = self.readFile(self.libPath+'svg-templates/default/box.svg')
				template = template.replace('{{name}}', obj['name'])
				self.appendInFile(self.outputFileName, template)
		self.appendInFile(self.outputFileName, '</svg>')
		return

	def writeHeader(self):
		# import os
		# print os.listdir("../lib/")
		self.outputFile = open(self.outputFileName, 'w')
		header = open(self.libPath+'svg-templates/default/partials/header.tpl')
		self.outputFile.write(header.read())
		header.close()
		self.outputFile.close()
		return

	def writeFooter(self):
		print '</svg>'
		return

	def appendInFile(self, filePath, content):
		tmp = open(filePath, 'a')
		tmp.write(content)
		tmp.close
		return

	def writeFile(self, filePath, content):
		tmp = open(filePath, 'w')
		tmp.write(content)
		tmp.close()
		return

	def readFile (self, filePath):
		tmp = open(filePath)
		content = tmp.read()
		tmp.close()
		return content