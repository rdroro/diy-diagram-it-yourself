Get Started
===========

DIY Language is pretty simple. It looks like:

    box(name: DIY Language; position: 0,0; link: DIY Program)
    circle(name: DIY Program; position: 1,0; link: SVG Diagram)
    box(name: SVG Diagram; position: 2, 0 )

What this code will generate ? This following diagram:

![Simple diamgram](http://i.imgur.com/fRAhi9c.png)

Cool isn't it?

To write your own diagrams, just follow the syntax:

    ELEMENT_NAME([ATTRIBUTE: VALUE;])

ELEMENT_NAME: is a name of the element to draw. List of available elements is [here](elements.md)

ATTRIBUTE: VALUE: The attribute of one element represented by key/value pairs. To separate them, you need to use ';' All elements have the defaults attributes/value:
* name: To define the name of element. This name can be drawn into the element (cf. [Elements page](elements.md) to see the behavior of each element). name attributes is also used to link elements together.
* position: To define the position of an element. X and Y coordinates separated by ',' See [grid.md](grid.md)
* vertical-align: The vertical alignment of the element into the cell. Possible value: top, middle, bottom
* horizontal-align: The horizontal alignment of the element into the cell. Possible value: left, middle, right

## Links: particular elements

To link elements together, there is two ways. With the first one, just put the name of element into link attribute as the previous example.

    box(name: DIY Language; link: DIY Program)
    box(name: DIY Program; position: 1,0)

 Do you need to link multiple elements ? Just separated them with ',' like:

    box(name: DIY Language; link: DIY Program, Other box)
    box(name: DIY Program; position: 1,0)
    box(name: Other box; position: 1, 1)

If for some reasons, you want to externalize links you can write

    box(name: DIY Language)
    box(name: DIY Program; position: 1,0)
    box(name: Other box; position: 1, 1)
    link(from: DIY Language; to: DIY Program)
    link(from: DIY Language; to: Other Box)

Currently, if you use link element, you need to describe all links. In fact, link element does not support multiple "to:" values separated by ','

Note that all links (in attribute or as an element) are evaluated after all other elements even if they are defined before.
