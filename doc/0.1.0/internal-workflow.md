Internal Workflow for generation
================================

This page explains how the version 0.1.0 works. Currently input is a JSON document.

## How it works

DIY follows this workflow:

1. Call diy.py script like : ./diy -i INPUT_FILE. INPUT_FILE must be a text file containing DIY language. Each object is an element in your diagram
diy open the file and calls Parse.parse to transform DIY language into Python List where each element is a Dictionary. List is passed to Interpretor. Interpretor will generate SVG output.

1. Parser. This object is in parser.py. Parser.parse will transform every elements into Dictionary. All these object are append in a List.

1. Interpretor. Interpretor is a main object of DIY. It merges each Dictionary element with related root element (located in lib/templates/default/json), transform grib position in valid pixel position (see grid.md). After that, call SvgRender object to transform json to svg

1. SvgRender. SvgRender transform each element to svg element. It matches json.type.json to json.type.svg
