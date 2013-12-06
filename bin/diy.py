#!/usr/bin/python

"""
main program to transform DIY language in diagramm

"""

import sys, getopt
from parser import Parser

version = '0.0.1'

def usage ():
	print '================'
	print 'Usage: diy tool to transform DIY language in diagram'
	print 'diy options:'
	print '\t-h: Display this help'
	print '\t-v: print diy version'
	print '\t-o: path to output svg file'
	print ''
	return

def main ():
	argv = sys.argv
	argv = argv[1:]

	try:
		opts, args = getopt.getopt(argv, "hvo:", ['help', 'version', 'output'])
	except getopt.GetoptError as err:
		print ''
		print err
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			json = open('../tests/json')
			parser = Parser(json)
			parser.parse()
			usage()
		elif opt in ('-v', '--version'):
			print 'diy version '+version
		
		else:
			usage()

if __name__ == "__main__":
    main()