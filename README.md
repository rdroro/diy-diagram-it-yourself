diy-diagram-it-yourself
=======================

DIY - Diagram It Yourself is a markdown language to easily describe the diagrams (interaction, dependence, workflow) in your code documentation, on wiki pages or just to share diagrams with others people. Do not use specific software to share diagram with people, use DIY and discover a new approach: The DaaC (Diagram as a Code) ;)

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

+ **GUI sucks** : I want to edit my diagram from my text editor
+ **Less is more** : I do not want to write a book for simple diagrams
+ **It's Beautiful** : I want a beautiful theme by default. Tired of ugly diagrams
+ **It's Ugly** : AAAH, the default theme sucks, let me make it myself - not implemented in 0.2.0
+ **Code sucks** : AAAH, code sucks, give me a GUI - not implemented in 0.2.0
+ **Cross-platform** : I'm sick of files that you can't edit without installing a gas-factory

## Get Started

### Installation

@todo Write the installation process via npm

### First test

To test diy you can create a demo.diy file containing:

    box(name: DIY Language; position: 0,0; link: DIY Program)
    circle(name: DIY Program; position: 1,0; link: SVG Diagram)
    box(name: SVG Diagram; position: 2, 0 )

and run:

    diy -i demo.diy

diagram.svg is now available in your working directory.

![Simple Example](http://i.imgur.com/fRAhi9c.png)

Next ? See [documentation](doc/0.1.0/)

## Contribute

If you want to contribute, the pull requests are welcome !

Just check the [contribute draft page](doc/0.1.0/contribute.md) before submit your code.


## License

This program is under the GNU General Public License v3.0

Copyright (C) 2013-2014 Romain Dubos

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
