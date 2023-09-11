#!/usr/bin/node
// script that prints the addition of 2 integers
const { argv } = require('process');
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

function add (a, b) {
  return a + b;
}

const result = add(a, b);
console.log(result);
