# -*- coding: utf8 -*-
class NameNotFoundException(Exception):

    """docstring for NameNotFoundException"""
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return self.arg


class ElementNotFoundException(Exception):
    """docstring for ElementNotFoundException"""
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return self.arg


class NoElementFoundExeception(Exception):
    """docstring for NoElementFoundExeception"""
    def __init__(self):
        super(NoElementFoundExeception, self).__init__()
