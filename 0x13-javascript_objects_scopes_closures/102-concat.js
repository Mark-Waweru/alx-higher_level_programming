#!/usr/bin/node

const fSource = require('fs');

const fArg = fSource.readFileSync(process.argv[2]).toString();
const sArg = fSource.readFileSync(process.argv[3]).toString();
fSource.writeFileSync(process.argv[4], fArg + sArg);
