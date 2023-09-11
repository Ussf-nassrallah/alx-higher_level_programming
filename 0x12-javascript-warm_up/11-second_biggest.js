#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const { argv } = require('process');
if (argv.length <= 3) {
  console.log('0');
} else {
  const data = argv.slice(2).map(Number);
  const arg = data.sort(function (a, b) { return b - a; })[1];
  console.log(arg);
}