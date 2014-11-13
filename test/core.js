var Parser = require('../bin/parser.js');
var assert = require("assert"); // node.js core module
var _ = require('lodash');
var path = require('path');
var fs = require('fs');
var lib = path.join(path.dirname(fs.realpathSync(__filename)), '../lib/templates/default');
var jsonlib = require(lib+'/json/default.js');

var validEltname        = 'box()';
var errorEltName        = 'box(';
var validOneAttr        = 'box(name: Controller)';
var validMultipleAttr   = 'box(name:controller; position:1,0 ; x:34; y:45)';
var validMultipleElt   = 'box(name: Model;  position : 1,0) \n circle()';
var validMultipleElt2   = 'box(name: Model;  position : 1,0) \n circle(name: Controller)';

describe('Parser.js', function(){

  describe('Test regexp', function(){

    it('The string "'+validEltname+'" is a valid regular expression', function(){
      assert.equal(true, Parser.test(validEltname));
    });

    it('The string "'+errorEltName+'" is not a valid regular expression', function () {
      assert.equal(false, Parser.test(errorEltName));
    });

    it('The string "'+validOneAttr+'" is a valid regular expression', function () {
      assert.equal(true, Parser.test(validOneAttr));
    });

    it('The string "'+validMultipleAttr+'" is a valid regular expression', function () {
      assert.equal(true, Parser.test(validMultipleAttr));
    });

    it('The string "'+validMultipleElt+'" is a valid regular expression', function () {
      assert.equal(true, Parser.test(validMultipleElt));
    });

    it('The string "'+validMultipleElt2+'" is a valid regular expression', function () {
      assert.equal(true, Parser.test(validMultipleElt2));
    });

  });

  describe('Parse string', function () {
    it('The string "'+validEltname+'" must return [["box"]] ', function (){
      var eval = Parser.parse(validEltname);
      assert.deepEqual([['box']], eval);
    });

    it('The string "'+validOneAttr+'" must return ["box", "name:Controller"]', function () {
      var eval = Parser.parse(validOneAttr);
      assert.deepEqual([['box', 'name:Controller']], eval);
    });

    it('The string "'+validMultipleAttr+'" must return [["box", "name:controller", "position:1,0", "x:34", "y:45"]]', function () {
      var eval = Parser.parse(validMultipleAttr);
      assert.deepEqual([["box", "name:controller", "position:1,0", "x:34", "y:45"]], eval);
    });

    it('The string "'+validMultipleElt+'" must return [["box", "name:Model", "position:1,0"],["circle"]]', function () {
      var eval = Parser.parse(validMultipleElt);
      assert.deepEqual([["box", "name:Model", "position:1,0"],["circle"]], eval);
    });

    it('The string "'+validMultipleElt2+'" must return [["box", "name:Model", "position:1,0"],["circle", "name:Controller"]]', function () {
      var eval = Parser.parse(validMultipleElt2);
      assert.deepEqual([["box", "name:Model", "position:1,0"],["circle", "name:Controller"]], eval);
    });
  });

  var fs = require('fs');
  var jsonRefPath = 'lib/templates/default/json/';
  describe('Compile array', function () {
    it('The array [["box", "name:controller", "position:2,2"]] must return a JSON array of one box object', function () {
      var box = _.clone(jsonlib.elements.box);
      box.name = 'controller';
      box.position = '2,2';

      var expected = [box];
      var arr = [['box', 'name:controller', 'position:2,2']];
      assert.deepEqual(expected, Parser.compile(arr));
    });

    it('Test if multiple elements compile', function () {
      var box = _.clone(jsonlib.elements.box);
      box.name = 'controller';

      var circle = _.clone(jsonlib.elements.circle);

      var expected = [box, circle];
      var arr = [['box', 'name:controller'], ['circle']];
      assert.deepEqual(expected, Parser.compile(arr));
    });
  });

});
