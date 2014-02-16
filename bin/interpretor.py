import os
import json
import re
from gridManagement import GridManagement
from svgRender import SvgRender

class Interpretor:
	""" 
	Change JSON str to svg diagram
	"""
	def __init__(self, json):
		# self.json contains all elements write by user in dict format
		self.json = json
		# @todo Externalize lib path	
		self.libPath = '../lib/'
		self.defaultTemplatePath = self.libPath+'templates/default/'	

		# List all available element in lib path
		self.elements = os.listdir(self.defaultTemplatePath+'json')
		# Remove extension in list
		self.elements = [elt.replace('.json', '') for elt in self.elements]

		# Initialize SvgWriter for render
		self.svg = SvgRender(self.defaultTemplatePath)


	"""
	Parse Json included in constructor to generate diagrams
	"""
	def generate (self):

		# self.writeHeader()
		for obj in self.json:
			if not obj['type'] in self.elements:
				# Element is missing in lib/.../json folder
				print "[ERROR] Unknown element: "+obj['type']
			else:
				base = json.load(open(self.defaultTemplatePath+'json/'+obj['type']+'.json'))
				base.update(obj)

				# Transform calculated statements
				base = self.evalCalculatedStatements(base, False)

				# Get position of element into grid
				base = self.getGridPosition(base)

				# Transform calculated statements
				base = self.evalCalculatedStatements(base, True)


				# Transform element in SVG
				self.svg.addElement(base)

		self.svg.writeFooter()
		self.writeFile('demo.svg', self.svg.__str__())
		return

	"""
	Eval each calculated statements identified by ##(.*)##
	@param element a dictionnary of one element
	@return dictionnary element passed in parameter with eval calculated statements 
	"""
	def evalCalculatedStatements(self, element, pEval):
		for key, value in element.iteritems():
			if (key != 'type'):
				if not re.match('##(.*)##', value.__str__()) is None:
					value = value.__str__().replace('#', '')
					references = re.findall('(this\.([a-zA-Z0-9_]*))', value)
					for ref in references:
						value = value.__str__().replace(ref[0], "element['"+ref[1]+"']")

				if pEval and re.findall("element\['.*'\]", value.__str__()):
					value = eval(value)
				
				element[key] = value
		return element


	"""
	Transform grid position into pixel position using GridManagement
	@param element a dictionnary of one element
	@return dictonnary element passed in parameter with pixel value for x and y
	"""
	def getGridPosition (self, element):
		# transform position by using GridManagement
		# elements must have x and y parameters
		position = GridManagement.getPosition(element['x'], element['y'], element['vertical-align'], element['horizontal-align'])
		element['x'] = position['x']
		element['y'] = position['y']
		return element
	

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