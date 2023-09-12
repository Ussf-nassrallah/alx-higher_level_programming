#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle
const SquareParent = require('./5-square.js');

class Square extends SquareParent {
  charPrint (c) {
    let char;

    if (typeof c === 'undefined') {
      char = 'X';
    } else {
      char = c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
