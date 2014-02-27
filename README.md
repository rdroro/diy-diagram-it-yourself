diy-diagram-it-yourself
=======================

DIY - Diagram It Yourselft is a markdown language for easily describe the diagrams in your code documentation (interaction, dependance, workflow), on wiki pages or just to share diagrams with others people. Do not use specific software to share diagram with people, use DaaC (Diagram as a Code) ;)

For example draw this:

![Diagram example](http://i.imgur.com/B5VlgIF.png)

by writing this:

    desktop(link: DIY program)
    box(name: DIY program; position: 1,0; link: Diagram, Parser, Interpretor)
    circle(name: Diagram; position: 1,2)
    box(name: Parser; position: 2, 0)
    box(name: Interpretor; position: 2, 1; link: Grid Management, SvgRender)
    box(name: Grid Management; position: 3, 0)
    box(name: SvgRender; position: 3, 1)
    github(position: 3,3)

## Philosophy

+ GUI sucks : I want to edit my diagram from my text editor
+ Less is more : I do not want to write a book for simple diagrams
+ It's Beautiful : I want a beautiful theme by default. Tired of ugly diagrams
+ It's Ugly : AAAH, the default theme sucks, let me make it myself
+ Code sucks : Bah, code sucks, give me a GUI
+ Cross-platform : I'm sick of files that you can't edit without installing a gas-factory

## Get Started

### Installation

+ Download the lastest stable version here (version = 0.1.0 will be released soon). For the dev version : [Download](https://github.com/rdroro/diy-diagram-it-yourself/archive/master.zip)
+ Unzip archive
+ the tools is into diy-diagram-it-yourself/bin/diy

If you want, you can add diy to your path

    export PATH=${PATH}:/path/to/unizpped-archive/diy-diagram-it-yourself/bin

### First test

To test diy you can create a demo.diy file contaning:

    box(name: DIY Language; position: 0,0; link: DIY Program)
    circle(name: DIY Program; position: 1,0; link: SVG Diagram)
    box(name: SVG Diagram; position: 2, 0 )

and run:

    diy -i demo.diy

diagram.svg is now available in your working directory.

![Simple Exampla](http://i.imgur.com/fRAhi9c.png)

Next ? See [documentation](doc/0.1.0/)


## License

The MIT License (MIT)

Copyright (c) 2013-2014 Romain Dubos

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

