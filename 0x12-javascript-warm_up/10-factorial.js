#!/usr/bin/node
// script that computes and prints a factorial
const { argv } = require('process');

function factorial (num) {
  if (num < 0) {
    return (-1);
  }

  if (num === 0 || isNaN(num)) {
    return (1);
  }

  return (num * factorial(num - 1));
}

console.log(factorial(parseInt(argv[2])));
