class SvgRender:

	"""SvgRender is a class for write SVG element in output"""

	def __init__(self, lib):
		self.libPath = lib
		self.svgString = ""
		self.writeHeader()

	def addElement(self, elements):
		eltFile = open(self.libPath+'/svg/'+elements['type']+'.svg')
		elt = eltFile.read()
		eltFile.close
		for key, value in elements.iteritems():
			if (key != 'type'):
				elt = elt.replace('{{'+key.__str__()+'}}', value.__str__())
		self.svgString += "\n"+elt

	"""
	Write svg header (in LIB/templates/default/svg/partials/header.tpl) 
	into Public variable self.svgString
	"""
	def writeHeader(self):
		# import os
		# print os.listdir("../lib/")
		header = open(self.libPath+'svg/partials/header.tpl')
		self.svgString = header.read()
		header.close()
		return

	"""
	Write </svg> tag into Public variable self.svgString
	"""
	def writeFooter(self):
		self.svgString += "\n</svg>"
		return

	def __str__(self):
		return self.svgString