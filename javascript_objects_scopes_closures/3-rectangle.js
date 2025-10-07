#!/usr/bin/node
// 3-rectangle.js
// Defines a Rectangle class with print() method

class Rectangle {
  constructor (w, h) {
    // Validate that w and h are positive integers (numbers > 0)
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      // Leave instance empty
      return;
    }

    this.width = w;
    this.height = h;
  }

  // Method to print the rectangle using 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
