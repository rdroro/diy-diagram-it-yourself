#!/usr/bin/python

"""
main program to transform DIY language in diagramm

"""

import sys
import getopt
from os import path
from parser import Parser


version = '0.0.1'


def usage():
	print '================'
	print 'Usage: diy tool to transform DIY language in diagram'
	print 'diy [path_to_diy_file] options:'
	print '\t-h, --help: Display this help'
	print '\t-v, --version: print diy version'
	print '\t-o, --output: path to output svg file'
	print '\t-i, --input: path to input diy file'
	print ''
	return


def start(input_file):
	if not path.exists(input_file):
		print '[ERROR] file: '+input_file+' does not exist'
		usage()
		sys.exit(110)
	print "gg"
	json = open(input_file)
	parser = Parser(json)
	parser.parse()
	json.close()


def main():
	argv = sys.argv
	argv = argv[1:]
	if len(argv) < 1:
		print '[ERROR] diy needs one parameter at least'
		usage()
		sys.exit(100)


	try:
		opts, args = getopt.getopt(argv, ":hi:vo:", ['help', 'version', 'output', 'input'])
	except getopt.GetoptError as err:
		print ''
		print err
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
		elif opt in ('-v', '--version'):
			print 'diy version '+version
		elif opt in ('-i', '--input'):
			start(arg)		
		else:
			# first argument must be input file
			# @todo
			print "Shame ..."


if __name__ == "__main__":
    main()