#!/usr/bin/node
const { argv } = require('node:process');

const intVal = parseInt(argv[2]);

if (!isNaN(intVal)) {
  console.log('My number: ' + intVal);
} else {
  console.log('Not a number');
}
