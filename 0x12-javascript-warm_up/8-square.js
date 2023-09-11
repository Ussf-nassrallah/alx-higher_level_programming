#!/usr/bin/node
// script that prints a square
const { argv } = require('process');
if (isNaN(argv[2]) || argv[2] === undefined) {
  console.log('Missing size');
} else {
  const size = Number(argv[2]);
  let output = '';
  for (let x = 0; x < size; x++) {
    output += 'x';
  }
  for (let y = 0; y < size; y++) {
    console.log(output);
  }
}