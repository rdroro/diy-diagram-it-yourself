#!/usr/bin/python

"""
main program to transform DIY language in diagramm

"""

import sys
import getopt
from os import path
from time import time
from parser import Parser
from interpretor import Interpretor


version = '0.1.0Alpha'


def usage():
	print '================'
	print 'Usage: diy is a tool to transform DIY language in diagram'
	print 'diy [path_to_diy_file] options:'
	print '\t-h, --help: Display this help'
	print '\t-v, --version: print diy version'
	print '\t-o, --output=: path to output svg file'
	print '\t-i, --input=: path to input diy file'
	print ''
	return

"""
Simple function to add content into the file.
delete all previous content
@param filePath string path to the file
@param content string content to write
"""
def writeFile(filePath, content):
	tmp = open(filePath, 'w')
	tmp.write(content)
	tmp.close()
	return


def start(input_file, output_file):

	if not path.exists(input_file):
		print '[ERROR] file: '+input_file+' does not exist'
		usage()
		sys.exit(110)

	markdown = open(input_file)

	json = Parser.parse(markdown)

	interpretor = Interpretor(json)
	result = interpretor.generate()

	stats = result['stats']
	document = result['diy']
	writeFile(output_file, document.__str__())
	markdown.close()
	return stats


def printStats(stats):
	print " ------------------------- "
	print "|          Stats          |"
	print " ------------------------- "
	for key, value in stats.iteritems():
		print "|   "+key+"   |   "+value.__str__()+"   |"
		print " ------------------------- "


def main():
	start_time = time()
	argv = sys.argv
	argv = argv[1:]
	if len(argv) < 1:
		print '[ERROR] diy needs one parameter at least'
		usage()
		sys.exit(100)


	output_file = "demo.svg"
	try:
		opts, args = getopt.getopt(argv, ":hi:vo:", ['help', 'version', 'output=', 'input='])
	except getopt.GetoptError as err:
		print ''
		print err
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
			sys.exit(0)
		elif opt in ('-o', '--output'):
			print arg
			output_file = arg
		elif opt in ('-v', '--version'):
			print 'diy version '+version
			sys.exit(0)
		elif opt in ('-i', '--input'):
			input_file = arg
			INPUT = arg
		else:
			# first argument must be input file
			# @todo
			usage()
			sys.exit(9000)
	
	stats = start(input_file, output_file)
	end_time = time()
	during_time = end_time - start_time

	print "Diagram generated in "+str(during_time)+" seconds"
	printStats(stats)



if __name__ == "__main__":
    main()