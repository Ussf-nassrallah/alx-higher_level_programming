#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let char;

    if (typeof c === 'undefined') {
      char = 'X';
    } else {
      char = c;
    }

    for (let i = 0; i < this.size; i++) {
      console.log(char.repeat(this.size));
    }
  }
}

module.exports = Square;
