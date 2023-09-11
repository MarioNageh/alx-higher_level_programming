#!/usr/bin/node
exports.addMeMaybe = function (number, functionToCall) {
  number++;
  functionToCall(number);
};
