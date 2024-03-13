#!/usr/bin/node
const { argv } = require('node:process');

const intVal = parseInt(argv[2]);

if (isNaN(intVal)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= intVal; i++) {
    console.log('C is fun');
  }
}
