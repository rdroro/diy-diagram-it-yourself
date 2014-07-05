# -*- coding: utf8 -*-
import os
import json
import re
import hashlib
import exception
from gridManagement import GridManagement
from svgRender import SvgRender


class Interpretor:

    STATS_NB_ELEMENTS = "nb_elements"
    STATS_NB_LINKS = "nb_links"

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

        # Save the max size of element position
        self.maxsize = {}
        self.maxsize['x'] = 0
        self.maxsize['y'] = 0

        # Initialize SvgWriter for render
        self.svg = SvgRender(self.defaultTemplatePath)
        self.svgLinks = SvgRender(self.defaultTemplatePath)

    def generate(self):
        """
        Parse Json included in constructor to generate diagrams

        Raises:
            exception.ElementNotFoundException: when a type element is unknown
        """
        # self.writeHeader()
        for obj in self.json:
            if not obj['type'] in self.elements:
                # Element is missing in lib/.../json folder
                raise exception.ElementNotFoundException(obj['type'])
            else:
                base = json.load(open(self.defaultTemplatePath+'/json/'+obj['type']+'.json'))
                base.update(obj)

                # Links have a different behaviour than other elements
                if obj['type'] == "link":
                    base['from'] = base['from']
                    base['to'] = base['to']
                    self.links.append(base)
                    continue

                base['name'] = base['name']
                if not base['link'] is None:
                    self.transformEmbeddedLink(base)

                # Get position of element into grid
                base = self.getGridPosition(base)

                # Store hash of name in namedElements
                hashName = hashlib.md5(base['name'].encode("utf8"))
                self.namedElements[hashName.hexdigest()] = base

                # Transform JSON element to SVG
                self.svg.addElement(base)

        # links treatments
        for link in self.links:
            link = self.linkPosition(link)
            # Transform element in SVG
            self.svgLinks.addElement(link)

        self.svg.prependFragment(self.svgLinks.svgString)
        self.stats[Interpretor.STATS_NB_ELEMENTS] = len(self.namedElements)
        self.stats[Interpretor.STATS_NB_LINKS] = len(self.links)

        r = {}
        r['stats'] = self.stats
        size = GridManagement.getDimension(self.maxsize)
        self.svg.writeHeader(size)
        r['diy'] = self.svg.__str__()
        return r

    def getGridPosition(self, element):
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

        if coord[0] > self.maxsize['x']:
            self.maxsize['x'] = coord[0]
        if coord[1] > self.maxsize['y']:
            self.maxsize['y'] = coord[1]

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

        regex = re.compile('\s')
        coord = regex.sub("", position)
        coord = coord.split(",")
        if len(coord) != 2:
            raise exception.MalFomattedPositionException(position)
        coord = [int(value) for value in coord]
        return coord

    def transformEmbeddedLink(self, element):
        """
        Transform embedded link to normal link

        Args:
            element: A element dictionnary
        """
        element['link'] = element['link']
        toElements = element['link'].split(',')
        ref = json.load(open(self.defaultTemplatePath+'/json/link.json'))
        for toElt in toElements:
            toElt = toElt.strip()
            generatedLink = ref.copy()
            generatedLink['type'] = "link"
            generatedLink['from'] = element['name']
            generatedLink['to'] = toElt
            self.links.append(generatedLink)

    def linkPosition(self, link):
        """
        Set start and stop position for a link by getting from and to position element

        Args:
            link: a dictionnary representing one link
        Returns:
            dictionnary link element with start and end position in pixel
        """
        fromHashName = hashlib.md5(link['from'])
        try:
            fromElement = self.namedElements[fromHashName.hexdigest()]
        except Exception:
            raise exception.NameNotFoundException(link['from'])

        link['xStart'] = fromElement['xCenter']
        link['yStart'] = fromElement['yCenter']

        toHashName = hashlib.md5(link['to'])
        try:
            toElement = self.namedElements[toHashName.hexdigest()]
        except Exception:
            raise exception.NameNotFoundException(link['to'])
            sts
        link['xEnd'] = toElement['xCenter']
        link['yEnd'] = toElement['yCenter']

        return link
