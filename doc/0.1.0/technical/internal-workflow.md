Internal Workflow for generation
================================

This page explains how the version 0.1.0 works. Currently input is a JSON document.

## How it works

DIY follows this workflow:

1. Call diy.py script like : ./diy -i INPUT_FILE. INPUT_FILE must be a valid JSON Array which contains JSON object. Each object is an element in your diagram
diy.py just open INPUT_FILE and call Parser with associated File Objects

1. Parser. This object is in parser.py. Currently, it doesn't make amazing stuff. It just transform File Object to JSON object. In future, Parser need to transform DIY language to JSON. Next, Parser create an Interpretor object with JSON object in contructor method and call Interpretor.generate() method

1. Interpretor. Interpretor is a main object of DIY. It merges each JSON element with related root element (located in lib/templates/default/json), transform grib position in valid pixel position (see grid.md) and eval calculated value of root element identified by ## ##. After that, call SvgRender object to transform json to svg

1. SvgRender. SvgRender transform each element to svg element. It matches json.type.json to json.type.svg
