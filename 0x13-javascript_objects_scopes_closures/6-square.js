#!/usr/bin/node
const NewSquare = require('./5-square.js');

module.exports = class Square extends NewSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = this.height; i; i--) {
      console.log(c.repeat(this.width));
    }
  }
};
