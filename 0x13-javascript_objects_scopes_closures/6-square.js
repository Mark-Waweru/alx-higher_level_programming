#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c == undefined) {
      for (let i = 0; i < this.height; i++) {
	let s = '';
        for (let j = 0; j < this.width; j++) {
          s += 'X';
	}
	console.log(s);
      }
    } else {
        for (let i = 0; i < this.height; i++) {
	  let s = '';
          for (let j = 0; j < this.width; j++) {
            s += c;
	  }
	  console.log(s);
        }
      }
  }
}

module.exports = Square;
