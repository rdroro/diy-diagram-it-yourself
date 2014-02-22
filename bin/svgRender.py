import re

class SvgRender:

	"""
	SvgRender is a class for write SVG element in output
	"""

	"""
	Constructor

	lib -- string, the path to svg element containing *.svg
	"""
	def __init__(self, lib):
		self.libPath = lib
		self.svgString = ""
		self.hasHeader = False
		self.hasFooter = False

	"""
	Transform json element to svg element. Replace all {{KEY}} value by {{VALUE}}

	element -- dictionnary
	"""
	def addElement(self, element):
		eltFile = open(self.libPath+'/svg/'+element['type']+'.svg')
		elt = eltFile.read()
		eltFile.close
		for key, value in element.iteritems():
			if (key != 'type'):
				elt = elt.replace('{{'+key.__str__()+'}}', value.__str__())
		self.svgString += "\n"+elt

	"""
	Simple add svg fragment to the beginning of document

	svgElement -- string svg element(s)
	"""
	def prependFragment(self, svgElement):
		if self.hasHeader:
			# Raise Exception
			print "[ERROR] Impossible to add fragment. Header is already defined"
			return
		self.svgString = "\n"+svgElement+self.svgString

	"""
	Return svg header saved in self.libPath/svg/partials/header.tpl
	"""
	def getHeader(self):
		header = open(self.libPath+'/svg/partials/header.tpl')
		headerStr = header.read()
		header.close()
		return headerStr

	"""
	Return svg end tag: \n</svg>
	"""
	def getFooter(self):
		return "\n</svg>"


	"""
	Write svg header (in LIB/templates/default/svg/partials/header.tpl) 
	into Public variable self.svgString
	"""
	def writeHeader(self):
		self.svgString = self.getHeader()+self.svgString
		self.hasHeader = True
		return

	"""
	Write </svg> tag into Public variable self.svgString
	"""
	def writeFooter(self):
		self.svgString += self.getFooter()
		self.hasFooter = True
		return

	"""
	Overwrite __str__ to display a SVG document with header and footer
	If header and footer are not set, __str__ add them
	"""
	def __str__(self):
		svgDocument = ""
		if not self.hasHeader:
			svgDocument = self.getHeader()

		svgDocument += self.svgString

		if not self.hasFooter:
			svgDocument += self.getFooter()

		return svgDocument