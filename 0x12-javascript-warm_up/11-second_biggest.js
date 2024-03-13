#!/usr/bin/node
const argv = process.argv.slice(2).map(Number);

if (argv.length <= 3) {
  console.log('0');
} else {
  const max1 = Math.max(...argv);
  const index = argv.indexOf(max1);
  argv.splice(index, 1);
  const max2 = Math.max(...argv);
  console.log(max2);
}
