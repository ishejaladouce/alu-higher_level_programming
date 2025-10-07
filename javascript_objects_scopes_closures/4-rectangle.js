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
  print
