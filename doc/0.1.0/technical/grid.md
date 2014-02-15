Grid management
===============

## How it works

The hole diagram is in grid layout. You can put an element into the cell by adding x and y parameters as:
    
    {
    "type": "box",
    "name": "Grid System"
    "x": "3",
    "y": "2"
    }

As you see, to set an element into a cell, just type x and y parameters where x is the column number and y is the row number.


You can define a specific number of columns/rows for your diagram. By default, new diagram is set
with 4 columns and 3 rows.

Currently, diagram is not dynamic. You must specify the size of the diagram if elements position are out of bound 
