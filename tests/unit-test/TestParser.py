# -*- coding: utf8 -*-
import unittest
import codecs
from parser import Parser
import exception


class TestParser(unittest.TestCase):
    """
    To run tests please setup PYTHONPATH as:
    export PYTHONPATH=path_to_project_folder/diy-diagram-it-yourself/bin:${PYTHONPATH}
    and run tests by typing following command:
    python -m unittest discover -s unit-test -p 'Test*'
    """

    def setUp(self):
        print '== Test Parser =='
        jsonfile = codecs.open("unit-test/samples/demo.json",  'r', 'utf-8')
        self.jsonstr = jsonfile.read().encode("utf8")
        jsonfile.close()
        self.markdownstr = ''

    def runTest(self):
        self.parse_json_test()

    def parse_json_test(self):
        # Check the retun type
        jsonList = Parser.parse_json(self.jsonstr)
        # Must be a list
        self.assertIsInstance(jsonList, list)
        # Each elements must be dic
        for dic in jsonList:
            self.assertIsInstance(dic, dict)

        # Test values. All variables are store as unicode. decode() returns unicode
        self.assertEqual(jsonList[0]["name"], "Démo".decode("utf8"))
        self.assertEqual(jsonList[0]["type"], "box".decode("utf8"))
        self.assertEqual(jsonList[1]["name"], "Here We go #MFB".decode("utf8"))
        self.assertEqual(jsonList[1]["type"], "circle".decode("utf8"))
        self.assertEqual(jsonList[1]["position"], "2, 0".decode("utf8"))

        # If inputstr is not in json format -> Raises exception.NotJSONException
        jsonstr = '["box": name, "type": Without quotes'
        self.assertRaises(exception.NotJSONException, Parser.parse_json, jsonstr)


if __name__ == '__main__':
    unittest.main()
