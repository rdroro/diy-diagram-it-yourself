import os
import json
import re
import hashlib
from HTMLParser import HTMLParser
import exception
from gridManagement import GridManagement
from svgRender import SvgRender

class Interpretor:

	STATS_NB_ELEMENTS="nb_elements"

	def __init__(self, json, libpath):
		""" 
		Change JSON str to svg diagram
		"""
		# self.json contains all elements write by user in dict format
		self.json = json
		# @todo Externalize lib path	
		self.libPath = libpath
		self.defaultTemplatePath = self.libPath+'/templates/default'	

		# List all available element in lib path
		self.elements = os.listdir(self.defaultTemplatePath+'/json')
		# Remove extension in list
		self.elements = [elt.replace('.json', '') for elt in self.elements]

		# Store links elements
		self.links = []

		# Store all elements (except links) in dictionnary where element['name'] is the key
		self.namedElements = {}

		self.stats = {}

		# Initialize SvgWriter for render
		self.svg = SvgRender(self.defaultTemplatePath)
		self.svgLinks = SvgRender(self.defaultTemplatePath)


	
	def generate (self):
		"""
		Parse Json included in constructor to generate diagrams
		"""
		# HTML parse
		htmlParser = HTMLParser()
		# self.writeHeader()
		for obj in self.json:
			if not obj['type'] in self.elements:
				# Element is missing in lib/.../json folder
				print "[ERROR] Unknown element: "+obj['type']
			else:
				base = json.load(open(self.defaultTemplatePath+'/json/'+obj['type']+'.json'))
				base.update(obj)

				# Links have a different behaviour than other elements
				if obj['type'] == "link":
					base['from'] = base['from'].encode("utf_8", 'xmlcharrefreplace')
					base['to']= base['to'].encode("utf_8", 'xmlcharrefreplace')
					self.links.append(base)
					continue

				base['name'] = base['name'].encode("utf_8", 'xmlcharrefreplace')

				# Get position of element into grid
				base = self.getGridPosition(base)

				# Store hash of name in namedElements
				hashName = hashlib.md5(base['name'].encode())
				self.namedElements[hashName.hexdigest()] = base

				# Transform JSON element to SVG
				self.svg.addElement(base)

		# links treatments
		for link in self.links:
			link = self.linkPosition(link)
			# Transform element in SVG
			self.svgLinks.addElement(link)

		self.svg.prependFragment(self.svgLinks.svgString)
		self.stats[Interpretor.STATS_NB_ELEMENTS] = len(self.json)

		r = {}
		r['stats'] = self.stats
		r['diy'] = self.svg.__str__()
		return r

	
	def getGridPosition (self, element):
		"""
		Transform grid position into pixel position using GridManagement

		Args:
			element: a dictionnary of one element
		Returns:
			dictonnary element passed in parameter with pixel value for x and y
		"""
		# transform position by using GridManagement
		# elements must have x and y parameters
		coord = self.splitPosition(element['position'])
		element['x'] = coord[0]
		element['y'] = coord[1]
		element = GridManagement.getPosition(element)
		return element


	def splitPosition(self, position):
		"""
		Parse "x,y" string and return list where 0 is x and 1 is y int value

		Args:
			position: a string wich can match this regex: [1-9]\d*\s*,[1-9]\d*
		Returns:
			A list where [0] represents integer x value and [1] represents integer y value
		Raises:
			exception.MalFomattedPositionException when position argument is not valid

		"""
		position = position.strip()
		if re.search("\d+\s*,\s*\d+", position) is None:
			raise exception.MalFomattedPositionException(position)

		coord = position.replace(" ", "")
		coord = coord.split(",")
		if len(coord) != 2:
			print '[ERROR] position is bad formatted'
		coord = [int(value) for value in coord]
		return coord

	def linkPosition(self, link):
		"""
		Set start and stop position for a link by getting from and to psoition element

		Args:
			link: a dictionnary representing one link
		"""
		fromHashName = hashlib.md5(link['from'].encode())
		try:
			fromElement = self.namedElements[fromHashName.hexdigest()]
		except Exception: 
			raise Exception("[ERROR] Link from element not found: "+link['from'])

		link['xStart'] = fromElement['xCenter']
		link['yStart'] = fromElement['yCenter']

		toHashName = hashlib.md5(link['to'].encode())
		try:
			toElement = self.namedElements[toHashName.hexdigest()]
		except Exception:
			raise Exception("[ERROR] Link to element not found: "+link['to'])
			sts
		link['xEnd'] = toElement['xCenter']
		link['yEnd'] = toElement['yCenter']

		return link