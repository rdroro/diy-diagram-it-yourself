# -*- coding: utf8 -*-
import unittest
from gridManagement import GridManagement


class TestGridManagement(unittest.TestCase):
    """
    To run tests please setup PYTHONPATH as:
    export PYTHONPATH=path_to_project_folder/diy-diagram-it-yourself/bin:${PYTHONPATH}
    and run tests by typing following command:
    python -m unittest discover -s unit-test -p 'Test*'
    """

    def setUp(self):
        print '== Test GridManagement =='
        self.element = {}
        self.element['x'] = "2"
        self.element['y'] = "2"
        self.element['vertical-middle'] = "10"
        self.element['vertical-bottom'] = "20"
        self.element['horizontal-middle'] = "2"
        self.element['horizontal-right'] = "4"
        self.element['horizontal-align'] = "middle"
        self.element['vertical-align'] = "middle"
        self.element['xCenter'] = "50"
        self.element['yCenter'] = "50"

    def runTest(self):
        e = self.element.copy()
        GridManagement.getPosition(e)
        self.position_test(e)

    def position_test(self, e):
        # X position must be equal to cell width * x position (into grid system) + horizontal alignement
        xalign = self.element['horizontal-align']
        xalign = int(self.element['horizontal-'+xalign])
        x = int(self.element['x'])

        yalign = self.element['vertical-align']
        yalign = int(self.element['vertical-'+yalign])
        y = int(self.element['y'])

        xResult = GridManagement.X_SIZE*x+xalign
        yResult = GridManagement.Y_SIZE*y+yalign
        self.assertEqual(e['x'], xResult, "X position is not valid: Resultat:"+e['x'].__str__()+" required: "+xResult.__str__())
        self.assertEqual(e['y'], yResult, "Y position is not valid: Resultat:"+e['y'].__str__()+" required: "+yResult.__str__())


if __name__ == '__main__':
    unittest.main()
