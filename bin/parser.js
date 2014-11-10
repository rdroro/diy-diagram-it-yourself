(function (exports) {
	'use strict';

	var _ = require('lodash');
	var fs = require('fs');
	var path = require('path');
	var lib = path.join(path.dirname(fs.realpathSync(__filename)), '../lib/templates/default');
	var jsonlib = require(lib+'/json/default.js');

	var reEltName = '([a-z]+)';
	var reFirstAttr = '([a-z]+:[\\w,]+)?';
	var reSecondAttr = '(?:;([a-z]+:[\\w,]+))*?';

	var reAllStr = reEltName+'\\('+reFirstAttr+reSecondAttr+'\\)';

	var reMatch = /([a-z]+)\((.*?)\)/g;
	var reMatchAttr = /(?:;?([\w,]+:[\w,]+))/g;

	/**
	* Remove all white space characters from a input sting except "\n"
	* @private
	* @param {string} input - The string that need to be clear
	* @return {string} the input string without white space charaters
	*/
	var clearWhiteSpaceChar = function (input) {
		return input.replace(/\s/g, '');
	};

	/**
	* Test if the string input is a valid diy string
	* @param {string} input - The string that need to be test
	* @return {boolean} true if the input string is valid, false otherwise
	*/
	exports.test = function (input) {
		var str = clearWhiteSpaceChar(input);
		var reAll = new RegExp(reAllStr, 'gm');
		return reAll.test(str);
	};

	/**
	* Parse the string in input to return Array where each element are in its
	* array
	* @param {string} input - The string that need to be parse
	* @return {Array} like [["box", "name:boxName"],["circle"]]
	*/
	exports.parse = function (input) {
		// test regex before parse via test()
		//@todo throw exception
		if (!this.test(input)) {
			console.log('Syntax problems in '+input);
			return -2;
		}
		var str = clearWhiteSpaceChar(input);
		var elt = [];
		var match = null;
		while ((match = reMatch.exec(str)) !== null) {
			var tmp = [];
			tmp.push(match[1]);
			var attrs = null;
			while ( (attrs = reMatchAttr.exec(match[2])) !== null) {
				// attrs = attrs.splice(1, attrs.length);
				tmp = tmp.concat(attrs[1]);
			}
			elt.push(tmp);
		}
		return elt;
	};

	/**
	* Compile an array from Parser.parse() to an array of objects
	* @param {array} arrayToCompile - The array from parse() function
	* @return {array} An array of objects where each object represent one element
	*/
	exports.compile = function (arrayToCompile) {
		if (!_.isArray(arrayToCompile)) {
			return null;
		}
		var compiledArray = [];
		for (var i = 0; i < arrayToCompile.length; i++) {
			var element = arrayToCompile[i];
			var obj = {type: element[0]};
			for (var j=1; j < element.length; j++) {
				var attr = element[j].split(':');
				obj[attr[0]] = attr[1];
			}
			var ref = jsonlib.elements[element[0]];
			ref = _.clone(ref);
			var obj2 = _.merge(ref, obj);
			compiledArray.push(ref);
		}
		return compiledArray;
	};

})(exports);
