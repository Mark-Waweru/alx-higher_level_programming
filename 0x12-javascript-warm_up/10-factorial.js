#!/usr/bin/node
const { argv } = require('node:process');

const factorialNum = parseInt(argv[2]);

if (argv.length <= 2) {
  console.log('1');
} else {
  const ans = factorial(factorialNum);
  console.log(ans);
}

function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
