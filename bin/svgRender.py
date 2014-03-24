import re


class SvgRender:
    """
    SvgRender is a class for write SVG element in output
    """

    def __init__(self, lib):
        """
        Constructor

        lib -- string, the path to svg element containing *.svg

        """
        self.libPath = lib
        self.svgString = ""
        self.hasHeader = False
        self.hasFooter = False

    def addElement(self, element):
        """
        Transform json element to svg element. Replace all {{KEY}} value by {{VALUE}}

        element -- dictionnary

        """
        eltFile = open(self.libPath+'/svg/'+element['type']+'.svg')
        elt = eltFile.read()
        eltFile.close
        for key, value in element.iteritems():
            if (key != 'type'):
                elt = elt.replace('{{'+key.__str__()+'}}', value.__str__().decode("utf-8"))
        self.svgString += "\n"+elt

    def prependFragment(self, svgElement):
        """
        Simple add svg fragment to the beginning of document

        svgElement -- string svg element(s)

        """
        if self.hasHeader:
            # Raise Exception
            print "[ERROR] Impossible to add fragment. Header is already defined"
            return
        self.svgString = "\n"+svgElement+self.svgString

    def getHeader(self):
        """
        Return svg header saved in self.libPath/svg/partials/header.tpl
        """
        header = open(self.libPath+'/svg/partials/header.tpl')
        headerStr = header.read()
        header.close()
        return headerStr

    def getFooter(self):
        """
        Return svg end tag: \n</svg>
        """
        return "\n</svg>"

    def writeHeader(self, size):
        """
        Write svg header (in LIB/templates/default/svg/partials/header.tpl)
        into Public variable self.svgString
        """
        headerStr = self.getHeader()
        headerStr = headerStr.replace('{{x}}', size['x'].__str__())
        headerStr = headerStr.replace('{{y}}', size['y'].__str__())
        self.svgString = headerStr+self.svgString
        self.hasHeader = True
        return

    def writeFooter(self):
        """
        Write </svg> tag into Public variable self.svgString
        """
        self.svgString += self.getFooter()
        self.hasFooter = True
        return

    def __str__(self):
        """
        Overwrite __str__ to display a SVG document with header and footer
        If header and footer are not set, __str__ add them
        """
        svgDocument = ""
        if not self.hasHeader:
            svgDocument = self.getHeader()

        svgDocument += self.svgString

        if not self.hasFooter:
            svgDocument += self.getFooter()

        return svgDocument
