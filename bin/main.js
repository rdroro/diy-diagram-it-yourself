#!/usr/bin/env node
console.time('Diagram generated in');
var fs = require('fs');
var program = require('commander');
var Parser = require('./parser.js');
var Interpreter = require('./interpreter.js');

program
.version('0.2.0')
.option('-o, --output [dest]', 'Specify the path to the destination file')
.parse(process.argv);

if (process.argv.length < 3) {
  program.help();
  process.exit(1);
}

if (! program.output) {
  program.output = 'diagram.html';
}

program.input = process.argv[2];

fs.readFile(program.input, 'utf8', function (err, data) {
  if (err) {
    console.log('File ""'+program.input+'"" does not exists');
    process.exit(1);
  }
  var tab = Parser.parse(data);
  var jsonArray = Parser.compile(Parser.parse(data));
  var svg = Interpreter.jsonToSvg(jsonArray);
  var html = '<html><body><svg width="100%" height="100%">'+svg+'</svg></body>';
  fs.writeFileSync(program.output, html, {encoding: 'utf8'});
  console.log('Output: '+program.output);
  console.timeEnd('Diagram generated in');
});
