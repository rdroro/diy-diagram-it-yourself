# -*- coding: utf8 -*-
import json
import re
import exception
import codecs


class Parser:
    """
    Read DIY language and transform it in JSON
    @todo what's happen when str is empty ?
    """

    @staticmethod
    def parse_markdown(str):
        """"
        Parse str - String - to transform DIY language to dictionnary
        @todo manage errors

        Args:
            str: str string containing DIY language
        Returns:
            the parsed input in dictionnary
        """

        jsoned = []

        reElements = re.compile("(\w*)\((.*?)\)", re.S)
        reBlank = re.compile('\s*')

        elements = reElements.findall(str)
        if len(elements) == 0:
            raise exception.NoElementFoundExeception()
        for element in elements:
            jsonElement = {}
            jsonElement['type'] = element[0]
            attributes = element[1].split(";")
            for couples in attributes:
                couple = couples.split(":")
                couple[0] = reBlank.sub("", couple[0].__str__())
                # strip() seems to need a str, no unicode
                couple[1] = couple[1].encode("utf8").strip()
                # but we need to save in unicode format
                jsonElement[couple[0].__str__()] = couple[1].decode("utf8")
            jsoned.append(jsonElement)

        return jsoned

    @staticmethod
    def parse_json(str):
        """
        Parse str - String to transform JSON string to dictionnary

        Args:
            str: str string containing DIY language
        Raises:
            NotJSONException if input is not valid JSON input
        """
        try:
            jsoned = json.loads(str)

        except Exception as e:
            print e
            raise exception.NotJSONException("")

        return jsoned
