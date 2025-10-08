#!/usr/bin/node
// 10-converter.js
// Returns a function that converts a number from base 10 to another base

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
