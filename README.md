diy-diagram-it-yourself
=======================

DIY - Diagram It Yourselft is a markdown language for describing easily the schemes in your code documentation to illustrate interaction, dependance, etc, on wiki pages or just to share diagrams with others people without specific software

This tools is under development. Specific markdown language are not defined yet. Currently, we use JSON to
describe diagram

## Get Started

### Installation

* Download the lastest stable version here (version = 0.1.0 will be released soon). For the dev version : [Download](https://github.com/rdroro/diy-diagram-it-yourself/archive/master.zip)
* Unzip archive
* If you want, you can add diy to your path:

    export PATH=${PATH}:/path/to/unizpped-archive/diy-diagram-it-yourself/bin

### First test

To test diy you can create a demo.diy file contaning this following content:

    box(name: DIY Language; position: 0,0; link: DIY Program)
    circle(name: DIY Program; position: 1,0; link: SVG Diagram)
    box(name: SVG Diagram; position: 2, 0 )

and run:

    diy -i path demo.diy

diagram.svg is now available in your working directory.



## Philosophy

+ GUI sucks : I want to edit my diagram from my text editor
+ Less is more : I do not want to write a book for simple diagrams
+ It's Beautiful : I want a beautiful theme by default. Tired of ugly diagrams
+ It's Ugly : AAAH, the default theme sucks, let me make it myself
+ Code sucks : Bah, code sucks, give me a GUI
+ Cross-platform : I'm sick of files that you can't edit without installing a gas-factory

# Todo

* Rewrite code documentation using real convention
* Rewrite Unit-test
* Think of code organization: Done but can be improve

