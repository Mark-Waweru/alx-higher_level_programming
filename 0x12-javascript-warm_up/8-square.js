#!/usr/bin/node
const { argv } = require('node:process');

const size = parseInt(argv[2]);

if (!isNaN(size)) {
  for (let i = 1; i <= size; i++) {
    let row = '';
    for (let j = 1; j <= size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
