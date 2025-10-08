#!/usr/bin/node
// 9-logme.js
// Prints the number of arguments already printed and the new argument value

let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
