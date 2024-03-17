#!/usr/bin/node

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    const character = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}
module.exports = Square;
