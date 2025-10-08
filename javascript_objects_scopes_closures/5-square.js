#!/usr/bin/node
// 5-square.js
// Defines a Square class that inherits from Rectangle

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call the parent class constructor with width and height equal to size
    super(size, size);
  }
}

module.exports = Square;
