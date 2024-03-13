#!/usr/bin/node
const { argv } = require('node:process');

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

if (argv.length <= 3) {
  console.log('NaN');
} else {
  add(a, b);
}

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
