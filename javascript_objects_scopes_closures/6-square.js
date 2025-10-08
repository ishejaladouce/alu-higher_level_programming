#!/usr/bin/node
// 6-square.js
// Defines a Square class with custom charPrint() method

const Square5 = require('./5-square');

class Square extends Square5 {
  // Prints the square using the given character 'c'
  // If 'c' is undefined, it defaults to 'X'
  charPrint (c) {
    const printChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(printChar.repeat(this.width));
    }
  }
}

module.exports = Square;
