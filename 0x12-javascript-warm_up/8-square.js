#!/usr/bin/node
const proc = require('process');
const num1 = Number(proc.argv[2]);
const num2 = Number(proc.argv[2]);
let i = 0;
let j = 0;
if ((num1 !== num2) || num1 === undefined) {
  console.log('Missing size');
} else {
  while (i < num1) {
      console.log('x' * num1);
    i++;
  }
}
