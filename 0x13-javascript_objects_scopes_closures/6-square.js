#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  constructor(size) {
    // Call constructor of base class (SquareBase) with size
    super(size);
  }

  charPrint(c) {
    // If c is undefined, use character X; otherwise, use provided character c
    if (c === undefined) {
      c = 'X';
    }

    // Print square using specified character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
