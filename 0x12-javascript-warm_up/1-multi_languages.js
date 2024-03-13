#!/usr/bin/node

const myLine = {
  line1: 'C is fun',
  line2: 'Python is cool',
  line3: 'JavaScript is amazing'
};

for (const line in myLine) {
  console.log(myLine[line]);
}
