#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create empty object if w or h is equal to 0 or not positive integer
      Object.create(null);
    }
  }

  print() {
    // Print rectangle using character X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    // Exchange width and height of rectangle
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    // Multiply width and height of rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
