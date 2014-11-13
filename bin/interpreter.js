(function (exports) {
  'use strict';

  var Handlebars = require('handlebars');
  var fs = require('fs');
  var _ = require('lodash');
  var path = require('path');
  var lib = path.join(path.dirname(fs.realpathSync(__filename)), '../lib/templates/default');
  var jsonlib = require(lib+'/json/default.js');
  var svglib = require(lib+'/svg/default.js');

  var convertPosition = function (position) {
    if (!position) {
      return {x:0, y:0};
    }
    var coord = position.split(',');
    return {x: coord[0]*200, y: coord[1]*100};
  };

  var addLinks = function (elements) {

    var linksArray = [];
    for (var i=0; i<elements.length; i++) {
      var elt = elements[i];
      var linkedElt = [];
      if (elt.type === 'link') {
        linkedElt.push(elt.to);
        elt = elements[_.findIndex(elements, {name: elt.from})];
      } else {
        if (!elt.link){
          continue;
        }
        linkedElt = elt.link.split(',');
      }
      for (var j=0; j<linkedElt.length; j++) {
        var suchLinkedElt = linkedElt[j];
        var endIndex = _.findIndex(elements, {name: suchLinkedElt});
        var endObj = elements[endIndex];
        var link = {
          type:'link',
          xStart: elt.xCenter + elt.x,
          yStart: elt.yCenter + elt.y,
          xEnd: endObj.xCenter + endObj.x,
          yEnd: endObj.yCenter + endObj.y
        };
        linksArray.push(link);
      }
    }
    return linksArray;
  };

  var getSvgString = function (type) {
    var svgSource = fs.readFileSync(lib+'/svg/'+type+'.svg', 'utf8');
    return svgSource;
  };

  exports.jsonToSvg = function (jsonArray) {
    var str = '';
    var elementDiagram = '';
    for (var i = 0; i < jsonArray.length; i++) {
      var element = jsonArray[i];
      if (element.type === 'link') {
        continue;
      }
      var svgSource = _.clone(svglib.elements[element.type]);
      var template = Handlebars.compile(svgSource);
      _.merge(element, convertPosition(element.position));
      element.x += element['horizontal-middle'];
      element.y += element['vertical-middle'];
      elementDiagram += '\n'+template(element);
    }
    var links = addLinks(jsonArray);

    var svgLinkSource = _.clone(svglib.elements.link);
    var linkDiagram = '';
    var linkTemplate = Handlebars.compile(svgLinkSource);

    for (var j = 0; j < links.length; j++) {
      var link = links[j];
      var jsonSource = _.clone(jsonlib.elements.link);

      _.merge(jsonSource, link);
      linkDiagram += linkTemplate(jsonSource);
    }
    str = linkDiagram + elementDiagram;
    return str;
  };

})(exports);
