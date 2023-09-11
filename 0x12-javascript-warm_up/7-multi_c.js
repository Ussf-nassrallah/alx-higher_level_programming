#!/usr/bin/node
// script that prints x times “C is fun”
const { argv } = require('process');
if (isNaN(argv[2]) || argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(argv[2]);
  for (let index = 0; index < x; index++) {
    console.log('C is fun');
  }
}
