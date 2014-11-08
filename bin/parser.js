'user strict';

(function (exports) {
	var _ = require('lodash');
	var reEltName = '([a-z]+)';
	var reFirstAttr = '([a-z]+:[\\w,]+)?';
	var reSecondAttr = '(?:;([a-z]+:[\\w,]+))*';
	var reAllStr = '^'+reEltName+'\\('+reFirstAttr+reSecondAttr+'\\)$';

	/**
	* Remove all white space characters from a input sting
	* @param {string} input - The string that need to be clear
	* @return {string} the input string without white space charaters
	*/
	var clearWhiteSpaceChar = function (input) {
		return input.replace(/[ \t]/g, '');
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
	*
	*/
	exports.parse = function (input) {
		var str = clearWhiteSpaceChar(input);
		var reAll = new RegExp(reAllStr, 'gm');
		var elt = [];
		while (match = reAll.exec(str)) {
			// remove the first elt because it's the full regexp match
			// remove the two last elements because it's index and input
			match = match.splice(1, match.length);
			// remove the undefined items
			_.remove(match, function (item) { return typeof item === 'undefined' });
			elt.push(match);
		}
		return elt;
	};
})(exports);
