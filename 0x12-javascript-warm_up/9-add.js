#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log('NaN');
} else {
  console.log(add(parseInt(args[2]), parseInt(args[3])));
}

function add (a, b) {
  return a + b;
}
