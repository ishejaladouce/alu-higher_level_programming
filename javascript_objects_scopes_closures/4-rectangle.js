#!/usr/bin/node
// 4-rectangle.js
// Defines a Rectangle class with print, rotate, and double methods

class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  // Prints the rectangle using 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Swaps the width and height
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Doubles the dimensions
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
