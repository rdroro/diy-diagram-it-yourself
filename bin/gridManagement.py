# -*- coding: utf8 -*-
import exception


class GridManagement:

    """
    GridManagement manage the position of elements.
    It used to return pixel position from grid position.
    By default, a cell size is 200x100 px
    """

    X_SIZE = 200
    Y_SIZE = 100

    VERTICAL_TOP_ALIGN = 0
    HORIZONTAL_LEFT_ALIGN = 0

    """
    Static method which convert grid position (x, y) to pixel position.
    Use GridManagement.X_SIZE and GridManagement.Y_SIZE to determine the default
    cell size. You can also manage the vertical and horizontal alignement.
    Vertical possible alignement values are "top", "middle", "bottom".
    Horizontal psossible alignement values are "left", "middle", "right".

    Args:
        element - a dictionary that must contains key:
            x -- The horizontal postion in a grid
            y -- The vertical position in a grid
            vertical-align -- The vertical position in a cell
            horizontal-align -- The horizontal position in a cell
            vertical-middle -- integer value
            vertical-top -- integer value
            horizontal-middle -- integer value
            horizontal-right -- integer value
    Raises:
        NotIntegerValueException -- when one value is not integer
    """
    @staticmethod
    def getPosition(element):
        x = element['x']
        y = element['y']
        verticalAlignement = element['vertical-align']
        horizontalAlignement = element['horizontal-align']

        # Default alignement is top, top
        verticalAlign = GridManagement.VERTICAL_TOP_ALIGN
        horizontalAlign = GridManagement.HORIZONTAL_LEFT_ALIGN

        if verticalAlignement == "middle":
            verticalAlign = element['vertical-middle']
        if verticalAlignement == "bottom":
            verticalAlign = element['vertical-bottom']

        if horizontalAlignement == "middle":
            horizontalAlign = element['horizontal-middle']
        if horizontalAlignement == "right":
            horizontalAlign = element['horizontal-right']

        try:
            x = int(x)
            y = int(y)
            horizontalAlign = int(horizontalAlign)
            verticalAlign = int(verticalAlign)
            xCenter = int(element["xCenter"])
            yCenter = int(element["yCenter"])
        except Exception as e:
            raise exception.NotIntegerValueException(e)

        element['x'] = x*GridManagement.X_SIZE+horizontalAlign
        element['y'] = y*GridManagement.Y_SIZE+verticalAlign
        # The element center move with its position
        element['xCenter'] = element['x']+xCenter
        element['yCenter'] = element['y']+yCenter
        return element

    @staticmethod
    def getDimension(maxsize):
        size = {}
        size['x'] = (maxsize['x']+1)*GridManagement.X_SIZE
        size['y'] = (maxsize['y']+1)*GridManagement.Y_SIZE
        return size
