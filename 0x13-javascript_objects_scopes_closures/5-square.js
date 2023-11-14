#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    // Call constructor of base class (Rectangle)
    super(size, size);
  }
}

module.exports = Square;
