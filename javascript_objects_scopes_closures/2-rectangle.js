#!/usr/bin/node
// 2-rectangle.js
// Defines a Rectangle class that validates width and height

class Rectangle {
  constructor (w, h) {
    // Validate that w and h are positive integers (numbers > 0)
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      // Do not set properties — keep the instance empty
      return;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
